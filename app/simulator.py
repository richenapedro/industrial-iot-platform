import random
from app.models.machine_state import MachineState


class MachineSimulator:
    def __init__(self, machine_id: str):
        self.machine_id = machine_id
        self.states = [
            "OFFLINE",
            "IDLE",
            "AUTOMATIC",
            "MANUAL",
            "ALARM",
            "MAINTENANCE",
        ]

    def get_current_state(self) -> MachineState:
        state = random.choice(self.states)

        return MachineState.create(
            machine_id=self.machine_id,
            state=state,
            source="SIMULATOR",
        )
