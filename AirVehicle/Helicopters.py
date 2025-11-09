from .AirVehicle import *
from .IPassengerTransportation import *
from .IAirVehicle import *


# Класс наследник Вертолёты
class Helicopters(AirVehicle, IAirVehicle, IPassengerTransportation):
    def __init__(self, name, size, purpose, weight, fuel, passengers):
        """Инициализирует вертолет с дополнительными параметрами веса, топлива и числа пассажиров"""
        super().__init__(name, size, purpose)       # Инициализация родительского класса
        self._weight = weight                       # Вес вертолета
        self._fuel = fuel                           # Тип двигателя (топливо)
        self._passengers = passengers               # Количество пассажиров

    # Геттер для weight
    @property
    def weight(self):
        """Возвращает вес воздушного судна"""
        return self._weight

    # Сеттер для weight
    @weight.setter
    def weight(self, value):
        """Устанавливает новое значение веса воздушного судна"""
        self._weight = value

    # Геттер для fuel
    @property
    def fuel(self):
        """Возвращает тип двигателя воздушного судна"""
        return self._fuel

    # Сеттер для fuel
    @fuel.setter
    def fuel(self, value):
        """Устанавливает новое значение типа двигателя воздушного судна"""
        self._fuel = value

    # Геттер для passengers
    @property
    def passengers(self):
        """Возвращает количество пассажиров воздушного судна"""
        return self._passengers

    # Сеттер для passengers
    @passengers.setter
    def passengers(self, value):
        """Устанавливает новое значение количество пассажиров воздушного судна"""
        self._passengers = value

    def info(self):
        """Представление подробной информации о вертолете"""
        return f'Вертолет: {super().info()}, Доп. характеристики:  Вес: "{self.weight}", ДВС: "{self.fuel}", Кол-во пассажиров: "{self.passengers}"'

    def land(self):
        return 'садится'

    def fly_away(self):
        return 'улетает'

    def refuel(self):
        return 'заправляется'

    def wait_for_landing(self):
        return 'ожидает посадки'