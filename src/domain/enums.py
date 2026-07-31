"""
System enumerations.

Defines the supported sensor types, risk levels,
data sources and simulation scenarios.
"""

from enum import Enum


class SensorType(str, Enum):
    WATER_LEVEL = "water_level"
    RAINFALL = "rainfall"
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    PRESSURE = "pressure"


class RiskLevel(str, Enum):
    SAFE = "SAFE"
    ATTENTION = "ATTENTION"
    ALERT = "ALERT"
    CRITICAL = "CRITICAL"
    UNKNOWN = "UNKNOWN"


class SourceType(str, Enum):
    SIMULATION = "simulation"
    HARDWARE = "hardware"
    CSV = "csv"
    API = "api"
    MANUAL = "manual"
    SYNTHETIC = "synthetic"


class SimulationScenario(str, Enum):
    RANDOM = "random"
    SAFE = "safe"
    ATTENTION = "attention"
    ALERT = "alert"
    CRITICAL = "critical"