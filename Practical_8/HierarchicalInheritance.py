class Vehicle:
    def vehicle_details(self):
        print("Vehicle Brand: Honda")
        print("Vehicle Type: Petrol")

class Car(Vehicle):
    def car_details(self):
        print("Car Model: City")
        print("Number of Doors: 4")

class Bike(Vehicle):
    def bike_details(self):
        print("Bike Model: Shine")
        print("Engine: 125cc")

car = Car()
car.vehicle_details()
car.car_details()

print()
 
bike = Bike()
bike.vehicle_details()
bike.bike_details()