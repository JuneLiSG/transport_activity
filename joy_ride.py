from car_class import Car
from aircraft_class import Aircraft
from boat_class import Boat
from engineless_class import Engineless

my_car = Car("VW", "blue", 150)
heli = Aircraft("helicopter", 7, 140, 12000)
boeing_747 = Aircraft("Boeing 747", 150, 614, 35000)
my_boat = Boat("yellow", "medium", 200)
bicycle = Engineless("bike", "red", 50)
scooter = Engineless("scooter", "green", 15)

garage = [my_car.type, my_boat.type, heli.name, boeing_747.name, bicycle.name, scooter.name]

def choose_vehicle(list):
    print(list)
    vehicle_choice = ""
    while vehicle_choice not in list:
        vehicle_choice = input("Please choose your vehicle: ")
    return vehicle_choice

choose_vehicle(garage)