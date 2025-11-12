"""
Base Agent Class

Provides common functionality for all specialized agents:
- Event handling
- Memory access
- Tool usage
- Health monitoring
"""

import logging
import asyncio
from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from datetime import datetime
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class AgentCapability:
    """Defines what an agent can do"""
    name: str
    can_handle_task_types: List[str]
    max_complexity: float
    thinking_budget_tokens: int
    requires_tools: List[str]


class BaseAgent(ABC):
    """
    Base class for all autonomous agents

    Provides:
    - Event-driven coordination
    - Memory access via R2R
    - Health monitoring
    - Task claiming mechanism
    """

    def __init__(
        self,
        agent_id: str,
        memory,
        event_bus,
        capability: AgentCapability
    ):
        """
        Initialize base agent

        Args:
            agent_id: Unique agent identifier
            memory: R2R memory system
            event_bus: Event bus for coordination
            capability: Agent capabilities
        """
        self.agent_id = agent_id
        self.memory = memory
        self.event_bus = event_bus
        self.capability = capability

        # State
        self.running = False
        self.current_task = None
        self.health_status = "initializing"

        # Event handlers
        self.event_handlers = {}

        # Metrics
        self.metrics = {
            "tasks_handled": 0,
            "tasks_succeeded": 0,
            "tasks_failed": 0,
            "avg_task_duration": 0.0
        }

        logger.info(f"Agent {self.agent_id} initialized")

    async def initialize(self):
        """Initialize agent resources"""
        self.health_status = "healthy"
        logger.info(f"Agent {self.agent_id} ready")

    async def start(self):
        """
        Start agent event loop

        Listens for relevant events and handles them
        """
        self.running = True
        self.health_status = "healthy"

        logger.info(f"Agent {self.agent_id} started")

        # Subscribe to relevant events
        relevant_events = self.get_relevant_event_types()
        await self.event_bus.subscribe(
            relevant_events,
            self.handle_event
        )

        # Start health monitoring
        asyncio.create_task(self._health_monitor_loop())

    async def stop(self):
        """Stop agent gracefully"""
        logger.info(f"Stopping agent {self.agent_id}")

        self.running = False
        self.health_status = "stopped"

        # Finish current task if any
        if self.current_task:
            logger.info(f"Finishing current task: {self.current_task}")
            # Allow some time to finish
            await asyncio.sleep(10)

    @abstractmethod
    def get_relevant_event_types(self) -> List[str]:
        """
        Return list of event types this agent handles

        Must be implemented by subclasses
        """
        pass

    @abstractmethod
    async def process_task(self, task: Dict) -> Dict:
        """
        Process a task

        Must be implemented by subclasses

        Args:
            task: Task data

        Returns:
            Result dictionary
        """
        pass

    async def handle_event(self, event: Dict):
        """
        Route event to appropriate handler

        Args:
            event: Event data
        """
        event_type = event.get("type")

        logger.debug(f"Agent {self.agent_id} received event: {event_type}")

        # Check if we have a handler for this event
        handler = self.event_handlers.get(event_type)

        if handler:
            try:
                await handler(event)
            except Exception as e:
                logger.error(
                    f"Agent {self.agent_id} failed to handle {event_type}: {e}"
                )

                # Emit error event
                await self.event_bus.emit({
                    "type": "agent_error",
                    "agent_id": self.agent_id,
                    "event_type": event_type,
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                })

    def on_event(self, event_type: str):
        """
        Decorator to register event handlers

        Example:
            @agent.on_event("task_created")
            async def handle_task_created(self, event):
                ...
        """
        def decorator(func):
            self.event_handlers[event_type] = func
            return func
        return decorator

    async def should_handle_task(self, task: Dict) -> bool:
        """
        Decide if this agent should handle a task

        Checks:
        - Task type matches capabilities
        - Complexity within limits
        - No other task in progress
        - Required tools available
        """
        # Already handling a task
        if self.current_task:
            return False

        # Check task type
        task_type = task.get("type", "unknown")
        if task_type not in self.capability.can_handle_task_types:
            return False

        # Check complexity
        complexity = task.get("complexity", 5.0)
        if complexity > self.capability.max_complexity:
            logger.debug(
                f"Task complexity {complexity} exceeds agent limit "
                f"{self.capability.max_complexity}"
            )
            return False

        # Check if we have successful precedents
        precedents = await self._find_similar_tasks(task)
        if precedents:
            # More likely to handle if we have experience
            return True

        # New type of task - be cautious
        if complexity > self.capability.max_complexity * 0.7:
            return False

        return True

    async def _find_similar_tasks(self, task: Dict) -> List[Dict]:
        """Find similar tasks in memory"""
        try:
            query = f"{task.get('type')}: {task.get('description', '')}"

            results = await self.memory.search(
                query=query,
                collection="tasks",
                filters={
                    "agent_id": self.agent_id,
                    "status": "completed"
                },
                limit=5
            )

            return results

        except Exception as e:
            logger.warning(f"Failed to find similar tasks: {e}")
            return []

    async def claim_task(self, task_id: str) -> bool:
        """
        Atomically claim a task

        Uses Redis for distributed locking

        Args:
            task_id: Task identifier

        Returns:
            True if claimed successfully
        """
        try:
            claimed = await self.event_bus.claim_task(
                task_id=task_id,
                agent_id=self.agent_id,
                ttl=300  # 5 minute timeout
            )

            if claimed:
                self.current_task = task_id
                logger.info(f"Agent {self.agent_id} claimed task {task_id}")

                # Emit claimed event
                await self.event_bus.emit({
                    "type": "task_claimed",
                    "task_id": task_id,
                    "agent_id": self.agent_id,
                    "timestamp": datetime.now().isoformat()
                })

            return claimed

        except Exception as e:
            logger.error(f"Failed to claim task {task_id}: {e}")
            return False

    async def release_task(self, task_id: str):
        """Release a claimed task"""
        if self.current_task == task_id:
            self.current_task = None

        await self.event_bus.release_task(task_id)

    async def execute_task(self, task: Dict):
        """
        Execute a task with monitoring and error handling

        Args:
            task: Task data
        """
        task_id = task.get("id")
        start_time = datetime.now()

        try:
            logger.info(f"Agent {self.agent_id} executing task {task_id}")

            # Emit start event
            await self.event_bus.emit({
                "type": "task_started",
                "task_id": task_id,
                "agent_id": self.agent_id,
                "timestamp": datetime.now().isoformat()
            })

            # Process the task (implemented by subclass)
            result = await self.process_task(task)

            # Calculate duration
            duration = (datetime.now() - start_time).total_seconds()

            # Update metrics
            self.metrics["tasks_handled"] += 1
            self.metrics["tasks_succeeded"] += 1
            self.metrics["avg_task_duration"] = (
                (self.metrics["avg_task_duration"] *
                 (self.metrics["tasks_handled"] - 1) + duration) /
                self.metrics["tasks_handled"]
            )

            # Emit completion event
            await self.event_bus.emit({
                "type": "task_completed",
                "task_id": task_id,
                "agent_id": self.agent_id,
                "result": result,
                "duration": duration,
                "timestamp": datetime.now().isoformat()
            })

            # Store result in memory
            await self.memory.store_task_result(task_id, result)

            logger.info(
                f"Agent {self.agent_id} completed task {task_id} "
                f"in {duration:.1f}s"
            )

        except Exception as e:
            logger.error(
                f"Agent {self.agent_id} failed task {task_id}: {e}"
            )

            # Update metrics
            self.metrics["tasks_failed"] += 1

            # Emit failure event
            await self.event_bus.emit({
                "type": "task_failed",
                "task_id": task_id,
                "agent_id": self.agent_id,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            })

            raise

        finally:
            # Release task
            await self.release_task(task_id)

    async def think(self, prompt: str, context: Dict = None) -> str:
        """
        Use AI model for reasoning

        Args:
            prompt: Thinking prompt
            context: Additional context from memory

        Returns:
            Reasoning output
        """
        # This would integrate with actual AI model (Claude, GPT, etc.)
        # For now, placeholder

        logger.debug(f"Agent {self.agent_id} thinking: {prompt[:100]}...")

        # In real implementation:
        # - Load relevant context from R2R memory
        # - Call AI model with thinking prompt
        # - Return reasoning output

        return "AI reasoning output placeholder"

    async def retrieve_context(self, query: str, limit: int = 5) -> List[Dict]:
        """
        Retrieve relevant context from memory

        Args:
            query: Search query
            limit: Maximum results

        Returns:
            List of relevant documents
        """
        try:
            results = await self.memory.search(
                query=query,
                limit=limit
            )

            return results

        except Exception as e:
            logger.error(f"Failed to retrieve context: {e}")
            return []

    async def health_check(self) -> bool:
        """
        Check agent health

        Returns:
            True if healthy
        """
        if not self.running:
            return False

        if self.health_status != "healthy":
            return False

        # Check if stuck on a task
        if self.current_task:
            # If task is taking too long, might be stuck
            # Would check actual task duration here
            pass

        return True

    async def _health_monitor_loop(self):
        """Background health monitoring"""
        while self.running:
            try:
                # Self-check
                is_healthy = await self.health_check()

                if not is_healthy:
                    logger.warning(f"Agent {self.agent_id} health check failed")
                    self.health_status = "unhealthy"

                # Report metrics
                await self.event_bus.emit({
                    "type": "agent_heartbeat",
                    "agent_id": self.agent_id,
                    "health": self.health_status,
                    "metrics": self.metrics,
                    "timestamp": datetime.now().isoformat()
                })

                await asyncio.sleep(30)  # Every 30 seconds

            except Exception as e:
                logger.error(f"Health monitor error: {e}")
                await asyncio.sleep(30)

    def get_metrics(self) -> Dict:
        """Get agent metrics"""
        return {
            **self.metrics,
            "agent_id": self.agent_id,
            "capability": self.capability.name,
            "health": self.health_status,
            "current_task": self.current_task
        }
