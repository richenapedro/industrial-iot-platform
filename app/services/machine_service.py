from app.models.machine import Machine


class MachineService:
    def update_state(self, machine: Machine, new_state: str) -> bool:
        previous_state = machine.state

        if previous_state == new_state:
            return False

        machine.state = new_state
        return True
