from enum import StrEnum


class MachineStateEnum(StrEnum):
    UNKNOWN = "UNKNOWN"
    IDLE = "IDLE"
    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"
    ALARM = "ALARM"
    MAINTENANCE = "MAINTENANCE"
