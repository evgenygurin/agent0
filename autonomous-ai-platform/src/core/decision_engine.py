"""
Decision Engine for Autonomous Platform

Handles multi-factor decision making including:
- Risk assessment for deployments
- Confidence calibration
- Escalation rules
- Auto-deployment decisions
"""

import logging
import math
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class DecisionType(Enum):
    """Types of decisions the engine handles"""
    AUTO_PROCEED = "auto_proceed"
    PROCEED_WITH_MONITORING = "proceed_with_monitoring"
    REQUEST_REVIEW = "request_review"
    BLOCK = "block"
    ESCALATE = "escalate"


@dataclass
class RiskScore:
    """Multi-dimensional risk assessment"""
    overall: float  # 0.0 to 1.0
    complexity: float
    test_coverage: float
    dependency_risk: float
    historical_stability: float
    impact_radius: float
    breakdown: Dict[str, float]
    recommendation: DecisionType


@dataclass
class DecisionContext:
    """Context for making decisions"""
    task_id: str
    pr_id: Optional[str] = None
    code_changes: Dict = None
    test_results: Dict = None
    review_comments: List = None
    is_critical: bool = False
    requires_breaking_changes: bool = False
    affected_files: List[str] = None
    metadata: Dict = None


@dataclass
class ConfidenceScore:
    """Calibrated confidence score"""
    raw_confidence: float
    calibrated_confidence: float
    historical_accuracy: float
    sample_size: int
    factors: Dict[str, float]


class DecisionEngine:
    """
    Multi-factor decision engine with learning-based calibration

    This engine:
    1. Assesses risk across multiple dimensions
    2. Calibrates confidence based on historical outcomes
    3. Makes deployment decisions
    4. Determines when to escalate to humans
    """

    def __init__(self, memory, config: Dict):
        """
        Initialize decision engine

        Args:
            memory: R2R memory system for storing decisions
            config: Configuration including thresholds
        """
        self.memory = memory
        self.config = config

        # Thresholds from config
        self.auto_deploy_threshold = config.get("auto_deploy_threshold", 0.8)
        self.risk_threshold_high = config.get("risk_threshold", 0.5)
        self.risk_threshold_critical = 0.8

        # Confidence calibration buckets
        self.confidence_buckets = {}

        # Decision history for learning
        self.decision_history = []

        logger.info("Decision Engine initialized")

    async def make_deployment_decision(
        self,
        context: DecisionContext
    ) -> DecisionType:
        """
        Make a deployment decision based on multi-factor analysis

        Args:
            context: Decision context with all relevant information

        Returns:
            Decision type (auto proceed, review, block, etc.)
        """
        logger.info(f"Making deployment decision for task {context.task_id}")

        # Critical tasks always require review
        if context.is_critical:
            logger.info("Critical task - requiring human review")
            return DecisionType.REQUEST_REVIEW

        # Assess risk across multiple dimensions
        risk_score = await self.assess_risk(context)

        # Get calibrated confidence from agents
        confidence = await self.get_calibrated_confidence(context)

        # Apply decision rules
        decision = self._apply_decision_rules(
            risk_score,
            confidence,
            context
        )

        # Store decision for learning
        await self._store_decision(context, risk_score, confidence, decision)

        logger.info(
            f"Decision for {context.task_id}: {decision.value} "
            f"(risk: {risk_score.overall:.2f}, confidence: {confidence.calibrated_confidence:.2f})"
        )

        return decision

    async def assess_risk(self, context: DecisionContext) -> RiskScore:
        """
        Comprehensive risk assessment

        Evaluates:
        1. Code complexity
        2. Test coverage
        3. Dependency changes
        4. Historical stability
        5. Impact radius (blast radius)
        """
        # Calculate individual risk factors
        complexity_risk = await self._assess_complexity_risk(context)
        coverage_risk = await self._assess_test_coverage_risk(context)
        dependency_risk = await self._assess_dependency_risk(context)
        stability_risk = await self._assess_historical_stability_risk(context)
        impact_risk = await self._assess_impact_radius_risk(context)

        # Weighted combination
        weights = {
            "complexity": 0.2,
            "coverage": 0.3,
            "dependencies": 0.2,
            "stability": 0.15,
            "impact": 0.15
        }

        overall_risk = (
            complexity_risk * weights["complexity"] +
            coverage_risk * weights["coverage"] +
            dependency_risk * weights["dependencies"] +
            stability_risk * weights["stability"] +
            impact_risk * weights["impact"]
        )

        # Create risk score object
        risk_score = RiskScore(
            overall=overall_risk,
            complexity=complexity_risk,
            test_coverage=coverage_risk,
            dependency_risk=dependency_risk,
            historical_stability=stability_risk,
            impact_radius=impact_risk,
            breakdown={
                "complexity": complexity_risk,
                "coverage": coverage_risk,
                "dependencies": dependency_risk,
                "stability": stability_risk,
                "impact": impact_risk
            },
            recommendation=self._risk_to_decision(overall_risk)
        )

        return risk_score

    async def _assess_complexity_risk(self, context: DecisionContext) -> float:
        """
        Assess risk based on code complexity

        Uses cyclomatic complexity, lines changed, etc.
        """
        if not context.code_changes:
            return 0.0

        total_complexity = 0.0
        num_files = 0

        for file_path, changes in context.code_changes.items():
            # Calculate complexity from AST
            complexity = changes.get("cyclomatic_complexity", 1)

            # More lines = more risk
            lines_changed = changes.get("lines_changed", 0)

            # Normalize complexity (cap at 20)
            normalized_complexity = min(complexity / 20.0, 1.0)

            # Normalize lines (cap at 500)
            normalized_lines = min(lines_changed / 500.0, 1.0)

            file_risk = (normalized_complexity + normalized_lines) / 2
            total_complexity += file_risk
            num_files += 1

        if num_files == 0:
            return 0.0

        return total_complexity / num_files

    async def _assess_test_coverage_risk(self, context: DecisionContext) -> float:
        """
        Assess risk based on test coverage

        Lower coverage = higher risk
        """
        if not context.test_results:
            return 1.0  # No tests = maximum risk

        coverage = context.test_results.get("coverage_percent", 0)

        # Invert coverage (0% coverage = 1.0 risk, 100% coverage = 0.0 risk)
        # With some minimum risk even at 100% coverage
        risk = max(0.1, 1.0 - (coverage / 100.0))

        return risk

    async def _assess_dependency_risk(self, context: DecisionContext) -> float:
        """
        Assess risk from dependency changes

        Uses R2R knowledge graph to check dependency updates
        """
        if not context.code_changes:
            return 0.0

        dependency_changes = 0
        breaking_changes = 0

        for file_path, changes in context.code_changes.items():
            if "dependencies" in changes:
                dependency_changes += len(changes["dependencies"].get("added", []))
                dependency_changes += len(changes["dependencies"].get("updated", []))
                breaking_changes += len(changes["dependencies"].get("breaking", []))

        # Risk increases with number of changes
        base_risk = min(dependency_changes / 10.0, 0.8)

        # Breaking changes add significant risk
        breaking_risk = min(breaking_changes * 0.3, 1.0)

        return min(base_risk + breaking_risk, 1.0)

    async def _assess_historical_stability_risk(
        self,
        context: DecisionContext
    ) -> float:
        """
        Assess risk based on historical stability of affected files

        Uses R2R memory to query past incidents
        """
        if not context.affected_files:
            return 0.3  # Moderate default risk

        try:
            # Query R2R for historical issues with these files
            incidents = await self.memory.search(
                query=f"incidents in files: {', '.join(context.affected_files[:5])}",
                collection="incidents",
                limit=20
            )

            if not incidents:
                return 0.1  # No history = low risk

            # Calculate incident rate
            recent_incidents = [
                inc for inc in incidents
                if self._is_recent(inc.get("timestamp"), days=90)
            ]

            incident_rate = len(recent_incidents) / len(incidents)

            # More recent incidents = higher risk
            return min(incident_rate * 1.5, 1.0)

        except Exception as e:
            logger.warning(f"Failed to assess historical stability: {e}")
            return 0.3

    async def _assess_impact_radius_risk(self, context: DecisionContext) -> float:
        """
        Assess risk based on impact radius (blast radius)

        Uses R2R GraphRAG to find all affected components
        """
        if not context.affected_files:
            return 0.0

        try:
            # Use knowledge graph to find dependencies
            affected_components = []

            for file_path in context.affected_files[:10]:  # Limit to 10 files
                # Query graph for dependents
                dependents = await self.memory.find_dependent_files(
                    file_path,
                    max_depth=3
                )
                affected_components.extend(dependents)

            # More affected components = higher risk
            unique_components = len(set(affected_components))

            # Normalize (cap at 50 components)
            risk = min(unique_components / 50.0, 1.0)

            return risk

        except Exception as e:
            logger.warning(f"Failed to assess impact radius: {e}")
            return 0.3

    def _is_recent(self, timestamp: str, days: int) -> bool:
        """Check if timestamp is within last N days"""
        try:
            ts = datetime.fromisoformat(timestamp)
            return (datetime.now() - ts) < timedelta(days=days)
        except:
            return False

    async def get_calibrated_confidence(
        self,
        context: DecisionContext
    ) -> ConfidenceScore:
        """
        Get calibrated confidence score from agents

        Calibration is based on historical accuracy
        """
        # Get raw confidence from agents (would be from actual agents)
        raw_confidence = await self._get_agent_confidence(context)

        # Get historical accuracy for this confidence bucket
        bucket = int(raw_confidence * 10) / 10  # Round to 0.1
        historical_data = self.confidence_buckets.get(bucket, [])

        if len(historical_data) < 10:
            # Not enough data - be conservative
            calibrated = raw_confidence * 0.8
            historical_accuracy = 0.5
            sample_size = len(historical_data)
        else:
            # Calibrate based on historical outcomes
            actual_success_rate = sum(historical_data) / len(historical_data)
            calibrated = actual_success_rate
            historical_accuracy = actual_success_rate
            sample_size = len(historical_data)

        return ConfidenceScore(
            raw_confidence=raw_confidence,
            calibrated_confidence=calibrated,
            historical_accuracy=historical_accuracy,
            sample_size=sample_size,
            factors={
                "agent_confidence": raw_confidence,
                "historical_calibration": historical_accuracy,
                "sample_size_penalty": min(sample_size / 100.0, 1.0)
            }
        )

    async def _get_agent_confidence(self, context: DecisionContext) -> float:
        """Get raw confidence from agent assessments"""
        # This would query actual agents
        # For now, return a reasonable default
        confidence_factors = []

        if context.test_results:
            test_success = context.test_results.get("success", False)
            confidence_factors.append(0.9 if test_success else 0.3)

        if context.review_comments:
            # Fewer review concerns = higher confidence
            num_concerns = len([
                c for c in context.review_comments
                if c.get("severity") in ["high", "critical"]
            ])
            review_confidence = max(0.3, 1.0 - (num_concerns * 0.2))
            confidence_factors.append(review_confidence)

        if confidence_factors:
            return sum(confidence_factors) / len(confidence_factors)

        return 0.5  # Neutral default

    def _apply_decision_rules(
        self,
        risk_score: RiskScore,
        confidence: ConfidenceScore,
        context: DecisionContext
    ) -> DecisionType:
        """
        Apply decision rules based on risk and confidence

        Decision Matrix:
        - Low risk + high confidence = AUTO_PROCEED
        - Medium risk + high confidence = PROCEED_WITH_MONITORING
        - High risk or low confidence = REQUEST_REVIEW
        - Critical risk = BLOCK
        """
        risk = risk_score.overall
        conf = confidence.calibrated_confidence

        # Critical risk - always block
        if risk > self.risk_threshold_critical:
            return DecisionType.BLOCK

        # High risk - request review
        if risk > self.risk_threshold_high:
            return DecisionType.REQUEST_REVIEW

        # Medium risk with high confidence - proceed with monitoring
        if risk > 0.3 and conf > 0.8:
            return DecisionType.PROCEED_WITH_MONITORING

        # Low risk with high confidence - auto proceed
        if risk < 0.3 and conf > self.auto_deploy_threshold:
            return DecisionType.AUTO_PROCEED

        # Default - request review
        return DecisionType.REQUEST_REVIEW

    def _risk_to_decision(self, risk: float) -> DecisionType:
        """Convert risk score to recommended decision"""
        if risk < 0.2:
            return DecisionType.AUTO_PROCEED
        elif risk < 0.5:
            return DecisionType.PROCEED_WITH_MONITORING
        elif risk < 0.8:
            return DecisionType.REQUEST_REVIEW
        else:
            return DecisionType.BLOCK

    async def _store_decision(
        self,
        context: DecisionContext,
        risk_score: RiskScore,
        confidence: ConfidenceScore,
        decision: DecisionType
    ):
        """Store decision in memory for learning"""
        decision_record = {
            "task_id": context.task_id,
            "pr_id": context.pr_id,
            "timestamp": datetime.now().isoformat(),
            "risk_score": risk_score.overall,
            "risk_breakdown": risk_score.breakdown,
            "raw_confidence": confidence.raw_confidence,
            "calibrated_confidence": confidence.calibrated_confidence,
            "decision": decision.value,
            "metadata": context.metadata
        }

        # Store in R2R
        await self.memory.store_decision(decision_record)

        # Add to local history
        self.decision_history.append(decision_record)

    async def record_outcome(
        self,
        task_id: str,
        success: bool,
        metrics: Dict = None
    ):
        """
        Record decision outcome for learning

        This updates confidence calibration
        """
        logger.info(
            f"Recording outcome for {task_id}: "
            f"{'success' if success else 'failure'}"
        )

        try:
            # Find original decision
            decision = next(
                (d for d in self.decision_history if d["task_id"] == task_id),
                None
            )

            if not decision:
                logger.warning(f"No decision found for task {task_id}")
                return

            # Update confidence bucket
            raw_conf = decision["raw_confidence"]
            bucket = int(raw_conf * 10) / 10

            if bucket not in self.confidence_buckets:
                self.confidence_buckets[bucket] = []

            self.confidence_buckets[bucket].append(1.0 if success else 0.0)

            # Store outcome in R2R for analysis
            await self.memory.store_outcome({
                "task_id": task_id,
                "decision": decision,
                "success": success,
                "metrics": metrics,
                "timestamp": datetime.now().isoformat()
            })

            logger.info(
                f"Confidence bucket {bucket} now has "
                f"{len(self.confidence_buckets[bucket])} samples"
            )

        except Exception as e:
            logger.error(f"Failed to record outcome: {e}")

    async def should_escalate(self, context: DecisionContext) -> bool:
        """
        Determine if a situation requires human escalation

        Escalation rules:
        - Security vulnerabilities
        - Breaking API changes
        - Novel situations (no precedents)
        - Uncertainty (low confidence)
        """
        # Check escalation conditions
        escalation_reasons = []

        # Security implications
        if context.metadata and context.metadata.get("security_sensitive"):
            escalation_reasons.append("security_sensitive")

        # Breaking changes
        if context.requires_breaking_changes:
            escalation_reasons.append("breaking_changes")

        # Check for precedents in memory
        precedents = await self._find_precedents(context)
        if len(precedents) == 0:
            escalation_reasons.append("no_precedents")

        # Low confidence
        confidence = await self.get_calibrated_confidence(context)
        if confidence.calibrated_confidence < 0.6:
            escalation_reasons.append("low_confidence")

        if escalation_reasons:
            logger.info(
                f"Escalation recommended for {context.task_id}: "
                f"{', '.join(escalation_reasons)}"
            )
            return True

        return False

    async def _find_precedents(self, context: DecisionContext) -> List[Dict]:
        """Find similar past decisions from memory"""
        try:
            query = f"Similar to: {context.task_id}"
            if context.metadata:
                query += f" {context.metadata.get('description', '')}"

            results = await self.memory.search(
                query=query,
                collection="decisions",
                limit=5
            )

            return results

        except Exception as e:
            logger.warning(f"Failed to find precedents: {e}")
            return []
