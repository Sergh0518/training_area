from .AirVehicle import *
from .IAirVehicle import *


# Класс наследник Дроны
class Drones(AirVehicle, IAirVehicle):
    def __init__(self, name, size, purpose, weight, fuel):
        """Инициализирует дрон с дополнительными параметрами веса и топлива"""
        super().__init__(name, size, purpose)               # Инициализация родительского класса
        self._weight = weight                               # Вес дрона
        self._fuel = fuel                                   # Тип двигателя (топливо)

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

    def info(self):
        """Представление подробной информации о дроне"""
        return f'Дрон: {super().info()}, Доп. характеристики:  Вес: "{self.weight}", Двигатель: "{self.fuel}"'

    def land(self):
        return 'садится'

    def fly_away(self):
        return 'улетает'

    def refuel(self):
        return 'заряжается'