"""
Custom exceptions used throughout the project.
"""


class MonitoringError(Exception):
    """Base exception."""


class ValidationError(MonitoringError):
    """Raised when payload validation fails."""


class RiskEngineError(MonitoringError):
    """Raised when the risk cannot be classified."""