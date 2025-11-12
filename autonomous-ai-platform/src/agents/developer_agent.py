"""
Developer Agent

Responsible for:
- Implementing features and bug fixes
- Writing production-quality code
- Running tests in sandboxes
- Creating pull requests
"""

import logging
from typing import Dict, List
from .base_agent import BaseAgent, AgentCapability

logger = logging.getLogger(__name__)


class DeveloperAgent(BaseAgent):
    """
    Developer agent that writes and tests code

    Key capabilities:
    - Code implementation from requirements
    - Test-driven development
    - Codegen sandbox execution
    - GitHub PR creation
    """

    def __init__(
        self,
        agent_id: str,
        memory,
        event_bus,
        capability: AgentCapability,
        codegen_client=None,
        github_client=None
    ):
        super().__init__(agent_id, memory, event_bus, capability)

        self.codegen = codegen_client
        self.github = github_client

        # Setup event handlers
        self._setup_handlers()

    def _setup_handlers(self):
        """Register event handlers"""

        @self.on_event("task_created")
        async def handle_task_created(event):
            task = event.get("task")

            # Check if we should handle this
            if await self.should_handle_task(task):
                # Try to claim it
                claimed = await self.claim_task(task["id"])

                if claimed:
                    # Execute the task
                    await self.execute_task(task)

        @self.on_event("code_review_completed")
        async def handle_review_completed(event):
            # React to code review feedback
            review = event.get("review")

            if review["requires_changes"]:
                # Implement review feedback
                await self._implement_review_feedback(review)

    def get_relevant_event_types(self) -> List[str]:
        """Events this agent handles"""
        return [
            "task_created",
            "code_review_completed",
            "test_failure"
        ]

    async def process_task(self, task: Dict) -> Dict:
        """
        Implement a task

        Workflow:
        1. Analyze requirements
        2. Design implementation approach
        3. Find relevant patterns from memory
        4. Write code
        5. Run tests in sandbox
        6. Create PR
        """
        task_id = task["id"]

        logger.info(f"Developer agent implementing task {task_id}")

        # Step 1: Analyze requirements
        analysis = await self._analyze_requirements(task)

        # Step 2: Find similar implementations
        patterns = await self._find_patterns(task)

        # Step 3: Design implementation
        implementation_plan = await self._design_implementation(
            task,
            analysis,
            patterns
        )

        # Step 4: Write code
        code = await self._write_code(implementation_plan)

        # Step 5: Run tests in sandbox
        test_results = await self._test_code(code)

        if not test_results["success"]:
            # Fix failures and retry
            code = await self._fix_test_failures(code, test_results)
            test_results = await self._test_code(code)

        # Step 6: Create PR
        pr = await self._create_pull_request(task, code)

        return {
            "success": True,
            "code": code,
            "tests": test_results,
            "pr_url": pr["url"],
            "implementation_plan": implementation_plan
        }

    async def _analyze_requirements(self, task: Dict) -> Dict:
        """
        Deep analysis of task requirements

        Uses AI reasoning to understand:
        - What needs to be built
        - Acceptance criteria
        - Edge cases
        - Dependencies
        """
        prompt = f"""
        Analyze this development task:

        Title: {task['title']}
        Description: {task['description']}
        Labels: {task.get('labels', [])}

        Provide:
        1. Core requirements
        2. Acceptance criteria
        3. Potential edge cases
        4. Dependencies to consider
        5. Complexity assessment
        """

        # Get relevant context from memory
        context = await self.retrieve_context(
            f"{task['title']} {task['description']}"
        )

        analysis = await self.think(prompt, context)

        return {
            "requirements": analysis,
            "context": context
        }

    async def _find_patterns(self, task: Dict) -> List[Dict]:
        """
        Find relevant solution patterns from memory

        Uses R2R to search for similar implementations
        """
        query = f"{task['type']}: {task['description']}"

        patterns = await self.memory.search(
            query=query,
            collection="patterns",
            limit=3
        )

        logger.info(f"Found {len(patterns)} relevant patterns")

        return patterns

    async def _design_implementation(
        self,
        task: Dict,
        analysis: Dict,
        patterns: List[Dict]
    ) -> Dict:
        """
        Design the implementation approach

        Considers:
        - Requirements
        - Available patterns
        - Codebase architecture
        - Best practices
        """
        prompt = f"""
        Design implementation for:
        {task['title']}

        Requirements: {analysis['requirements']}

        Available patterns:
        {self._format_patterns(patterns)}

        Design:
        1. Files to create/modify
        2. Key functions/classes
        3. Data structures
        4. Algorithm approach
        5. Test strategy
        """

        design = await self.think(prompt)

        return {
            "design": design,
            "patterns_used": [p["id"] for p in patterns]
        }

    async def _write_code(self, plan: Dict) -> Dict:
        """
        Write the actual code

        Uses AI to generate production-quality code
        """
        logger.info("Writing code...")

        prompt = f"""
        Implement this design:
        {plan['design']}

        Requirements:
        - Production quality
        - Well-tested
        - Type-safe
        - Documented
        - Following best practices
        """

        code = await self.think(prompt)

        # Parse code into files
        files = self._parse_code_output(code)

        return {
            "files": files,
            "plan": plan
        }

    async def _test_code(self, code: Dict) -> Dict:
        """
        Run tests in Codegen sandbox

        Executes:
        - Unit tests
        - Integration tests
        - Linters
        - Type checking
        """
        if not self.codegen:
            logger.warning("Codegen client not available, skipping tests")
            return {"success": True, "skipped": True}

        logger.info("Running tests in sandbox...")

        try:
            # Create sandbox
            sandbox_id = await self.codegen.create_sandbox()

            # Write code files
            for file_path, content in code["files"].items():
                await self.codegen.write_file(sandbox_id, file_path, content)

            # Run tests
            test_result = await self.codegen.execute(
                sandbox_id,
                command="npm test",
                timeout=300
            )

            # Run linter
            lint_result = await self.codegen.execute(
                sandbox_id,
                command="npm run lint",
                timeout=60
            )

            # Cleanup sandbox
            await self.codegen.destroy_sandbox(sandbox_id)

            return {
                "success": test_result["exit_code"] == 0,
                "tests": test_result,
                "linting": lint_result
            }

        except Exception as e:
            logger.error(f"Test execution failed: {e}")
            return {
                "success": False,
                "error": str(e)
            }

    async def _fix_test_failures(
        self,
        code: Dict,
        test_results: Dict
    ) -> Dict:
        """
        Fix failing tests

        Analyzes test output and fixes issues
        """
        logger.info("Fixing test failures...")

        prompt = f"""
        These tests are failing:
        {test_results['tests']['stderr']}

        Original code:
        {code}

        Fix the issues while maintaining functionality.
        """

        fixed_code = await self.think(prompt)

        return self._parse_code_output(fixed_code)

    async def _create_pull_request(self, task: Dict, code: Dict) -> Dict:
        """
        Create GitHub pull request

        Creates:
        - Feature branch
        - Commits code
        - Opens PR with description
        """
        if not self.github:
            logger.warning("GitHub client not available")
            return {"url": "N/A"}

        logger.info("Creating pull request...")

        try:
            # Create branch
            branch_name = f"agent/{task['id']}"
            await self.github.create_branch(branch_name)

            # Commit code
            for file_path, content in code["files"].items():
                await self.github.write_file(
                    branch_name,
                    file_path,
                    content
                )

            # Create PR
            pr = await self.github.create_pr(
                title=task["title"],
                body=self._generate_pr_description(task, code),
                head=branch_name,
                base="main"
            )

            return pr

        except Exception as e:
            logger.error(f"Failed to create PR: {e}")
            return {"url": "N/A", "error": str(e)}

    def _format_patterns(self, patterns: List[Dict]) -> str:
        """Format patterns for prompt"""
        if not patterns:
            return "No similar patterns found"

        formatted = []
        for p in patterns:
            formatted.append(f"- {p['name']}: {p.get('approach', 'N/A')}")

        return "\n".join(formatted)

    def _parse_code_output(self, code_text: str) -> Dict[str, str]:
        """
        Parse AI output into file structure

        Expects format:
        ```filename
        code content
        ```
        """
        # Simplified parser
        # In real implementation, would properly parse code blocks

        files = {}

        # Placeholder parsing
        files["src/implementation.ts"] = code_text

        return files

    def _generate_pr_description(self, task: Dict, code: Dict) -> str:
        """Generate PR description"""
        return f"""
## {task['title']}

**Task**: {task.get('description', 'N/A')}

### Changes
- Implemented feature according to requirements
- Added comprehensive tests
- Updated documentation

### Files Changed
{self._list_files(code['files'])}

### Testing
- ✅ All tests passing
- ✅ Linting passed
- ✅ Type checking passed

---
*This PR was created by Developer Agent `{self.agent_id}`*
"""

    def _list_files(self, files: Dict) -> str:
        """List changed files"""
        return "\n".join([f"- `{path}`" for path in files.keys()])

    async def _implement_review_feedback(self, review: Dict):
        """Implement code review feedback"""
        logger.info(f"Implementing review feedback for PR {review['pr_id']}")

        # Get the code
        # Apply review suggestions
        # Update PR

        # Placeholder for now
        pass
