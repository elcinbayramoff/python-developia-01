from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year, fuel_capacity, litr_per_km):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self._fuel_level = 0
        self.total_distance = 0
        self.litr_per_km = litr_per_km

    def get_fuel_level(self):
        return self_fuel_level

    def refuel(self, amount):
        if self._fuel_level + amount > self.fuel_capacity:
            raise ValueError("Yanacaq tutumu alisdi!")
        self_fuel_level += amount

    def display_details(seld):
        print(f"Istehlakci: {self.make}")
        print(f"Model: {self.model}")
        print("İl: {self.year}")
        print(f"Yanacaq baki: {self.fuel_capacity} L")
        print(f"Yanacaq Səviyyəsi: {self._fuel_level} L")

 