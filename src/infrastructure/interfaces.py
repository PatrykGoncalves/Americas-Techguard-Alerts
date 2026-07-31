"""
Application interfaces.
"""

from abc import ABC
from abc import abstractmethod

from domain.models import (
    EnvironmentalPayload,
    SensorReading,
)

from domain.enums import (
    SensorType,
    SimulationScenario,
)


class BaseSimulator(ABC):

    @abstractmethod
    def read(
        self,
        sensor_type: SensorType,
        scenario: SimulationScenario,
    ) -> SensorReading:
        ...

    @abstractmethod
    def generate(
        self,
        sensor_type: SensorType,
        scenario: SimulationScenario,
    ) -> EnvironmentalPayload:
        ...


class BaseValidator(ABC):

    @abstractmethod
    def validate(
        self,
        payload: EnvironmentalPayload,
    ) -> None:
        ...


class BaseRiskEngine(ABC):

    @abstractmethod
    def evaluate(
        self,
        payload: EnvironmentalPayload,
    ) -> None:
        ...

class BaseLogger(ABC):

    @abstractmethod
    def info(
        self,
        message: str,
    ) -> None:
        ...

    @abstractmethod
    def warning(
        self,
        message: str,
    ) -> None:
        ...

    @abstractmethod
    def error(
        self,
        message: str,
    ) -> None:
        ...

    @abstractmethod
    def save_payload(
        self,
        payload: EnvironmentalPayload,
    ) -> None:
        ...