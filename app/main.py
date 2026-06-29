import time

from app.handlers.console_event_handler import ConsoleEventHandler
from app.models.machine import Machine
from app.services.machine_service import MachineService
from app.simulator import MachineSimulator


def main():
    machine = Machine(
        machine_id="g352",
        manufacturer="GROB",
        controller="TNC7",
    )

    service = MachineService()
    simulator = MachineSimulator(machine=machine, service=service)
    handler = ConsoleEventHandler()

    while True:
        event = simulator.simulate_state_change()

        if event:
            handler.handle_machine_state_changed(event)
        else:
            print("No state change detected")

        time.sleep(2)


if __name__ == "__main__":
    main()
