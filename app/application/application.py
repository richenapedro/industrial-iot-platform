import time

from app.handlers.console_event_handler import ConsoleEventHandler
from app.models.machine import Machine
from app.repositories.in_memory_event_store import InMemoryEventStore
from app.services.machine_service import MachineService
from app.simulator import MachineSimulator
from app.config import AppConfig


class Application:
    def __init__(self):
        self.config = AppConfig()
        self.machine = Machine(
            machine_id=self.config.machine_id,
            manufacturer=self.config.machine_manufacturer,
            controller=self.config.machine_controller,
        )
        self.service = MachineService()
        self.simulator = MachineSimulator(machine=self.machine, service=self.service)
        self.handler = ConsoleEventHandler()
        self.event_store = InMemoryEventStore()

    def run(self) -> None:
        try:
            while True:
                event = self.simulator.simulate_state_change()

                if event:
                    self.event_store.save(event)
                    self.handler.handle_machine_state_changed(event)

                    machine_events = self.event_store.get_by_machine_id(
                        self.machine.machine_id
                    )
                    latest_event = self.event_store.get_latest_by_machine_id(
                        self.machine.machine_id
                    )

                    print(
                        f"Events for {self.machine.machine_id}: {len(machine_events)}"
                    )
                    print(f"Total events stored: {len(self.event_store.get_all())}")

                    if latest_event:
                        print(f"Latest event: {latest_event.to_dict()}")

                else:
                    print("No state change detected")

                time.sleep(self.config.simulation_interval_seconds)

        except KeyboardInterrupt:
            print("Application stopped by user.")

        except Exception as error:
            print(f"Application error: {error}")
