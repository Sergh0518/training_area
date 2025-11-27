# Родительский класс воздушных судов
class AirVehicle:
    """Инициализация объекта воздушного судна"""
    def __init__(self, name, size, purpose):
        self._name = name                  # Название воздушного судна
        self._size = size                  # Размер судна
        self._purpose = purpose            # Назначение судна

    # Геттер для name
    @property
    def name(self):
        """Возвращает название воздушного судна"""
        return self._name

    # Сеттер для name
    @name.setter
    def name(self, value):
        """Устанавливает новое значение имени воздушного судна"""
        self._name = value

    # Геттер для size
    @property
    def size(self):
        """Возвращает размер воздушного судна"""
        return self._size

    # Сеттер для size
    @size.setter
    def size(self, value):
        """Устанавливает новое значение размера воздушного судна"""
        self._size = value

    # Геттер для purpose
    @property
    def purpose(self):
        """Возвращает назначение воздушного судна"""
        return self._purpose

    # Сеттер для purpose
    @purpose.setter
    def purpose(self, value):
        """Устанавливает новое значение назначения воздушного судна"""
        self._purpose = value

    def info(self):
        """Предоставление информации о воздушном средстве"""
        return f'"{self.name}" имеет размер: "{self.size}" его направление: "{self.purpose}"'