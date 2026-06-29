from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    machine_id: str = "g352"
    machine_manufacturer: str = "GROB"
    machine_controller: str = "TNC7"
    simulation_interval_seconds: int = 2
