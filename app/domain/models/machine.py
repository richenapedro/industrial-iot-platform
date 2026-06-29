from dataclasses import dataclass

from app.models.machine_state_enum import MachineStateEnum


@dataclass
class Machine:
    machine_id: str
    manufacturer: str
    controller: str
    state: MachineStateEnum = MachineStateEnum.UNKNOWN
    program: str | None = None
    active_tool: str | None = None
    alarm_active: bool = False
