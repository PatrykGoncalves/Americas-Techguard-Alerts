"""
Filesystem paths used by the application.
"""

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

OUTPUT_DIR = ROOT_DIR / "outputs"
DATA_DIR = ROOT_DIR / "data"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

EXECUTION_LOG = OUTPUT_DIR / "execution.log"
NOTIFICATION_LOG = OUTPUT_DIR / "notifications.log"
PAYLOAD_LOG = OUTPUT_DIR / "processed_payloads.json"
LATEST_PAYLOAD = OUTPUT_DIR / "latest_payload.json"