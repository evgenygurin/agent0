"""
Learning System for Continuous Improvement

Implements multiple learning mechanisms:
1. Pattern extraction from successful solutions
2. Reinforcement learning from deployment outcomes
3. Meta-learning to optimize learning process itself
4. Transfer learning across projects
"""

import logging
import numpy as np
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
from collections import defaultdict
import json

logger = logging.getLogger(__name__)


@dataclass
class Pattern:
    """Represents a learned solution pattern"""
    id: str
    name: str
    task_type: str
    approach: str
    code_structure: Dict
    dependencies: List[str]
    test_strategy: Dict
    success_rate: float
    usage_count: int
    created_at: datetime
    last_used: datetime
    applicability_conditions: Dict


@dataclass
class LearningExample:
    """Training example from real outcomes"""
    task_id: str
    decision: Dict
    code_changes: Dict
    outcome: Dict
    reward: float
    timestamp: datetime


class LearningSystem:
    """
    Continuous learning system that improves platform performance

    Key capabilities:
    1. Extract reusable patterns from successes
    2. Learn from failures
    3. Optimize decision-making parameters
    4. Transfer knowledge between projects
    """

    def __init__(self, memory, metrics_store: Dict):
        """
        Initialize learning system

        Args:
            memory: R2R memory system
            metrics_store: Reference to platform metrics
        """
        self.memory = memory
        self.metrics = metrics_store

        # Pattern library
        self.patterns = {}

        # Learning examples
        self.learning_examples = []

        # Hyperparameters (can be tuned)
        self.learning_rate = 0.01
        self.pattern_threshold = 0.7
        self.memory_decay_rate = 0.05

        # Performance tracking
        self.performance_history = []

        logger.info("Learning System initialized")

    async def learn_from_success(
        self,
        task_id: str,
        implementation: Dict,
        metrics: Dict
    ):
        """
        Extract patterns from successful implementations

        Args:
            task_id: Task identifier
            implementation: Implementation details (code, tests, etc.)
            metrics: Success metrics (quality score, time, etc.)
        """
        logger.info(f"Learning from successful task: {task_id}")

        try:
            # Only learn from high-quality solutions
            quality_score = metrics.get("quality_score", 0)

            if quality_score < self.pattern_threshold:
                logger.debug(
                    f"Quality score {quality_score} below threshold "
                    f"{self.pattern_threshold}, skipping pattern extraction"
                )
                return

            # Extract pattern from implementation
            pattern = await self._extract_pattern(task_id, implementation, metrics)

            if pattern:
                # Check if similar pattern exists
                similar = await self._find_similar_pattern(pattern)

                if similar:
                    # Merge with existing pattern
                    await self._merge_patterns(similar, pattern)
                else:
                    # Store as new pattern
                    self.patterns[pattern.id] = pattern
                    await self.memory.store_pattern(pattern.__dict__)

                logger.info(f"Pattern extracted: {pattern.name}")

        except Exception as e:
            logger.error(f"Failed to learn from success: {e}")

    async def learn_from_failure(
        self,
        task_id: str,
        error_details: Dict,
        context: Dict
    ):
        """
        Learn from failures to avoid repeating mistakes

        Args:
            task_id: Task identifier
            error_details: What went wrong
            context: Context of the failure
        """
        logger.info(f"Learning from failure: {task_id}")

        try:
            # Create anti-pattern to avoid
            anti_pattern = {
                "task_id": task_id,
                "error_type": error_details.get("type"),
                "error_message": error_details.get("message"),
                "context": context,
                "timestamp": datetime.now().isoformat(),
                "avoid": True
            }

            # Store in memory
            await self.memory.store_anti_pattern(anti_pattern)

            # Adjust decision-making if applicable
            if "decision_factors" in context:
                await self._adjust_decision_weights(
                    context["decision_factors"],
                    success=False
                )

        except Exception as e:
            logger.error(f"Failed to learn from failure: {e}")

    async def learn_from_deployment(
        self,
        deployment_id: str,
        outcome: Dict
    ):
        """
        Reinforcement learning from deployment outcomes

        Args:
            deployment_id: Deployment identifier
            outcome: Deployment outcome (success, metrics, incidents)
        """
        logger.info(f"Learning from deployment: {deployment_id}")

        try:
            # Get original decision
            decision = await self.memory.get_decision(deployment_id)

            if not decision:
                logger.warning(f"No decision found for {deployment_id}")
                return

            # Calculate reward signal
            reward = self._calculate_reward(outcome)

            # Create learning example
            example = LearningExample(
                task_id=deployment_id,
                decision=decision,
                code_changes=outcome.get("code_changes", {}),
                outcome=outcome,
                reward=reward,
                timestamp=datetime.now()
            )

            self.learning_examples.append(example)

            # Update decision model (simplified Q-learning)
            await self._update_decision_model(example)

            # Store for future analysis
            await self.memory.store_learning_example(example.__dict__)

            # Update metrics
            self.metrics["learning_iterations"] += 1

            logger.info(f"Learned from deployment {deployment_id}, reward: {reward:.2f}")

        except Exception as e:
            logger.error(f"Failed to learn from deployment: {e}")

    def _calculate_reward(self, outcome: Dict) -> float:
        """
        Calculate reward signal from deployment outcome

        Reward function combining multiple signals:
        - Tests passed: +1.0
        - Production healthy: +2.0
        - Performance improved: +0.3
        - Bugs found: -0.5 each
        - Rollback: -1.0
        - Review iterations: -0.2 each
        """
        reward = 0.0

        # Positive rewards
        if outcome.get("tests_passed"):
            reward += 1.0

        if outcome.get("production_healthy"):
            reward += 2.0

        if outcome.get("performance_improved"):
            reward += 0.3

        if outcome.get("review_approved"):
            reward += 0.5

        # Negative rewards
        bugs_found = outcome.get("bugs_found", 0)
        reward -= 0.5 * bugs_found

        if outcome.get("rolled_back"):
            reward -= 1.0

        review_iterations = outcome.get("review_iterations", 0)
        reward -= 0.2 * review_iterations

        incidents = outcome.get("incidents", 0)
        reward -= 1.0 * incidents

        return reward

    async def _update_decision_model(self, example: LearningExample):
        """
        Update decision-making model based on outcome

        Simplified Q-learning update
        """
        # Extract features from decision
        features = self._extract_decision_features(example.decision)

        # Update feature weights based on reward
        for feature_name, feature_value in features.items():
            # Simple gradient update
            adjustment = self.learning_rate * example.reward * feature_value

            # Store adjusted weights (would update actual model)
            logger.debug(
                f"Feature '{feature_name}' adjustment: {adjustment:.4f}"
            )

    def _extract_decision_features(self, decision: Dict) -> Dict[str, float]:
        """Extract features from a decision"""
        return {
            "risk_score": decision.get("risk_score", 0.5),
            "confidence": decision.get("calibrated_confidence", 0.5),
            "test_coverage": decision.get("test_coverage", 0.5),
            "complexity": decision.get("complexity", 0.5)
        }

    async def _extract_pattern(
        self,
        task_id: str,
        implementation: Dict,
        metrics: Dict
    ) -> Optional[Pattern]:
        """
        Extract reusable pattern from implementation

        Analyzes:
        - Code structure (AST patterns)
        - Dependencies used
        - Test strategies
        - Success metrics
        """
        try:
            # Analyze code structure
            code_structure = self._analyze_code_structure(
                implementation.get("code", {})
            )

            # Extract dependencies
            dependencies = implementation.get("dependencies", [])

            # Analyze test strategy
            test_strategy = self._analyze_test_strategy(
                implementation.get("tests", {})
            )

            # Determine applicability conditions
            applicability = self._determine_applicability(
                implementation,
                metrics
            )

            # Create pattern
            pattern = Pattern(
                id=f"pattern_{task_id}",
                name=self._generate_pattern_name(code_structure),
                task_type=implementation.get("task_type", "general"),
                approach=code_structure.get("approach", "unknown"),
                code_structure=code_structure,
                dependencies=dependencies,
                test_strategy=test_strategy,
                success_rate=1.0,  # Initial success
                usage_count=0,
                created_at=datetime.now(),
                last_used=datetime.now(),
                applicability_conditions=applicability
            )

            return pattern

        except Exception as e:
            logger.error(f"Failed to extract pattern: {e}")
            return None

    def _analyze_code_structure(self, code: Dict) -> Dict:
        """Analyze code to extract structural patterns"""
        # Simplified AST analysis
        structure = {
            "approach": "unknown",
            "patterns": [],
            "complexity": 0
        }

        # In a real system, would parse AST and extract patterns
        # e.g., design patterns, architectural patterns, etc.

        return structure

    def _analyze_test_strategy(self, tests: Dict) -> Dict:
        """Extract test strategy patterns"""
        return {
            "test_types": tests.get("types", []),
            "coverage": tests.get("coverage", 0),
            "assertions_per_test": tests.get("avg_assertions", 0)
        }

    def _determine_applicability(
        self,
        implementation: Dict,
        metrics: Dict
    ) -> Dict:
        """Determine when this pattern is applicable"""
        return {
            "task_types": [implementation.get("task_type")],
            "min_quality_threshold": metrics.get("quality_score", 0.7),
            "complexity_range": [0, 10]
        }

    def _generate_pattern_name(self, code_structure: Dict) -> str:
        """Generate descriptive pattern name"""
        approach = code_structure.get("approach", "general")
        return f"{approach}_pattern"

    async def _find_similar_pattern(self, pattern: Pattern) -> Optional[Pattern]:
        """Find existing similar pattern"""
        # Use R2R to find semantically similar patterns
        try:
            results = await self.memory.search(
                query=json.dumps(pattern.code_structure),
                collection="patterns",
                limit=1
            )

            if results and results[0].get("similarity", 0) > 0.85:
                # Found similar pattern
                pattern_id = results[0]["id"]
                return self.patterns.get(pattern_id)

        except Exception as e:
            logger.warning(f"Failed to search for similar patterns: {e}")

        return None

    async def _merge_patterns(self, existing: Pattern, new: Pattern):
        """Merge new pattern with existing pattern"""
        # Update success rate
        total_uses = existing.usage_count + 1
        existing.success_rate = (
            (existing.success_rate * existing.usage_count + 1.0) / total_uses
        )
        existing.usage_count = total_uses
        existing.last_used = datetime.now()

        # Update in memory
        await self.memory.store_pattern(existing.__dict__)

        logger.info(
            f"Merged pattern {existing.name}: "
            f"success_rate={existing.success_rate:.2f}, "
            f"usage_count={existing.usage_count}"
        )

    async def _adjust_decision_weights(
        self,
        factors: Dict[str, float],
        success: bool
    ):
        """Adjust decision-making weights based on outcome"""
        adjustment = self.learning_rate if success else -self.learning_rate

        for factor_name, factor_value in factors.items():
            # Simple weight adjustment
            logger.debug(
                f"Adjusting {factor_name} by {adjustment * factor_value:.4f}"
            )

    async def evolve_patterns(self):
        """
        Periodic pattern evolution

        - Promote successful patterns
        - Deprecate failing patterns
        - Merge similar patterns
        """
        logger.info("Evolving patterns...")

        try:
            # Get all patterns with recent usage data
            for pattern_id, pattern in list(self.patterns.items()):
                # Promote highly successful patterns
                if pattern.success_rate > 0.85 and pattern.usage_count > 10:
                    logger.info(f"Promoting pattern {pattern.name}")
                    # Could increase pattern's weight in recommendations

                # Deprecate failing patterns
                elif pattern.success_rate < 0.4 and pattern.usage_count > 5:
                    logger.info(f"Deprecating pattern {pattern.name}")
                    del self.patterns[pattern_id]
                    await self.memory.deprecate_pattern(pattern_id)

                # Apply memory decay to unused patterns
                days_since_use = (datetime.now() - pattern.last_used).days
                if days_since_use > 90:
                    pattern.success_rate *= (1.0 - self.memory_decay_rate)
                    logger.debug(
                        f"Applied decay to {pattern.name}: "
                        f"success_rate={pattern.success_rate:.2f}"
                    )

        except Exception as e:
            logger.error(f"Failed to evolve patterns: {e}")

    async def optimize_hyperparameters(self):
        """
        Meta-learning: optimize learning system's own parameters

        Uses Bayesian optimization to find optimal:
        - Learning rate
        - Pattern threshold
        - Memory decay rate
        """
        logger.info("Optimizing learning hyperparameters...")

        try:
            # Get recent performance history
            recent_performance = self.performance_history[-100:]

            if len(recent_performance) < 50:
                logger.info("Not enough data for hyperparameter optimization")
                return

            # Calculate baseline performance
            baseline = np.mean([p["score"] for p in recent_performance[:50]])

            # Try different parameter combinations
            candidate_params = [
                {"learning_rate": 0.005, "pattern_threshold": 0.75},
                {"learning_rate": 0.01, "pattern_threshold": 0.70},
                {"learning_rate": 0.02, "pattern_threshold": 0.80},
            ]

            best_params = None
            best_score = baseline

            for params in candidate_params:
                # Simulate performance with these params
                score = await self._evaluate_params(params, recent_performance)

                if score > best_score:
                    best_score = score
                    best_params = params

            # Apply best parameters
            if best_params:
                self.learning_rate = best_params["learning_rate"]
                self.pattern_threshold = best_params["pattern_threshold"]

                logger.info(
                    f"Updated hyperparameters: "
                    f"learning_rate={self.learning_rate}, "
                    f"pattern_threshold={self.pattern_threshold}"
                )

        except Exception as e:
            logger.error(f"Failed to optimize hyperparameters: {e}")

    async def _evaluate_params(
        self,
        params: Dict,
        history: List[Dict]
    ) -> float:
        """Evaluate performance with given parameters"""
        # Simplified backtest
        # In real system, would replay decisions with new params

        return np.random.random()  # Placeholder

    async def track_performance(self, metrics: Dict):
        """Track learning system performance over time"""
        performance_snapshot = {
            "timestamp": datetime.now().isoformat(),
            "metrics": metrics,
            "score": self._calculate_performance_score(metrics)
        }

        self.performance_history.append(performance_snapshot)

        # Keep last 1000 snapshots
        if len(self.performance_history) > 1000:
            self.performance_history = self.performance_history[-1000:]

    def _calculate_performance_score(self, metrics: Dict) -> float:
        """Calculate overall performance score"""
        # Weighted combination of metrics
        score = 0.0

        score += metrics.get("tasks_completed", 0) * 0.3
        score += metrics.get("deployment_success_rate", 0) * 0.4
        score += metrics.get("code_quality", 0) * 0.3

        return score

    async def get_pattern_recommendations(
        self,
        task_description: str,
        task_type: str
    ) -> List[Pattern]:
        """
        Get recommended patterns for a task

        Uses R2R semantic search to find applicable patterns
        """
        try:
            # Search for relevant patterns
            results = await self.memory.search(
                query=f"{task_type}: {task_description}",
                collection="patterns",
                limit=5
            )

            # Get pattern objects
            patterns = []
            for result in results:
                pattern_id = result.get("id")
                if pattern_id in self.patterns:
                    patterns.append(self.patterns[pattern_id])

            # Sort by success rate
            patterns.sort(key=lambda p: p.success_rate, reverse=True)

            return patterns

        except Exception as e:
            logger.error(f"Failed to get pattern recommendations: {e}")
            return []

    async def transfer_learning(
        self,
        source_project: str,
        target_project: str
    ):
        """
        Transfer learned patterns from one project to another

        Enables learning across different codebases
        """
        logger.info(
            f"Transferring learning from {source_project} to {target_project}"
        )

        try:
            # Get patterns from source project
            source_patterns = await self.memory.search(
                query=f"project:{source_project}",
                collection="patterns",
                limit=50
            )

            # Analyze applicability to target project
            applicable_patterns = []

            for pattern_data in source_patterns:
                pattern = Pattern(**pattern_data)

                # Check if pattern is generally applicable
                if self._is_transferable(pattern):
                    applicable_patterns.append(pattern)

            logger.info(
                f"Found {len(applicable_patterns)} transferable patterns"
            )

            # Apply patterns to target project
            for pattern in applicable_patterns:
                # Clone pattern for new project
                new_pattern = Pattern(
                    id=f"{pattern.id}_transferred_{target_project}",
                    name=pattern.name,
                    task_type=pattern.task_type,
                    approach=pattern.approach,
                    code_structure=pattern.code_structure,
                    dependencies=pattern.dependencies,
                    test_strategy=pattern.test_strategy,
                    success_rate=pattern.success_rate * 0.8,  # Discount
                    usage_count=0,
                    created_at=datetime.now(),
                    last_used=datetime.now(),
                    applicability_conditions=pattern.applicability_conditions
                )

                self.patterns[new_pattern.id] = new_pattern
                await self.memory.store_pattern(new_pattern.__dict__)

        except Exception as e:
            logger.error(f"Failed to transfer learning: {e}")

    def _is_transferable(self, pattern: Pattern) -> bool:
        """Determine if a pattern can be transferred to another project"""
        # Patterns with high success rate and usage are more transferable
        return (
            pattern.success_rate > 0.75 and
            pattern.usage_count > 5 and
            pattern.task_type in ["implementation", "testing", "refactor"]
        )
