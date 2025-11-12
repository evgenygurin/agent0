"""
Architect Agent

Responsible for:
- High-level system design
- Architectural decisions
- Task decomposition
- Technical planning
"""

import logging
from typing import Dict, List
from .base_agent import BaseAgent, AgentCapability

logger = logging.getLogger(__name__)


class ArchitectAgent(BaseAgent):
    """
    Architect agent for system design and planning

    Key capabilities:
    - System architecture design
    - Task decomposition into subtasks
    - Technology stack decisions
    - Architectural risk assessment
    """

    def __init__(
        self,
        agent_id: str,
        memory,
        event_bus,
        capability: AgentCapability
    ):
        super().__init__(agent_id, memory, event_bus, capability)
        self._setup_handlers()

    def _setup_handlers(self):
        """Register event handlers"""

        @self.on_event("task_created")
        async def handle_task_created(event):
            task = event.get("task")

            # Architect handles high-level tasks
            if task.get("type") in ["feature", "architecture"]:
                if await self.should_handle_task(task):
                    claimed = await self.claim_task(task["id"])

                    if claimed:
                        await self.execute_task(task)

    def get_relevant_event_types(self) -> List[str]:
        """Events this agent handles"""
        return ["task_created", "architecture_review_requested"]

    async def process_task(self, task: Dict) -> Dict:
        """
        Process architectural task

        Workflow:
        1. Analyze requirements deeply
        2. Research similar architectures
        3. Design system architecture
        4. Decompose into implementable tasks
        5. Assess risks
        6. Create technical specification
        """
        task_id = task["id"]

        logger.info(f"Architect agent designing solution for {task_id}")

        # Step 1: Deep requirement analysis
        analysis = await self._deep_analysis(task)

        # Step 2: Research existing patterns
        research = await self._research_architectures(task, analysis)

        # Step 3: Design architecture
        architecture = await self._design_architecture(
            task,
            analysis,
            research
        )

        # Step 4: Decompose into tasks
        subtasks = await self._decompose_tasks(architecture)

        # Step 5: Risk assessment
        risks = await self._assess_risks(architecture)

        # Step 6: Create specification
        spec = await self._create_specification(
            architecture,
            subtasks,
            risks
        )

        # Store architectural decision in memory
        await self._store_architecture_decision(architecture, spec)

        return {
            "success": True,
            "architecture": architecture,
            "subtasks": subtasks,
            "risks": risks,
            "specification": spec
        }

    async def _deep_analysis(self, task: Dict) -> Dict:
        """
        Deep analysis with extensive thinking

        Uses full 8K token budget for thorough reasoning
        """
        prompt = f"""
        Perform deep architectural analysis of this requirement:

        {task['title']}
        {task['description']}

        Consider:
        1. Functional requirements
        2. Non-functional requirements (performance, scalability, security)
        3. Integration points with existing systems
        4. Data models and flows
        5. User experience implications
        6. Technical constraints
        7. Future extensibility

        Think deeply about each aspect.
        """

        # Retrieve extensive context from codebase
        context = await self.retrieve_context(
            task['description'],
            limit=20  # More context for architect
        )

        # Use GraphRAG to understand system dependencies
        dependency_graph = await self._analyze_dependencies(task)

        analysis = await self.think(prompt, {
            **context,
            "dependencies": dependency_graph
        })

        return {
            "analysis": analysis,
            "dependencies": dependency_graph
        }

    async def _analyze_dependencies(self, task: Dict) -> Dict:
        """
        Use knowledge graph to understand system dependencies

        Queries R2R GraphRAG for:
        - Existing components that will be affected
        - Integration points
        - Dependency chains
        """
        try:
            # Find affected files/components
            affected = await self.memory.find_affected_components(
                task_description=task['description']
            )

            # Get dependency graph
            graph = await self.memory.get_dependency_graph(
                components=affected,
                depth=3
            )

            return graph

        except Exception as e:
            logger.warning(f"Failed to analyze dependencies: {e}")
            return {}

    async def _research_architectures(
        self,
        task: Dict,
        analysis: Dict
    ) -> Dict:
        """
        Research similar architectural solutions

        Uses R2R agentic RAG for multi-step research
        """
        logger.info("Researching architectural patterns...")

        query = f"""
        Find architectural patterns for: {task['title']}

        Requirements: {analysis['analysis'][:500]}

        Look for:
        - Similar system designs
        - Proven patterns
        - Common pitfalls
        - Best practices
        """

        # Use R2R's deep research agent
        research = await self.memory.deep_research(query)

        return research

    async def _design_architecture(
        self,
        task: Dict,
        analysis: Dict,
        research: Dict
    ) -> Dict:
        """
        Design the system architecture

        Creates:
        - Component design
        - Data flow diagrams
        - API contracts
        - Technology choices
        """
        prompt = f"""
        Design system architecture for:
        {task['title']}

        Analysis: {analysis['analysis']}

        Research findings: {research.get('answer', 'N/A')}

        Design:
        1. High-level architecture (components, layers)
        2. Component interactions and APIs
        3. Data models and storage
        4. Technology stack choices (with rationale)
        5. Scalability approach
        6. Security considerations
        7. Deployment strategy

        Provide detailed design with diagrams in Mermaid format.
        """

        design = await self.think(prompt)

        return {
            "design": design,
            "components": self._extract_components(design),
            "apis": self._extract_apis(design),
            "tech_stack": self._extract_tech_stack(design)
        }

    async def _decompose_tasks(self, architecture: Dict) -> List[Dict]:
        """
        Decompose architecture into implementable tasks

        Creates subtasks for:
        - Each component implementation
        - API development
        - Database setup
        - Testing
        - Documentation
        """
        prompt = f"""
        Decompose this architecture into implementation tasks:

        {architecture['design']}

        Create tasks for:
        1. Infrastructure setup
        2. Data model implementation
        3. Component implementation (one task per component)
        4. API implementation
        5. Integration work
        6. Testing
        7. Documentation

        For each task, specify:
        - Clear description
        - Acceptance criteria
        - Dependencies
        - Estimated complexity
        """

        decomposition = await self.think(prompt)

        tasks = self._parse_tasks(decomposition)

        # Store tasks in memory for developer agents to pick up
        for task in tasks:
            await self.memory.store_task(task)

            # Emit event
            await self.event_bus.emit({
                "type": "subtask_created",
                "task": task,
                "parent_task": architecture.get("task_id")
            })

        logger.info(f"Decomposed into {len(tasks)} subtasks")

        return tasks

    async def _assess_risks(self, architecture: Dict) -> Dict:
        """
        Assess architectural risks

        Evaluates:
        - Technical risks
        - Complexity risks
        - Integration risks
        - Scalability risks
        - Security risks
        """
        prompt = f"""
        Assess risks for this architecture:

        {architecture['design']}

        Identify:
        1. Technical risks (feasibility, complexity)
        2. Integration risks (with existing systems)
        3. Performance/scalability risks
        4. Security risks
        5. Operational risks
        6. Team/skills risks

        For each risk:
        - Severity (low/medium/high/critical)
        - Likelihood
        - Impact
        - Mitigation strategy
        """

        risk_analysis = await self.think(prompt)

        risks = self._parse_risks(risk_analysis)

        return risks

    async def _create_specification(
        self,
        architecture: Dict,
        subtasks: List[Dict],
        risks: Dict
    ) -> str:
        """
        Create comprehensive technical specification

        Markdown document with:
        - Architecture overview
        - Component details
        - API specifications
        - Implementation tasks
        - Risk assessment
        - Timeline estimate
        """
        spec = f"""
# Technical Specification

## Overview
{architecture['design']}

## Architecture

### Components
{self._format_components(architecture['components'])}

### APIs
{self._format_apis(architecture['apis'])}

### Technology Stack
{self._format_tech_stack(architecture['tech_stack'])}

## Implementation Plan

### Tasks
{self._format_tasks(subtasks)}

### Dependencies
```mermaid
graph TD
{self._generate_dependency_graph(subtasks)}
```

## Risk Assessment
{self._format_risks(risks)}

## Timeline Estimate
{self._estimate_timeline(subtasks)}

---
*Designed by Architect Agent `{self.agent_id}`*
"""

        return spec

    async def _store_architecture_decision(
        self,
        architecture: Dict,
        spec: str
    ):
        """
        Store architectural decision in memory

        Creates knowledge graph nodes for:
        - Architecture decision
        - Components
        - Technical choices
        - Rationale
        """
        await self.memory.store_architecture({
            "architecture": architecture,
            "specification": spec,
            "timestamp": datetime.now().isoformat(),
            "agent_id": self.agent_id
        })

        logger.info("Stored architectural decision in memory")

    def _extract_components(self, design: str) -> List[Dict]:
        """Extract components from design"""
        # Simplified extraction
        # In real implementation, would parse structured output
        return [
            {"name": "component1", "type": "service"},
            {"name": "component2", "type": "database"}
        ]

    def _extract_apis(self, design: str) -> List[Dict]:
        """Extract API definitions"""
        return [
            {"endpoint": "/api/v1/resource", "method": "GET"}
        ]

    def _extract_tech_stack(self, design: str) -> Dict:
        """Extract technology choices"""
        return {
            "backend": "Node.js",
            "database": "PostgreSQL",
            "frontend": "React"
        }

    def _parse_tasks(self, decomposition: str) -> List[Dict]:
        """Parse task list from AI output"""
        # Simplified parsing
        return [
            {
                "id": f"task_{i}",
                "title": f"Implementation task {i}",
                "type": "implementation",
                "complexity": 5.0
            }
            for i in range(5)
        ]

    def _parse_risks(self, risk_analysis: str) -> Dict:
        """Parse risks from analysis"""
        return {
            "high": [],
            "medium": [],
            "low": []
        }

    def _format_components(self, components: List[Dict]) -> str:
        """Format components for spec"""
        return "\n".join([
            f"- **{c['name']}** ({c['type']})"
            for c in components
        ])

    def _format_apis(self, apis: List[Dict]) -> str:
        """Format APIs for spec"""
        return "\n".join([
            f"- `{a['method']} {a['endpoint']}`"
            for a in apis
        ])

    def _format_tech_stack(self, stack: Dict) -> str:
        """Format tech stack for spec"""
        return "\n".join([
            f"- **{k.title()}**: {v}"
            for k, v in stack.items()
        ])

    def _format_tasks(self, tasks: List[Dict]) -> str:
        """Format tasks for spec"""
        return "\n".join([
            f"{i+1}. {task['title']} (complexity: {task['complexity']})"
            for i, task in enumerate(tasks)
        ])

    def _generate_dependency_graph(self, tasks: List[Dict]) -> str:
        """Generate Mermaid dependency graph"""
        # Simplified graph
        return "\n".join([
            f"Task{i} --> Task{i+1}"
            for i in range(len(tasks) - 1)
        ])

    def _format_risks(self, risks: Dict) -> str:
        """Format risks for spec"""
        sections = []

        for severity, risk_list in risks.items():
            if risk_list:
                sections.append(f"### {severity.title()} Risks\n")
                for risk in risk_list:
                    sections.append(f"- {risk}\n")

        return "\n".join(sections) if sections else "No significant risks identified."

    def _estimate_timeline(self, tasks: List[Dict]) -> str:
        """Estimate implementation timeline"""
        total_complexity = sum(t.get("complexity", 5.0) for t in tasks)
        days = int(total_complexity / 2)  # Rough estimate

        return f"Estimated: **{days} days** ({len(tasks)} tasks)"
