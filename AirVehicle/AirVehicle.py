from abc import ABC, abstractmethod

class Aeroport:
    def __init__(self, size_area):
        self.size_area = size_area


class IAirVehicle(ABC):
    @abstractmethod
    def land(self):
        raise NotImplementedError

    @abstractmethod
    def fly_away(self):
        raise NotImplementedError

    @abstractmethod
    def refuel(self):
        raise NotImplementedError


class IPassengerTransportation(ABC):
    @abstractmethod
    def wait_for_landing(self):
        raise NotImplementedError


# Родительский класс воздушных судов
class AirVehicle:
    def __init__(self, name, size, purpose):
        self._name = name
        self._size = size
        self._purpose = purpose

    # Геттер для name
    @property
    def name(self):
        return self._name

    # Сеттер для name
    @name.setter
    def name(self, value):
        self._name = value

    # Геттер для size
    @property
    def size(self):
        return self._size

    # Сеттер для size
    @size.setter
    def size(self, value):
        self._size = value

    # Геттер для purpose
    @property
    def purpose(self):
        return self._purpose

    # Сеттер для purpose
    @purpose.setter
    def purpose(self, value):
        self._purpose = value

    def info(self):
        return f'"{self._name}" имеет размер: "{self._size}" его направление: "{self._purpose}"'

# Классы наследники для разных видов воздушных судов
class Airplanes(AirVehicle, IAirVehicle, IPassengerTransportation):                       # Самолёты
    def __init__(self, name, size, purpose, weight, fuel, passengers):
        super().__init__(name, size, purpose)
        self._weight = weight
        self._fuel = fuel
        self._passengers = passengers

    # Геттер для weight
    @property
    def weight(self):
        return self._weight

    # Сеттер для weight
    @weight.setter
    def weight(self, value):
        self._weight = value

    # Геттер для fuel
    @property
    def fuel(self):
        return self._fuel

    # Сеттер для fuel
    @fuel.setter
    def fuel(self, value):
        self._fuel = value

    # Геттер для passengers
    @property
    def passengers(self):
        return self._passengers

    # Сеттер для passengers
    @passengers.setter
    def passengers(self, value):
        self._passengers = value


    def info(self):
        return f'Самолет: {super().info()}, Доп. характеристики:  Вес: "{self.weight}", ДВС: "{self.fuel}", Кол-во пассажиров: "{self.passengers}"'

    def land(self):
        return f'{self.name} садится'

    def fly_away(self):
        return f'{self.name} улетает'

    def refuel(self):
        return f'{self.name} заправляется'

    def wait_for_landing(self):
        return f'{self.name} ожидает посадки'


class Helicopters(AirVehicle, IAirVehicle, IPassengerTransportation):                     # Вертолёты
    def __init__(self, name, size, purpose, weight, fuel, passengers):
        super().__init__(name, size, purpose)
        self._weight = weight
        self._fuel = fuel
        self._passengers = passengers

    # Геттер для weight
    @property
    def weight(self):
        return self._weight

    # Сеттер для weight
    @weight.setter
    def weight(self, value):
        self._weight = value

    # Геттер для fuel
    @property
    def fuel(self):
        return self._fuel

    # Сеттер для fuel
    @fuel.setter
    def fuel(self, value):
        self._fuel = value

    # Геттер для passengers
    @property
    def passengers(self):
        return self._passengers

    # Сеттер для passengers
    @passengers.setter
    def passengers(self, value):
        self._passengers = value

    def info(self):
        return f'Вертолет: {super().info()}, Доп. характеристики:  Вес: "{self.weight}", ДВС: "{self.fuel}", Кол-во пассажиров: "{self.passengers}"'

    def land(self):
        return f'{self.name} садится'

    def fly_away(self):
        return f'{self.name} улетает'

    def refuel(self):
        return f'{self.name} заправляется'

    def wait_for_landing(self):
        return f'{self.name} ожидает посадки'


class Drones(AirVehicle, IAirVehicle):                           # Дроны
    def __init__(self, name, size, purpose, weight, fuel):
        super().__init__(name, size, purpose)
        self._weight = weight
        self._fuel = fuel

    # Геттер для weight
    @property
    def weight(self):
        return self._weight

    # Сеттер для weight
    @weight.setter
    def weight(self, value):
        self._weight = value

    # Геттер для fuel
    @property
    def fuel(self):
        return self._fuel

    # Сеттер для fuel
    @fuel.setter
    def fuel(self, value):
        self._fuel = value

    def info(self):
        return f'Дрон: {super().info()}, Доп. характеристики:  Вес: "{self.weight}", Двигатель: "{self.fuel}"'

    def land(self):
        return f'{self.name} садится'

    def fly_away(self):
        return f'{self.name} улетает'

    def refuel(self):
        return f'{self.name} заряжается'


class Airships(AirVehicle, IAirVehicle):                         # Дирижабли
    def __init__(self, name, size, purpose, weight, fuel):
        super().__init__(name, size, purpose)
        self._weight = weight
        self._fuel = fuel

    # Геттер для weight
    @property
    def weight(self):
        return self._weight

    # Сеттер для weight
    @weight.setter
    def weight(self, value):
        self._weight = value

    # Геттер для fuel
    @property
    def fuel(self):
        return self._fuel

    # Сеттер для fuel
    @fuel.setter
    def fuel(self, value):
        self._fuel = value

    def info(self):
        return f'Дирижабль: {super().info()}, Доп. характеристики:  Вес: "{self.weight}", Двигатель: "{self.fuel}"'

    def land(self):
        return f'{self.name} садится'

    def fly_away(self):
        return f'{self.name} улетает'

    def refuel(self):
        return f'{self.name} заправляется'