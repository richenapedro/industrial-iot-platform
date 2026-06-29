from abc import ABC, abstractmethod
from typing import Any, Callable, Awaitable


class MachineConnector(ABC):
    @abstractmethod
    async def connect(self) -> None:
        pass

    @abstractmethod
    async def disconnect(self) -> None:
        pass

    @abstractmethod
    async def read(self, tag: str) -> Any:
        pass

    @abstractmethod
    async def write(self, tag: str, value: Any) -> None:
        pass

    @abstractmethod
    async def subscribe(
        self,
        tag: str,
        callback: Callable[[Any], Awaitable[None]],
    ) -> None:
        pass
