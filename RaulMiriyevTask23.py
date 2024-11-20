from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model, year, fuel_capacity, litr_per_km):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.__fuel_level = 0
        self.total_distance = 0
        self.litr_per_km = litr_per_km

    def get_fuel_level(self):
        return self.__fuel_level

    def refuel(self, amount):
        if self.__fuel_level + amount > self.fuel_capacity:
            print("Cannot pass fuel capacity limit.")
            return
        self.__fuel_level += amount
        print(f"Fuel Level: {self.__fuel_level} litr")

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def drive(self, distance):
        pass

    def display_details(self):
        print(f"Producer: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Fuel Capacity: {self.fuel_capacity} litr")
        print(f"Fuel Level: {self.get_fuel_level()} litr")


class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} the engine started.")

    def stop_engine(self):
        print(f"{self.make} {self.model} the engine stopped.")

    def drive(self, distance):
        required_fuel = distance * self.litr_per_km
        if required_fuel > self.get_fuel_level():
            print("Not enough fuel.")
            return
        self.total_distance += distance
        self.refuel(-required_fuel)
        print(f"{distance} km distance traveled. Total distance: {self.total_distance} km.")

print("Starting...")

my_car = Car("Porsche", "911 GT3 RS", 2023, 50, 0.08)
print("Car Information:")
my_car.display_details()

print("\nAdding fuel...")
my_car.refuel(30)

print("\nStarting the engine...")
my_car.start_engine()

print("\nThe car is being driven...")
my_car.drive(100)

print("\nVehicle information is displayed again:")
my_car.display_details()

print("\nEngine stops...")
my_car.stop_engine()