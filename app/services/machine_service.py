from app.events.machine_events import MachineStateChangedEvent
from app.models.machine import Machine
from app.models.machine_state_enum import MachineStateEnum
from app.exceptions import InvalidMachineStateTransitionError


class MachineService:
    allowed_transitions = {
        MachineStateEnum.UNKNOWN: [MachineStateEnum.IDLE],
        MachineStateEnum.IDLE: [
            MachineStateEnum.AUTOMATIC,
            MachineStateEnum.MANUAL,
            MachineStateEnum.MAINTENANCE,
        ],
        MachineStateEnum.AUTOMATIC: [
            MachineStateEnum.IDLE,
            MachineStateEnum.ALARM,
        ],
        MachineStateEnum.MANUAL: [
            MachineStateEnum.IDLE,
            MachineStateEnum.MAINTENANCE,
        ],
        MachineStateEnum.ALARM: [MachineStateEnum.MANUAL],
        MachineStateEnum.MAINTENANCE: [MachineStateEnum.IDLE],
    }

    def update_state(
        self,
        machine: Machine,
        new_state: MachineStateEnum,
        source: str = "UNKNOWN",
    ) -> MachineStateChangedEvent | None:
        previous_state = machine.state

        if previous_state == new_state:
            return None

        if not self._is_transition_allowed(previous_state, new_state):
            raise InvalidMachineStateTransitionError(
                f"Invalid state transition: {previous_state} -> {new_state}"
            )

        machine.state = new_state

        return MachineStateChangedEvent.create(
            machine_id=machine.machine_id,
            previous_state=previous_state.value,
            new_state=new_state.value,
            source=source,
        )

    def _is_transition_allowed(
        self,
        previous_state: MachineStateEnum,
        new_state: MachineStateEnum,
    ) -> bool:
        allowed_next_states = self.allowed_transitions.get(previous_state, [])
        return new_state in allowed_next_states
