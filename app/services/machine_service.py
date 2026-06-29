from app.models.machine import Machine


class MachineService:
    def update_state(self, machine: Machine, new_state: str) -> None:
        machine.state = new_state
