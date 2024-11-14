#Abstraction - mucerred
# from abc import ABC, abstractmethod

# class Shape(ABC):
    
#     @abstractmethod
#     def perimeter(self):
#         pass
    
#     @abstractmethod
#     def area(self):
#         pass
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
    
#     def area(self):
#         return 3.14 * self.radius * self.radius
    
# class Rectangle(Shape):
#     def __init__(self, side):
#         self.side = side
    
#     def perimeter(self):
#         return 4 * self.side
    
#     def area(self):
#         return self.side ** 2
    
# c1 = Circle(4)
# print(c1.area())

# r1 = Rectangle(4)
# print(r1.area())

# s1 = Shape() OLMAZZZZ
# print(s1) 
# from abc import ABC, abstractmethod

# class Person(ABC): # Base, Parent
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname

#     @abstractmethod
#     def details(self):
#         return {
#             'name' : self.name,
#             'surname' : self.surname
#                 }

# class Student(Person): #child class
#     def __init__(self, name: str, surname: str, status: bool):
#         super().__init__(name, surname)
#         self.status = status

#     def details(self):
#         data = super().details()
#         data['status'] = self.status
#         return data
    
#     def get_fullname(self):
#         return f'{self.surname} {self.name}'

# st1 = Student('Ali','Aliyev',True)
# print(st1.details())


