# a = str()
# a = int('5')
# list()
# tuple()
# dict()

#class +
#obyektler +
#metodlari
#atributlar 
#static classmetod
# class Car: # Boyukle baslamaq ve sozleri CamelCase yazmaq
#     model = 'Toyoto'
#     color = 'Black'
    
# car1 = Car() # Obyekti
# car2 = Car()
# # car1.model = 'Porsche'
# # car1.color = 'Red'
# print(car1.model, car1.color)
# print(car2.model, car2.color)

# print(type(car1))
# print(type('salam'))
#dunder method, magic metods

# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
        
#     def data(self):
#         print(f'{self.model} {self.color}')
    
# car1 = Car('Porsche', 'White')
# car1.data()

# car2 = Car('Toyoto', 'Black')
# car2.data()


class Person:
    count = 0
    member_names = []
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
        Person.count += 1
        Person.member_names.append(self.name)
        
    def greet(self, soz):
        print(f'{soz}, {self.name} {self.surname}')
    
person1 = Person('Ehmed', 'Ehmedov') #instance, obyekt
person2 = Person('Ali', 'Aliyev')
# print(person2.count)
person3 = Person('Vali', 'Valiyev')
# print(person3.count)
# print(person3.member_names)
# person3.count=0
# print(person3.count)
# print(person2.count)
person3.age = 15
print(person3.age)

# person1.greet('Hello')