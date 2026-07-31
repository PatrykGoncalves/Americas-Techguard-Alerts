"""
Risk classification engine.
"""

from infrastructure.interfaces import BaseRiskEngine
from infrastructure.risk_config import RISK_RULES

from domain.exceptions import RiskEngineError
from domain.models import EnvironmentalPayload


class RiskEngine(BaseRiskEngine):

    def evaluate(
        self,
        payload: EnvironmentalPayload,
    ) -> None:

        rules = RISK_RULES.get(
            payload.sensor_type
        )

        if rules is None:

            raise RiskEngineError(
                f"No rules defined for "
                f"{payload.sensor_type.value}"
            )

        for rule in rules:

            if rule.matches(payload.value):
                payload.update_risk(

                    level=rule.risk_level,
                    message=rule.alert_message,
                    prediction_horizon=rule.prediction_horizon,
                    recommended_action=rule.recommended_action,

                )

                return

        raise RiskEngineError(
            "Unable to classify payload."
        )