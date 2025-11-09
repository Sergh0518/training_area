from AirVehicle.Airplanes import *
from AirVehicle.Helicopters import *
from AirVehicle.Drones import *
from AirVehicle.Airships import *
from AirVehicle.Aeroport import *



# Создание экземпляров каждого типа транспортных средств
aerobus = Airplanes('Аэробус', 100, 'Гражданские перелёты',5000, 'Керосин', 300)     # объект самолёта
jet_aircraft = Airplanes('Jet', 10, 'Частные полеты на джет', 5000, 'Керосин', 7)    # объект самолёта
mi_8 = Helicopters('Ми-8', 10, 'Транспортировка грузов', 4000, 'Керосин', 4)         # объект вертолёта
helicopter = Helicopters('Aligator', 8, 'Военные операции', 3000, 'Керосин', 4)      # объект вертолёта
drone = Drones('H-Aero', 1, 'Разведка местности', 0.5, 'Электропривод')                         # объект дрона
dirigible = Airships('Airlander', 20, 'Рекламные акции', 4000, 'Электропривод')                 # объект дирижабля

# Массив воздушных судов
vehicles = {'Аэробус': aerobus, 'Jet': jet_aircraft, 'Ми-8': mi_8, 'Aligator': helicopter, 'H-Aero': drone, 'Airlander': dirigible}

# Создание экземпляра класса Aeroport
aeroport = Aeroport(10000, vehicles)

print('Время 08:00')
print(f"{aeroport.vehicles['Airlander'].name} {aeroport.vehicles['Airlander'].refuel()}")
print(f"{aeroport.vehicles['Airlander'].name} {aeroport.vehicles['Airlander'].fly_away()}")
print('Время 09:00')
print(f"{aeroport.vehicles['Aligator'].name} {aeroport.vehicles['Aligator'].land()}")
print(f"{aeroport.vehicles['Aligator'].name} {aeroport.vehicles['Aligator'].wait_for_landing()}")
print(f"{aeroport.vehicles['Aligator'].name} {aeroport.vehicles['Aligator'].fly_away()}")
print('Время 12:00')
print(f"{aeroport.vehicles['Аэробус'].name} {aeroport.vehicles['Аэробус'].refuel()}")
print(f"{aeroport.vehicles['Аэробус'].name} {aeroport.vehicles['Аэробус'].wait_for_landing()}")
print(f"{aeroport.vehicles['Аэробус'].name} {aeroport.vehicles['Аэробус'].fly_away()}")
print('Время 18:00')
print(f"{aeroport.vehicles['Aligator'].name} {aeroport.vehicles['Aligator'].land()}")
print(f"{aeroport.vehicles['Aligator'].name} {aeroport.vehicles['Aligator'].refuel()}")
print('Время 20:00')
print(f"{aeroport.vehicles['Airlander'].name} {aeroport.vehicles['Airlander'].land()}")
print(f"{aeroport.vehicles['Airlander'].name} {aeroport.vehicles['Airlander'].refuel()}")