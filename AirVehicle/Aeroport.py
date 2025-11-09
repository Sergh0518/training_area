class Aeroport:
    def __init__(self, size_area, vehicles):
        """Инициализирует аэропорт заданной площадью и списком воздушных судов.
           Этот класс хранит список воздушных судов и управляет ими,
           позволяя обращаться к каждому экземпляру отдельно.
        """
        self._size_area = size_area                    # Площадь аэропорта
        self._vehicles = vehicles                      # Список воздушных судов

    # Геттер для size_area
    @property
    def size_area(self):
        """Возвращает площадь аэропорта"""
        return self._size_area

    # Сеттер для size_area
    @size_area.setter
    def size_area(self, value):
        """Устанавливает новое значение площади аэропорта"""
        self._size_area = value

    # Геттер для vehicles
    @property
    def vehicles(self):
        """Возвращает список воздушных судов"""
        return self._vehicles

    # Сеттер для vehicles
    @vehicles.setter
    def vehicles(self, value):
        """Устанавливает новое значение списку воздушных судов"""
        self._vehicles = value