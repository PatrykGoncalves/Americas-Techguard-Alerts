"""
Americas TechGuard - Environmental Alert Simulation

Main application entry point.
"""

from pipeline import MonitoringPipeline

from processors.simulator import (
    EnvironmentalDataSimulator,
)

from processors.validator import (
    PayloadValidator,
)

from processors.risk_engine import (
    RiskEngine,
)

from processors.logger import (
    ApplicationLogger,
)

from domain.enums import (
    SensorType,
    SimulationScenario,
)

from domain.serializers import (
    PayloadSerializer,
)


def main():

    pipeline = MonitoringPipeline(

        simulator=EnvironmentalDataSimulator(),

        validator=PayloadValidator(),

        risk_engine=RiskEngine(),

        logger=ApplicationLogger(),

    )

    payload = pipeline.execute(

        sensor_type=SensorType.WATER_LEVEL,

        scenario=SimulationScenario.ALERT,

    )

    print("\n" + "=" * 70)

    print("FINAL PAYLOAD")

    print("=" * 70)

    print(
        PayloadSerializer.to_json(
            payload
        )
    )


if __name__ == "__main__":
    main()