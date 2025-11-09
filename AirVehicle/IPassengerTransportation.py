from abc import ABC, abstractmethod


class IPassengerTransportation(ABC):
    @abstractmethod
    def wait_for_landing(self):
        """Обязательная реализация метода ожидания посадки"""
        raise NotImplementedError