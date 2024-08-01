from abc import ABC, abstractmethod


class INotificationRepository(ABC):
    @abstractmethod
    def retrieve(self, key: str):
        pass

    @abstractmethod
    def create(self, key: str, value: str, ex: int):
        pass

    @abstractmethod
    def increment(self, key: str):
        pass
