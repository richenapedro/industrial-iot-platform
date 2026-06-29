import random

from app.models.machine import Machine
from app.services.machine_service import MachineService


class MachineSimulator:
    def __init__(self, machine: Machine, service: MachineService):
        self.machine = machine
        self.service = service

    def simulate_state_change(self):
        possible_states = self.service.allowed_transitions.get(
            self.machine.state,
            ["UNKNOWN"],
        )

        new_state = random.choice(possible_states)

        return self.service.update_state(
            machine=self.machine,
            new_state=new_state,
            source="SIMULATOR",
        )
