from abc import ABC, abstractmethod


class IAirVehicle(ABC):
    """Эти интерфейсы определяют контракт, обязывающий классы реализовать указанные методы."""
    @abstractmethod
    def land(self):
        """Обязательная реализация метода приземления"""
        raise NotImplementedError

    @abstractmethod
    def fly_away(self):
        """Обязательная реализация метода полета"""
        raise NotImplementedError

    @abstractmethod
    def refuel(self):
        """Обязательная реализация метода заправки топливом"""
        raise NotImplementedError