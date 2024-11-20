# Multiple inheritance
# class Mammal:
#     def mammal_info(self):
#         print("Mammals can give direct birth.")
# class WingedAnimal:
#     def winged_animal_info(self):
#         print("Winged animals can flap.")
 
# class Bat(Mammal, WingedAnimal):
#     pass
# b1 = Bat()
# b1.mammal_info()
# b1.winged_animal_info()
# --------------------------------------
# Multilevel inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         pass

# class Mammal(Animal):
#     def feed_young(self):
#         print("Feeding young")

# class Dog(Mammal):
#     def speak(self):
#         print("Woof!")
# dog1=Dog("Pitbul")
# print(dog1.name)
# -------------------
# Abstraction
from abc import abstractmethod,ABC
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass
class Bird(Flyable):
    def fly(self):
        print("The bird is flying")
class Plane(Flyable):
    def fly(self):
        print("The plane is flying")
plane=Plane()
plane.fly()
bird=Bird()
bird.fly()