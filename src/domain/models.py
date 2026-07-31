"""
Domain models.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from datetime import datetime

from .enums import (
    RiskLevel,
    SensorType,
    SourceType,
)


# ---------------------------------------------------------
# Basic models
# ---------------------------------------------------------


@dataclass(slots=True)
class Location:

    latitude: float

    longitude: float

    altitude: float | None = None


@dataclass(slots=True)
class SensorReading:

    sensor_type: SensorType

    sensor_value: float

    unit: str


@dataclass(slots=True)
class RiskAssessment:
    """
    Result of the environmental risk assessment.
    """

    risk_level: RiskLevel

    alert_message: str

    prediction_horizon: str

    recommended_action: str


# ---------------------------------------------------------
# Rule model
# ---------------------------------------------------------


@dataclass(frozen=True, slots=True)
class ThresholdRule:
    """
    Represents a threshold-based risk classification rule.
    """

    minimum: float
    maximum: float
    risk_level: RiskLevel
    alert_message: str
    prediction_horizon: str
    recommended_action: str

    def matches(self, value: float) -> bool:
        return self.minimum <= value < self.maximum

# ---------------------------------------------------------
# Main domain object
# ---------------------------------------------------------


@dataclass(slots=True)
class EnvironmentalPayload:

    device_id: str

    node_name: str

    timestamp: datetime

    location: Location

    sensor: SensorReading

    risk: RiskAssessment = field(
        default_factory=RiskAssessment
    )

    source: SourceType = (
        SourceType.SIMULATION
    )

    # -----------------------------------------------------

    @property
    def value(self) -> float:

        return self.sensor.sensor_value

    @property
    def sensor_type(self) -> SensorType:

        return self.sensor.sensor_type

    @property
    def risk_level(self) -> RiskLevel:

        return self.risk.risk_level

    @property
    def alert_message(self) -> str:

        return self.risk.alert_message

    # -----------------------------------------------------

    def update_risk(
            self,
            level,
            message,
            prediction_horizon="",
            recommended_action="",
    ):
        self.risk.risk_level = level
        self.risk.alert_message = message
        self.risk.prediction_horizon = prediction_horizon
        self.risk.recommended_action = recommended_action

    # -----------------------------------------------------

    def is_simulated(self) -> bool:

        return (
            self.source
            is SourceType.SIMULATION
        )

    # -----------------------------------------------------

    def __str__(self):

        return (

            f"{self.device_id} | "

            f"{self.sensor.sensor_type.value}: "

            f"{self.sensor.sensor_value:.2f} "

            f"{self.sensor.unit}"

        )