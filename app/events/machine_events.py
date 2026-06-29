from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class MachineStateChangedEvent:
    machine_id: str
    previous_state: str
    new_state: str
    source: str
    timestamp: datetime

    @classmethod
    def create(
        cls,
        machine_id: str,
        previous_state: str,
        new_state: str,
        source: str,
    ) -> "MachineStateChangedEvent":
        return cls(
            machine_id=machine_id,
            previous_state=previous_state,
            new_state=new_state,
            source=source,
            timestamp=datetime.now(timezone.utc),
        )
