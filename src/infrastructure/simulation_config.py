"""
Simulation ranges.
"""

from domain.enums import (
    SensorType,
    SimulationScenario,
)

SIMULATION_RANGES = {

    SensorType.WATER_LEVEL: {

        SimulationScenario.SAFE:
            (0.20, 0.90),

        SimulationScenario.ATTENTION:
            (1.00, 1.90),

        SimulationScenario.ALERT:
            (2.00, 2.90),

        SimulationScenario.CRITICAL:
            (3.00, 4.00),

        SimulationScenario.RANDOM:
            (0.20, 4.00),
    },

    SensorType.RAINFALL: {

        SimulationScenario.SAFE:
            (0, 10),

        SimulationScenario.ATTENTION:
            (10, 40),

        SimulationScenario.ALERT:
            (40, 80),

        SimulationScenario.CRITICAL:
            (80, 120),

        SimulationScenario.RANDOM:
            (0, 120),
    },
}

SENSOR_UNITS = {

    SensorType.WATER_LEVEL:
        "m",

    SensorType.RAINFALL:
        "mm",

    SensorType.TEMPERATURE:
        "°C",

    SensorType.HUMIDITY:
        "%",

    SensorType.PRESSURE:
        "hPa",
}