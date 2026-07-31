"""
Factory responsible for creating EnvironmentalPayload instances.
"""

from datetime import datetime, timezone

from .enums import (
    RiskLevel,
    SensorType,
    SourceType,
)

from .models import (
    EnvironmentalPayload,
    Location,
    RiskAssessment,
    SensorReading,
)


class PayloadFactory:
    """
    Factory used to create fully initialized
    EnvironmentalPayload objects.
    """

    @staticmethod
    def create(
        *,
        device_id: str,
        node_name: str,
        latitude: float,
        longitude: float,
        altitude: float | None = None,
        sensor_type: SensorType,
        sensor_value: float,
        unit: str,
        source: SourceType = SourceType.SIMULATION,
    ) -> EnvironmentalPayload:

        return EnvironmentalPayload(

            device_id=device_id,

            node_name=node_name,

            timestamp=datetime.now(timezone.utc),

            location=Location(
                latitude=latitude,
                longitude=longitude,
                altitude=altitude,
            ),

            sensor=SensorReading(
                sensor_type=sensor_type,
                sensor_value=sensor_value,
                unit=unit,
            ),

            risk=RiskAssessment(
                risk_level=RiskLevel.UNKNOWN,
                alert_message="",
                prediction_horizon="",
                recommended_action="",
            ),

            source=source,
        )