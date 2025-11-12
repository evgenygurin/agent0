"""
Autonomous AI Development Platform - Core Implementation

This module orchestrates the autonomous development cycle integrating:
- R2R for distributed memory and GraphRAG
- Codegen for safe code execution
- Linear for task management
- Multiple specialized AI agents
"""

import asyncio
import logging
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class TaskStatus(Enum):
    """Task lifecycle status"""
    PENDING = "pending"
    CLAIMED = "claimed"
    IN_PROGRESS = "in_progress"
    TESTING = "testing"
    REVIEW = "review"
    DEPLOYING = "deploying"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Task:
    """Represents a development task"""
    id: str
    title: str
    description: str
    priority: int
    labels: List[str]
    status: TaskStatus
    assigned_agent: Optional[str] = None
    created_at: datetime = None
    metadata: Dict = None


@dataclass
class AgentCapability:
    """Defines agent capabilities and constraints"""
    name: str
    can_handle_task_types: List[str]
    max_complexity: float
    thinking_budget_tokens: int
    requires_tools: List[str]


class AutonomousDevelopmentPlatform:
    """
    Main orchestrator for autonomous AI development

    This platform enables fully autonomous software development through:
    1. Distributed multi-agent collaboration
    2. Shared memory via R2R GraphRAG
    3. Safe code execution in Codegen sandboxes
    4. Continuous learning from outcomes
    """

    def __init__(self, config: Dict):
        """
        Initialize the autonomous platform

        Args:
            config: Platform configuration including API keys and settings
        """
        self.config = config
        self.running = False

        # Core components (initialized in start())
        self.memory = None
        self.linear = None
        self.github = None
        self.codegen = None
        self.event_bus = None
        self.decision_engine = None
        self.learning_system = None

        # Agent registry
        self.agents = {}
        self.agent_health = {}

        # Metrics
        self.metrics = {
            "tasks_completed": 0,
            "tasks_failed": 0,
            "deployments": 0,
            "incidents": 0,
            "learning_iterations": 0
        }

        logger.info("Autonomous Development Platform initialized")

    async def start(self):
        """
        Start the autonomous development platform

        Initializes all components and begins the autonomous loop
        """
        logger.info("🚀 Starting Autonomous Development Platform...")

        try:
            # Initialize core systems
            await self._initialize_core_systems()

            # Initialize agents
            await self._initialize_agents()

            # Setup integrations
            await self._setup_integrations()

            # Start monitoring
            asyncio.create_task(self._monitoring_loop())

            self.running = True
            logger.info("✅ Platform started successfully")

            # Enter autonomous development loop
            await self._autonomous_development_loop()

        except Exception as e:
            logger.error(f"❌ Failed to start platform: {e}")
            raise

    async def _initialize_core_systems(self):
        """Initialize R2R memory, event bus, decision engine"""
        from ..memory.r2r_memory_system import R2RMemorySystem
        from ..integrations.event_bus import EventBus
        from .decision_engine import DecisionEngine
        from .learning_system import LearningSystem

        logger.info("Initializing core systems...")

        # R2R Memory System with GraphRAG
        self.memory = R2RMemorySystem(
            base_url=self.config.get("r2r_url", "http://localhost:7272")
        )
        await self.memory.initialize()
        logger.info("✓ R2R Memory System initialized")

        # Redis-backed Event Bus
        self.event_bus = EventBus(
            redis_url=self.config.get("redis_url", "redis://localhost:6379")
        )
        await self.event_bus.connect()
        logger.info("✓ Event Bus initialized")

        # Decision Engine with risk assessment
        self.decision_engine = DecisionEngine(
            memory=self.memory,
            config=self.config.get("decision_engine", {})
        )
        logger.info("✓ Decision Engine initialized")

        # Learning System for continuous improvement
        self.learning_system = LearningSystem(
            memory=self.memory,
            metrics_store=self.metrics
        )
        logger.info("✓ Learning System initialized")

    async def _initialize_agents(self):
        """Initialize all specialized agents"""
        from ..agents.architect_agent import ArchitectAgent
        from ..agents.developer_agent import DeveloperAgent
        from ..agents.tester_agent import TesterAgent
        from ..agents.reviewer_agent import ReviewerAgent
        from ..agents.deployer_agent import DeployerAgent
        from ..agents.monitor_agent import MonitorAgent

        logger.info("Initializing agents...")

        agent_configs = [
            {
                "class": ArchitectAgent,
                "name": "architect",
                "capability": AgentCapability(
                    name="architect",
                    can_handle_task_types=["feature", "architecture", "design"],
                    max_complexity=10.0,
                    thinking_budget_tokens=8000,
                    requires_tools=["memory", "github"]
                )
            },
            {
                "class": DeveloperAgent,
                "name": "developer",
                "capability": AgentCapability(
                    name="developer",
                    can_handle_task_types=["implementation", "bug", "refactor"],
                    max_complexity=8.0,
                    thinking_budget_tokens=4000,
                    requires_tools=["memory", "github", "codegen"]
                )
            },
            {
                "class": TesterAgent,
                "name": "tester",
                "capability": AgentCapability(
                    name="tester",
                    can_handle_task_types=["testing", "qa"],
                    max_complexity=6.0,
                    thinking_budget_tokens=4000,
                    requires_tools=["codegen", "memory"]
                )
            },
            {
                "class": ReviewerAgent,
                "name": "reviewer",
                "capability": AgentCapability(
                    name="reviewer",
                    can_handle_task_types=["review", "quality"],
                    max_complexity=7.0,
                    thinking_budget_tokens=4000,
                    requires_tools=["memory", "github"]
                )
            },
            {
                "class": DeployerAgent,
                "name": "deployer",
                "capability": AgentCapability(
                    name="deployer",
                    can_handle_task_types=["deployment"],
                    max_complexity=5.0,
                    thinking_budget_tokens=2000,
                    requires_tools=["github", "monitoring"]
                )
            },
            {
                "class": MonitorAgent,
                "name": "monitor",
                "capability": AgentCapability(
                    name="monitor",
                    can_handle_task_types=["monitoring", "incident"],
                    max_complexity=8.0,
                    thinking_budget_tokens=4000,
                    requires_tools=["monitoring", "memory"]
                )
            }
        ]

        for agent_config in agent_configs:
            try:
                agent = agent_config["class"](
                    agent_id=agent_config["name"],
                    memory=self.memory,
                    event_bus=self.event_bus,
                    capability=agent_config["capability"]
                )

                # Initialize agent
                await agent.initialize()

                # Start agent's event loop
                asyncio.create_task(agent.start())

                self.agents[agent_config["name"]] = agent
                self.agent_health[agent_config["name"]] = "healthy"

                logger.info(f"✓ {agent_config['name']} agent initialized")

            except Exception as e:
                logger.error(f"Failed to initialize {agent_config['name']}: {e}")

        logger.info(f"Initialized {len(self.agents)} agents")

    async def _setup_integrations(self):
        """Setup Linear, GitHub, and Codegen integrations"""
        from ..integrations.linear_client import LinearClient
        from ..integrations.github_client import GitHubClient
        from ..integrations.codegen_client import CodegenClient

        logger.info("Setting up integrations...")

        # Linear for task management
        self.linear = LinearClient(
            api_key=self.config.get("linear_api_key")
        )

        # Setup Linear webhooks
        webhook_url = f"{self.config['platform_url']}/webhooks/linear"
        await self.linear.setup_webhook(
            url=webhook_url,
            events=["Issue.create", "Issue.update", "Comment.create"]
        )
        logger.info("✓ Linear integration configured")

        # GitHub for code repository
        self.github = GitHubClient(
            token=self.config.get("github_token"),
            repo=self.config.get("github_repo")
        )
        logger.info("✓ GitHub integration configured")

        # Codegen for sandbox execution
        self.codegen = CodegenClient(
            api_key=self.config.get("codegen_api_key")
        )
        logger.info("✓ Codegen integration configured")

    async def _autonomous_development_loop(self):
        """
        Main autonomous development loop

        Continuously:
        1. Fetch tasks from Linear
        2. Route to appropriate agents
        3. Monitor progress
        4. Learn from outcomes
        """
        logger.info("🔄 Entering autonomous development loop...")

        while self.running:
            try:
                # Check for new tasks
                tasks = await self._fetch_pending_tasks()

                if tasks:
                    logger.info(f"Found {len(tasks)} pending tasks")

                    for task in tasks:
                        # Emit task event for agents to pick up
                        await self.event_bus.emit({
                            "type": "task_created",
                            "task": task.__dict__,
                            "timestamp": datetime.now().isoformat()
                        })

                # Health check agents
                await self._check_agent_health()

                # Collect metrics
                await self._collect_metrics()

                # Sleep before next iteration
                await asyncio.sleep(self.config.get("poll_interval", 30))

            except Exception as e:
                logger.error(f"Error in autonomous loop: {e}")
                await asyncio.sleep(60)

    async def _fetch_pending_tasks(self) -> List[Task]:
        """Fetch pending tasks from Linear"""
        try:
            linear_issues = await self.linear.get_unassigned_tasks(
                limit=self.config.get("max_parallel_tasks", 10)
            )

            tasks = []
            for issue in linear_issues:
                task = Task(
                    id=issue["id"],
                    title=issue["title"],
                    description=issue.get("description", ""),
                    priority=issue.get("priority", 0),
                    labels=[label["name"] for label in issue.get("labels", [])],
                    status=TaskStatus.PENDING,
                    created_at=datetime.now()
                )
                tasks.append(task)

                # Store task in R2R memory
                await self.memory.store_task(task)

            return tasks

        except Exception as e:
            logger.error(f"Failed to fetch tasks: {e}")
            return []

    async def _check_agent_health(self):
        """Monitor agent health and restart if needed"""
        for agent_name, agent in self.agents.items():
            try:
                is_healthy = await agent.health_check()

                if not is_healthy and self.agent_health[agent_name] == "healthy":
                    logger.warning(f"⚠️ Agent {agent_name} became unhealthy")
                    self.agent_health[agent_name] = "unhealthy"

                    # Try to restart agent
                    await self._restart_agent(agent_name)

                elif is_healthy and self.agent_health[agent_name] == "unhealthy":
                    logger.info(f"✅ Agent {agent_name} recovered")
                    self.agent_health[agent_name] = "healthy"

            except Exception as e:
                logger.error(f"Health check failed for {agent_name}: {e}")

    async def _restart_agent(self, agent_name: str):
        """Restart a failed agent"""
        logger.info(f"🔄 Restarting agent {agent_name}")

        try:
            # Stop old agent
            if agent_name in self.agents:
                await self.agents[agent_name].stop()

            # Create new agent instance
            # (Implementation would depend on agent type)
            logger.info(f"✓ Agent {agent_name} restarted")

        except Exception as e:
            logger.error(f"Failed to restart {agent_name}: {e}")

    async def _collect_metrics(self):
        """Collect platform metrics"""
        try:
            # Get current system state
            active_tasks = len(await self._get_active_tasks())
            healthy_agents = sum(
                1 for status in self.agent_health.values()
                if status == "healthy"
            )

            metrics_snapshot = {
                "timestamp": datetime.now().isoformat(),
                "active_tasks": active_tasks,
                "healthy_agents": healthy_agents,
                "total_agents": len(self.agents),
                **self.metrics
            }

            # Store in R2R for analysis
            await self.memory.store_metrics(metrics_snapshot)

        except Exception as e:
            logger.error(f"Failed to collect metrics: {e}")

    async def _get_active_tasks(self) -> List[Task]:
        """Get all currently active tasks"""
        return await self.memory.get_tasks_by_status([
            TaskStatus.CLAIMED,
            TaskStatus.IN_PROGRESS,
            TaskStatus.TESTING,
            TaskStatus.REVIEW
        ])

    async def _monitoring_loop(self):
        """Background monitoring and alerting"""
        while self.running:
            try:
                # Check for incidents
                incidents = await self._check_for_incidents()

                if incidents:
                    logger.warning(f"⚠️ Detected {len(incidents)} incidents")

                    for incident in incidents:
                        await self.event_bus.emit({
                            "type": "incident_detected",
                            "incident": incident,
                            "timestamp": datetime.now().isoformat()
                        })

                await asyncio.sleep(60)  # Check every minute

            except Exception as e:
                logger.error(f"Monitoring loop error: {e}")
                await asyncio.sleep(60)

    async def _check_for_incidents(self) -> List[Dict]:
        """Check production systems for incidents"""
        incidents = []

        # Check error rates, latency, etc.
        # This would integrate with actual monitoring systems

        return incidents

    async def stop(self):
        """Gracefully stop the platform"""
        logger.info("🛑 Stopping Autonomous Development Platform...")

        self.running = False

        # Stop all agents
        for agent_name, agent in self.agents.items():
            try:
                await agent.stop()
                logger.info(f"✓ Stopped {agent_name}")
            except Exception as e:
                logger.error(f"Error stopping {agent_name}: {e}")

        # Close connections
        if self.event_bus:
            await self.event_bus.close()

        logger.info("✅ Platform stopped")


async def main():
    """Example usage"""
    config = {
        "r2r_url": "http://localhost:7272",
        "redis_url": "redis://localhost:6379",
        "linear_api_key": "YOUR_LINEAR_API_KEY",
        "github_token": "YOUR_GITHUB_TOKEN",
        "github_repo": "owner/repo",
        "codegen_api_key": "YOUR_CODEGEN_API_KEY",
        "platform_url": "https://your-platform.com",
        "poll_interval": 30,
        "max_parallel_tasks": 10,
        "decision_engine": {
            "auto_deploy_threshold": 0.8,
            "risk_threshold": 0.5
        }
    }

    platform = AutonomousDevelopmentPlatform(config)

    try:
        await platform.start()
    except KeyboardInterrupt:
        logger.info("Received shutdown signal")
        await platform.stop()


if __name__ == "__main__":
    asyncio.run(main())
