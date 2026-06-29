from app.events.machine_events import MachineStateChangedEvent


class ConsoleEventHandler:
    def handle_machine_state_changed(
        self,
        event: MachineStateChangedEvent,
    ) -> None:
        print(event.to_dict())
