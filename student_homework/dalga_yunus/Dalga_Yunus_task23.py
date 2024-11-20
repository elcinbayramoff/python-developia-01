from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year, fuel_capacity, litr_per_km):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0
        self.total_distance = 0
        self.litr_per_km = litr_per_km

    def get_fuel_level(self):
        return self.fuel_level

    def refuel(self, amount):
        if self.fuel_level + amount > self.fuel_capacity:
            raise ValueError("Cannot refuel beyond fuel capacity!")
        self.fuel_level += amount

    def display_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Fuel Capacity: {self.fuel_capacity}L")
        print(f"Fuel Level: {self.fuel_level}L")
        print(f"Total Distance: {self.total_distance} km")

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def drive(self, distance):
        pass

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_capacity, litr_per_km, num_doors):
        super().__init__(make, model, year, fuel_capacity, litr_per_km)
        self.num_doors = num_doors

    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

    def drive(self, distance):
        required_fuel = distance * self.litr_per_km
        if self.fuel_level < required_fuel:
            raise ValueError("Not enough fuel to drive this distance!")
        self.fuel_level -= required_fuel
        self.total_distance += distance
        print(f"Car drove {distance} km.")

class Truck(Vehicle):
    def __init__(self, make, model, year, fuel_capacity, litr_per_km, cargo_capacity):
        super().__init__(make, model, year, fuel_capacity, litr_per_km)
        self.cargo_capacity = cargo_capacity

    def start_engine(self):
        print("Truck engine started.")

    def stop_engine(self):
        print("Truck engine stopped.")

    def drive(self, distance):
        required_fuel = distance * self.litr_per_km
        if self.fuel_level < required_fuel:
            raise ValueError("Not enough fuel to drive this distance!")
        self.fuel_level -= required_fuel
        self.total_distance += distance
        print(f"Truck drove {distance} km.")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_capacity, litr_per_km, engine_type):
        super().__init__(make, model, year, fuel_capacity, litr_per_km)
        self.engine_type = engine_type

    def start_engine(self):
        print("Motorcycle engine started.")

    def stop_engine(self):
        print("Motorcycle engine stopped.")

    def drive(self, distance):
        required_fuel = distance * self.litr_per_km
        if self.fuel_level < required_fuel:
            raise ValueError("Not enough fuel to drive this distance!")
        self.fuel_level -= required_fuel
        self.total_distance += distance
        print(f"Motorcycle drove {distance} km.")

if __name__ == "__main__":
    my_car = Car(make="Toyota", model="Corolla", year=2020, fuel_capacity=50, litr_per_km=0.1, num_doors=4)
    my_car.display_details()
    my_car.start_engine()
    my_car.refuel(30)
    print(f"Fuel Level after refuel: {my_car.get_fuel_level()}L")
    my_car.drive(100)
    print(f"Fuel Level after drive: {my_car.get_fuel_level()}L")
    my_car.stop_engine()

    my_truck = Truck(make="Ford", model="F-150", year=2021, fuel_capacity=100, litr_per_km=0.2, cargo_capacity=2000)
    my_truck.display_details()
    my_truck.start_engine()
    my_truck.refuel(70)
    print(f"Fuel Level after refuel: {my_truck.get_fuel_level()}L")
    my_truck.drive(50)
    print(f"Fuel Level after drive: {my_truck.get_fuel_level()}L")
    my_truck.stop_engine()

    my_motorcycle = Motorcycle(make="Harley-Davidson", model="Sportster", year=2022, fuel_capacity=20, litr_per_km=0.05, engine_type="V-Twin")
    my_motorcycle.display_details()
    my_motorcycle.start_engine()
    my_motorcycle.refuel(15)
    print(f"Fuel Level after refuel: {my_motorcycle.get_fuel_level()}L")
    my_motorcycle.drive(150)
    print(f"Fuel Level after drive: {my_motorcycle.get_fuel_level()}L")
    my_motorcycle.stop_engine()