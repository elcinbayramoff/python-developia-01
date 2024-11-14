# class Dog:
#     def sound(self):
#         return 'Hav hav'

# class Cat:
#     def sound(self):
#         return 'Meow Meow '

# class Duck:
#     def sound(self):
#         return 'duck duck'

# animals = [Dog(), Cat(), Duck()]

# for animal in animals:
#     print(animal.sound())


#Duck typing- If it looks like duck, if it swims like duck, if it behaves like duck then it is probably duck

#Poly with inheritance

class Shape:
    def area(self):
        return ''
class Square(Shape):
    def __init__(self, side):
        self.side = side       
    def area(self):
        return self.side * self.side
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius     
    def area(self):
        return 3.14 * self.radius * self.radius
s1 = Square(4)
c1 = Circle(2)
shapes = [s1, c1]
for i in shapes:
    print(i.area())

