from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    def __init__(self, make, model, year, fuel_capacity, total_distance, litr_per_km):
        self.make = make
        self.model = model
        self.year = year
        
        self.fuel_capacity = fuel_capacity
        self.__fuel_level = 0
        
        self.total_distance = total_distance
        self.litr_per_km = litr_per_km
    
    def refuel(self, amount):
        if amount <= 0:
            print('Dogru qiymet teyin edilmedi')
            return
        
        if (self.__fuel_level + amount) > self.fuel_capacity:
            print('Maksimum tutum asildi')
            return
        self.__fuel_level += amount
            
    def get_fuel_level(self):
        return self.__fuel_level
    
    def display_details(self):
        return f'{self.make} {self.model} {self.year} {self.__fuel_level} {self.fuel_capacity}'
    
    @abstractmethod
    def start_engine(self):
        ...
    
    @abstractmethod
    def stop_engine(self):
        ...
        
    @abstractmethod
    def drive(self):
        ...

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_capacity, total_distance, litr_per_km, num_doors):
        super().__init__(make, model, year, fuel_capacity, total_distance, litr_per_km)
        self.num_doors = num_doors
        self.started = False
    def start_engine(self):
        self.started = True
        return f'Car started'
    
    def stop_engine(self):
        self.started = False
        return f'Car stoped'
    
    def drive(self, amount):
        litres = amount * self.litr_per_km
        if litres > self._Vehicle__fuel_level:
            print('Kifayet qeder yanacaq yoxdur')
            return
        self._Vehicle__fuel_level -= litres
        self.total_distance += amount
        
car1 = Car('Toyota', 'Carolla', 2020, 120, 0, 2, 4)

# print(car1.display_details())
print(car1.get_fuel_level())
car1.refuel(30)
car1.drive(5)
print(car1.get_fuel_level())
print(car1.start_engine())
    
        
    
