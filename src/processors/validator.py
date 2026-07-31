"""
Payload validator.
"""

from infrastructure.interfaces import BaseValidator

from domain.models import EnvironmentalPayload

from domain.exceptions import ValidationError

from domain.enums import SensorType


class PayloadValidator(BaseValidator):

    def validate(
        self,
        payload: EnvironmentalPayload,
    ) -> None:

        self._validate_device(payload)

        self._validate_location(payload)

        self._validate_sensor(payload)

    # ----------------------------------------------------

    def _validate_device(
        self,
        payload,
    ):

        if not payload.device_id:
            raise ValidationError(
                "Device ID cannot be empty."
            )

        if not payload.node_name:
            raise ValidationError(
                "Node name cannot be empty."
            )

    # ----------------------------------------------------

    def _validate_location(
        self,
        payload,
    ):

        if not (
            -90
            <= payload.location.latitude
            <= 90
        ):

            raise ValidationError(
                "Latitude out of range."
            )

        if not (
            -180
            <= payload.location.longitude
            <= 180
        ):

            raise ValidationError(
                "Longitude out of range."
            )

    # ----------------------------------------------------

    def _validate_sensor(
        self,
        payload,
    ):

        if (
            payload.sensor.sensor_type
            not in SensorType
        ):

            raise ValidationError(
                "Unsupported sensor."
            )

        if payload.sensor.sensor_value < 0:

            raise ValidationError(
                "Negative sensor value."
            )

        if payload.sensor.unit == "":

            raise ValidationError(
                "Sensor unit is empty."
            )