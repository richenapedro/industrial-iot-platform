from app.handlers.console_event_handler import ConsoleEventHandler
from app.models.machine import Machine
from app.services.machine_service import MachineService
from app.simulator import MachineSimulator
from app.repositories.in_memory_event_store import InMemoryEventStore


def main():
    machine = Machine(
        machine_id="g352",
        manufacturer="GROB",
        controller="TNC7",
    )

    service = MachineService()
    simulator = MachineSimulator(machine=machine, service=service)
    handler = ConsoleEventHandler()
    event_store = InMemoryEventStore()

    try:
        event = simulator.simulate_state_change()

        if event:
            event_store.save(event)
            handler.handle_machine_state_changed(event)
            print(f"Total events stored: {len(event_store.get_all())}")
        else:
            print("No state change detected")

    except Exception as error:
        print(f"Application error: {error}")


if __name__ == "__main__":
    main()
