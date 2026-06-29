from app.events.machine_events import MachineStateChangedEvent


class InMemoryEventStore:
    def __init__(self):
        self.events: list[MachineStateChangedEvent] = []

    def save(self, event: MachineStateChangedEvent) -> None:
        self.events.append(event)

    def get_all(self) -> list[MachineStateChangedEvent]:
        return self.events

    def get_by_machine_id(self, machine_id: str) -> list[MachineStateChangedEvent]:
        return [event for event in self.events if event.machine_id == machine_id]

    def get_latest_by_machine_id(
        self,
        machine_id: str,
    ) -> MachineStateChangedEvent | None:
        machine_events = self.get_by_machine_id(machine_id)

        if not machine_events:
            return None

        return machine_events[-1]
