from dataclasses import dataclass


@dataclass
class Machine:
    machine_id: str
    manufacturer: str
    controller: str
    state: str = "UNKNOWN"
    program: str | None = None
    active_tool: str | None = None
    alarm_active: bool = False
