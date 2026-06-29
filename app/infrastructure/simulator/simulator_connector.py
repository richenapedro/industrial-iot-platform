import random
from typing import Any, Awaitable, Callable

from app.domain.interfaces.machine_connector import MachineConnector
from app.domain.models.machine_state_enum import MachineStateEnum


class SimulatorConnector(MachineConnector):
    def __init__(self):
        self.connected = False
        self.values = {
            "machine_state": MachineStateEnum.UNKNOWN,
            "program": None,
            "active_tool": None,
            "alarm_active": False,
        }

    async def connect(self) -> None:
        self.connected = True

    async def disconnect(self) -> None:
        self.connected = False

    async def read(self, tag: str) -> Any:
        return self.values.get(tag)

    async def write(self, tag: str, value: Any) -> None:
        self.values[tag] = value

    async def subscribe(
        self,
        tag: str,
        callback: Callable[[Any], Awaitable[None]],
    ) -> None:
        value = random.choice(
            [
                MachineStateEnum.IDLE,
                MachineStateEnum.AUTOMATIC,
                MachineStateEnum.MANUAL,
                MachineStateEnum.ALARM,
                MachineStateEnum.MAINTENANCE,
            ]
        )

        self.values[tag] = value
        await callback(value)
