"""
Monitoring pipeline.
"""

from domain.models import EnvironmentalPayload


class MonitoringPipeline:

    def __init__(
        self,
        simulator,
        validator,
        risk_engine,
        logger,
    ):

        self.simulator = simulator
        self.validator = validator
        self.risk_engine = risk_engine
        self.logger = logger

    def execute(
        self,
        sensor_type,
        scenario,
    ) -> EnvironmentalPayload:

        self.logger.info(
            "Monitoring pipeline started."
        )

        payload = self.simulator.generate(
            sensor_type=sensor_type,
            scenario=scenario,
        )

        self.logger.info(
            "Payload generated."
        )

        self.validator.validate(payload)

        self.logger.info(
            "Payload validated."
        )

        self.risk_engine.evaluate(payload)

        self.logger.info(
            f"Risk classified as {payload.risk_level.value}."
        )

        self.logger.save_payload(payload)

        self.logger.info(
            "Monitoring pipeline finished."
        )

        return payload