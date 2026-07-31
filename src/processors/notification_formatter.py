from domain.models import EnvironmentalPayload


class NotificationFormatter:
    """
    Formats environmental alerts for mobile devices.
    """

    @staticmethod
    def format(
        payload: EnvironmentalPayload,
    ) -> str:

        return (
            f"[{payload.risk.risk_level.name}] "
            f"{payload.alert_message}\n"
            f"Location: {payload.node_name}\n"
            f"Coordinates: "
            f"{payload.location.latitude:.4f}, "
            f"{payload.location.longitude:.4f}\n"
            f"Prediction: "
            f"{payload.risk.prediction_horizon}\n"
            f"Recommended action:\n"
            f"{payload.risk.recommended_action}"
        )