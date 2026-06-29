from app.events.machine_events import MachineStateChangedEvent


class InMemoryEventStore:
    def __init__(self):
        self.events: list[MachineStateChangedEvent] = []

    def save(self, event: MachineStateChangedEvent) -> None:
        self.events.append(event)

    def get_all(self) -> list[MachineStateChangedEvent]:
        return self.events
