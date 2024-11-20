# from math import sqrt

# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
        
#     def area(self):
#         return self.width*self.height
    
#     def perimetr(self):
#         return (self.width+self.height)*2
    
#     def diagonal(self):
#         d=sqrt(self.width**2+self.height**2)
#         round_d=round(d,2)
#         return round_d
    
#     def __str__(self) -> str:
#         return f"A rectangle with a width of {self.width} and a height of {self.height}"

# rect=Rectangle(3,4)
# print(rect)
# print("Area=",rect.area())
# print("Perimetr=",rect.perimetr())
# print("Diagonal=",rect.diagonal())
# ------------------------------------------------------
# INHERITANCES
# class Vehicle:
#     def __init__(self,make,model,year,max_speed):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.max_speed=max_speed
        
# class Motorcycle(Vehicle):
#     def __init__(self, make, model, year,max_speed,number_of_wheels):
#         super().__init__(make,model,year,max_speed)
#         self.number_of_wheels=number_of_wheels
        
# class Car(Vehicle):
#     def __init__(self,make, model, year,max_speed,doors):
#         super().__init__(make,model,year,max_speed)
#         self.doors=doors
        
# car1=Car('Mercedes-Benz','W140',1991,250,4)
# print(car1.make,car1.doors)
# print(car1.max_speed)
# ---------------------------------------------------
# POLYMORPHISM
# class Confectionery:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def full_name(self):
#         print("Everyone has their price.")
# class Cake(Confectionery):
#     def full_name(self):
#         print(f"Price of {self.name}:{self.price}")
# class Candy(Confectionery):
#     def full_name(self):
#         print(f"Price of {self.name}: {self.price}")
# candy1=Candy("Krokant",4)
# candy1.full_name()



