from __future__ import annotations

from datetime import datetime
from pathlib import Path

from domain.models import EnvironmentalPayload
from domain.serializers import PayloadSerializer

from infrastructure import paths
from infrastructure.interfaces import BaseLogger

from processors.notification_formatter import (
    NotificationFormatter,
)



class ApplicationLogger(BaseLogger):

    def __init__(self):

        paths.OUTPUT_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

    # ---------------------------------------------------------

    def _write(
        self,
        file: Path,
        text: str,
    ) -> None:

        with open(
            file,
            "a",
            encoding="utf-8",
        ) as f:

            f.write(text)

    # ---------------------------------------------------------

    def _log(
        self,
        level: str,
        message: str,
    ) -> None:

        timestamp = datetime.now().isoformat()

        line = (
            f"[{timestamp}] "
            f"[{level}] "
            f"{message}\n"
        )

        print(line, end="")

        self._write(
            paths.EXECUTION_LOG,
            line,
        )

    # ---------------------------------------------------------

    def info(
        self,
        message: str,
    ) -> None:

        self._log("INFO", message)

    # ---------------------------------------------------------

    def warning(
        self,
        message: str,
    ) -> None:

        self._log("WARNING", message)

    # ---------------------------------------------------------

    def error(
        self,
        message: str,
    ) -> None:

        self._log("ERROR", message)

    # ---------------------------------------------------------

    def save_payload(
            self,
            payload: EnvironmentalPayload,
    ) -> None:
        print(">>> save_payload() executado")

        json_payload = PayloadSerializer.to_json(payload)

        self._write(
            paths.PAYLOAD_LOG,
            json_payload + "\n\n",
        )

        print(paths.LATEST_PAYLOAD)

        with open(
                paths.LATEST_PAYLOAD,
                "w",
                encoding="utf-8",
        ) as f:
            f.write(json_payload)

        notification = NotificationFormatter.format(payload)
        self.save_notification(notification)



    # ---------------------------------------------------------

    def save_notification(
        self,
        notification: str,
    ) -> None:

        self._write(

            paths.NOTIFICATION_LOG,

            notification + "\n\n",
        )