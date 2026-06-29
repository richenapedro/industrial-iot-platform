from app.events.machine_events import MachineStateChangedEvent
from app.models.machine import Machine


class MachineService:
    def update_state(
        self,
        machine: Machine,
        new_state: str,
        source: str = "UNKNOWN",
    ) -> MachineStateChangedEvent | None:
        previous_state = machine.state

        if previous_state == new_state:
            return None

        machine.state = new_state

        return MachineStateChangedEvent.create(
            machine_id=machine.machine_id,
            previous_state=previous_state,
            new_state=new_state,
            source=source,
        )
