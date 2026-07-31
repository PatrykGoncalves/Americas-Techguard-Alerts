"""
Environmental data simulator.
"""

from __future__ import annotations

import random

from infrastructure.interfaces import BaseSimulator
from infrastructure.simulation_config import (
    SIMULATION_RANGES,
    SENSOR_UNITS,
)
from infrastructure import config

from domain.enums import (
    SensorType,
    SimulationScenario,
)

from domain.models import SensorReading
from domain.factory import PayloadFactory


class EnvironmentalDataSimulator(BaseSimulator):

    def read(
        self,
        sensor_type: SensorType,
        scenario: SimulationScenario = SimulationScenario.RANDOM,
    ) -> SensorReading:

        ranges = SIMULATION_RANGES[sensor_type]

        if scenario not in ranges:
            scenario = SimulationScenario.RANDOM

        minimum, maximum = ranges[scenario]

        value = round(
            random.uniform(minimum, maximum),
            2,
        )

        return SensorReading(
            sensor_type=sensor_type,
            sensor_value=value,
            unit=SENSOR_UNITS[sensor_type],
        )

    def generate(
        self,
        sensor_type: SensorType,
        scenario: SimulationScenario = SimulationScenario.RANDOM,
    ):

        reading = self.read(
            sensor_type,
            scenario,
        )

        return PayloadFactory.create(

            device_id=config.DEVICE_ID,

            node_name=config.NODE_NAME,

            latitude=config.LATITUDE,

            longitude=config.LONGITUDE,

            altitude=config.ALTITUDE,

            sensor_type=reading.sensor_type,

            sensor_value=reading.sensor_value,

            unit=reading.unit,
        )