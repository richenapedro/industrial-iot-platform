import time

from app.handlers.console_event_handler import ConsoleEventHandler
from app.models.machine import Machine
from app.repositories.in_memory_event_store import InMemoryEventStore
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
    event_store = InMemoryEventStore()

    try:
        while True:
            event = simulator.simulate_state_change()

            if event:
                event_store.save(event)
                handler.handle_machine_state_changed(event)

                machine_events = event_store.get_by_machine_id(machine.machine_id)
                latest_event = event_store.get_latest_by_machine_id(machine.machine_id)

                print(f"Events for {machine.machine_id}: {len(machine_events)}")
                print(f"Total events stored: {len(event_store.get_all())}")

                if latest_event:
                    print(f"Latest event: {latest_event.to_dict()}")

            else:
                print("No state change detected")

            time.sleep(2)

    except KeyboardInterrupt:
        print("Application stopped by user.")

    except Exception as error:
        print(f"Application error: {error}")


if __name__ == "__main__":
    main()
