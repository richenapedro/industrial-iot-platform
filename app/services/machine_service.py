from app.events.machine_events import MachineStateChangedEvent
from app.models.machine import Machine


class MachineService:
    allowed_transitions = {
        "UNKNOWN": ["IDLE"],
        "IDLE": ["AUTOMATIC", "MANUAL", "MAINTENANCE"],
        "AUTOMATIC": ["IDLE", "ALARM"],
        "MANUAL": ["IDLE", "MAINTENANCE"],
        "ALARM": ["MANUAL"],
        "MAINTENANCE": ["IDLE"],
    }

    def update_state(
        self,
        machine: Machine,
        new_state: str,
        source: str = "UNKNOWN",
    ) -> MachineStateChangedEvent | None:
        previous_state = machine.state

        if previous_state == new_state:
            return None

        if not self._is_transition_allowed(previous_state, new_state):
            raise ValueError(
                f"Invalid state transition: {previous_state} -> {new_state}"
            )

        machine.state = new_state

        return MachineStateChangedEvent.create(
            machine_id=machine.machine_id,
            previous_state=previous_state,
            new_state=new_state,
            source=source,
        )

    def _is_transition_allowed(self, previous_state: str, new_state: str) -> bool:
        allowed_next_states = self.allowed_transitions.get(previous_state, [])
        return new_state in allowed_next_states
