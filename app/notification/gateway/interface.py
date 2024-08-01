from abc import ABC, abstractmethod


class IGateway(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass
