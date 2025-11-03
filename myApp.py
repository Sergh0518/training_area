from AirVehicle import *

# Создание экземпляров каждого типа транспортных средств
aerobus = Airplanes('Аэробус', 100, 'Гражданские перелёты',5000, 'Керосин', 300)     # объект самолёта
jet_aircraft = Airplanes('Jet', 10, 'Частные полеты на джет', 5000, 'Керосин', 7)    # объект самолёта
mi_8 = Helicopters('Ми-8', 10, 'Транспортировка грузов', 4000, 'Керосин', 4)         # объект вертолёта
helicopter = Helicopters('Aligator', 8, 'Военные операции', 3000, 'Керосин', 4)      # объект вертолёта
drone = Drones('H-Aero', 1, 'Разведка местности', 0.5, 'Электропривод')                         # объект дрона
dirigible = Airships('Airlander', 20, 'Рекламные акции', 4000, 'Электропривод')                 # объект дирижабля


# Выводы информации обо всех объектах
print(aerobus.info())
print(mi_8.info())
print(jet_aircraft.info())
print(helicopter.info())
print(drone.info())
print(dirigible.info())
print('========================')
print(aerobus.refuel())
print(aerobus.wait_for_landing())
print(aerobus.fly_away())
print(aerobus.land())
print(mi_8.refuel())
print(mi_8.wait_for_landing())
print(mi_8.fly_away())
print(mi_8.land())
print(jet_aircraft.refuel())
print(jet_aircraft.wait_for_landing())
print(jet_aircraft.fly_away())
print(jet_aircraft.land())
print(helicopter.refuel())
print(helicopter.wait_for_landing())
print(helicopter.fly_away())
print(helicopter.land())
print(drone.refuel())
print(drone.fly_away())
print(drone.land())
print(dirigible.refuel())
print(dirigible.fly_away())
print(dirigible.land())