from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class MachineState:
    machine_id: str
    state: str
    source: str
    timestamp: datetime
    quality: str = "GOOD"

    @classmethod
    def create(
        cls,
        machine_id: str,
        state: str,
        source: str = "SIMULATOR",
        quality: str = "GOOD",
    ) -> "MachineState":
        return cls(
            machine_id=machine_id,
            state=state,
            source=source,
            quality=quality,
            timestamp=datetime.now(timezone.utc),
        )

    def to_dict(self) -> dict:
        return {
            "machine_id": self.machine_id,
            "state": self.state,
            "source": self.source,
            "quality": self.quality,
            "timestamp": self.timestamp.isoformat(),
        }
