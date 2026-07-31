"""
Payload serialization utilities.
"""

from __future__ import annotations

import json

from .models import EnvironmentalPayload


class PayloadSerializer:

    @staticmethod
    def to_dict(
        payload: EnvironmentalPayload,
    ) -> dict:

        return {

            "device_id": payload.device_id,

            "node_name": payload.node_name,

            "timestamp": payload.timestamp.isoformat(),

            "location": {

                "latitude": payload.location.latitude,

                "longitude": payload.location.longitude,

                "altitude": payload.location.altitude,
            },

            "sensor": {

                "sensor_type":
                    payload.sensor.sensor_type.value,

                "sensor_value":
                    payload.sensor.sensor_value,

                "unit":
                    payload.sensor.unit,
            },

            "risk": {

                "risk_level":
                    payload.risk.risk_level.value,

                "alert_message":
                    payload.risk.alert_message,

                "prediction_horizon":
                    payload.risk.prediction_horizon,

                "recommended_action":
                    payload.risk.recommended_action,
            },

            "source":
                payload.source.value,
        }

    @staticmethod
    def to_json(
        payload: EnvironmentalPayload,
        indent: int = 4,
    ) -> str:

        return json.dumps(

            PayloadSerializer.to_dict(payload),

            indent=indent,

            ensure_ascii=False,
        )

    @staticmethod
    def save(
        payload: EnvironmentalPayload,
        filename: str,
    ) -> None:

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as f:

            f.write(
                PayloadSerializer.to_json(payload)
            )


    @staticmethod
    def pretty_print(
        payload: EnvironmentalPayload,
    ) -> None:

        print(
            PayloadSerializer.to_json(payload)
        )