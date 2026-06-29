import random

from app.models.machine import Machine
from app.services.machine_service import MachineService


class MachineSimulator:
    def __init__(self, machine: Machine, service: MachineService):
        self.machine = machine
        self.service = service
        self.states = [
            "IDLE",
            "AUTOMATIC",
            "MANUAL",
            "ALARM",
            "MAINTENANCE",
        ]

    def simulate_state_change(self):
        new_state = random.choice(self.states)

        return self.service.update_state(
            machine=self.machine,
            new_state=new_state,
            source="SIMULATOR",
        )
