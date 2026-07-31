"""
Risk classification rules.
"""

from domain.enums import (
    SensorType,
    RiskLevel,
)

from domain.models import (
    ThresholdRule,
)

WATER_LEVEL_RULES = [

    ThresholdRule(
        minimum=0,
        maximum=1,
        risk_level=RiskLevel.SAFE,
        alert_message="Normal conditions.",
        prediction_horizon="No immediate risk.",
        recommended_action="Continue monitoring.",
    ),

    ThresholdRule(
        minimum=1,
        maximum=2,
        risk_level=RiskLevel.ATTENTION,
        alert_message="River level increasing.",
        prediction_horizon="Next 6 hours",
        recommended_action="Increase monitoring frequency.",
    ),

    ThresholdRule(
        minimum=2,
        maximum=3,
        risk_level=RiskLevel.ALERT,
        alert_message="Flood risk detected. Prepare response.",
        prediction_horizon="Next 2 hours",
        recommended_action="Notify local authorities and prepare response teams.",
    ),

    ThresholdRule(
        minimum=3,
        maximum=float("inf"),
        risk_level=RiskLevel.CRITICAL,
        alert_message="Critical flood risk. Immediate action required.",
        prediction_horizon="Next 30 minutes",
        recommended_action="Issue emergency warning and evacuate vulnerable areas.",
    ),
]

RISK_RULES = {

    SensorType.WATER_LEVEL:
        WATER_LEVEL_RULES,
}