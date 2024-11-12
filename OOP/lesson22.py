# # a = str()
# # a = int('5')
# # list()
# # tuple()
# # dict()

# #class +
# #obyektler +
# #metodlari
# #atributlar 
# #static classmetod
# # class Car: # Boyukle baslamaq ve sozleri CamelCase yazmaq
# #     model = 'Toyoto'
# #     color = 'Black'
    
# # car1 = Car() # Obyekti
# # car2 = Car()
# # # car1.model = 'Porsche'
# # # car1.color = 'Red'
# # print(car1.model, car1.color)
# # print(car2.model, car2.color)

# # print(type(car1))
# # print(type('salam'))
# #dunder method, magic metods

# # class Car:
# #     def __init__(self, model, color):
# #         self.model = model
# #         self.color = color
        
# #     def data(self):
# #         print(f'{self.model} {self.color}')
    
# # car1 = Car('Porsche', 'White')
# # car1.data()

# # car2 = Car('Toyoto', 'Black')
# # car2.data()


# class Person:
#     count = 0
#     member_names = []
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
        
#         Person.count += 1
#         Person.member_names.append(self.name)
        
#     def greet(self, soz):
#         print(f'{soz}, {self.name} {self.surname}')
    
# person1 = Person('Ehmed', 'Ehmedov') #instance, obyekt
# person2 = Person('Ali', 'Aliyev')
# # print(person2.count)
# person3 = Person('Vali', 'Valiyev')
# # print(person3.count)
# # print(person3.member_names)
# # person3.count=0
# # print(person3.count)
# # print(person2.count)
# person3.age = 15
# print(person3.age)

# # person1.greet('Hello')
#dunder methods, magical methods, special methods _ _ func_name _ _. __init__()
#__str__, __repr__, __len__
from datetime import date

class BookReader:
    reader_count = 0
    readers = []
    
    def __init__(self, reader_name, birth_year, title, author, pages,age=None):
        self.reader_name = reader_name
        self.birth_year = birth_year
        self.age = age
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        BookReader.reader_count += 1
        BookReader.readers.append(reader_name)
    
    def read_pages(self, num: int) -> None:
        if self.current_page + num > self.pages:
            self.current_page = self.pages
            print('Kitab sehife limiti asildi')
        else:
            self.current_page += num
            print('Hal-hazirki kitab sehifesi guncellendi')
    
    def restart(self):
        self.current_page = 1
        print('Sizin hal-hazirki kitab sehifeniz 1-e qaytarildi')
    
    def bookmark(self):
        print(f'{self.pages}-in {self.current_page}-ci sehifesindesiniz')

    def __str__(self) -> str:
        return f'{self.reader_name} - {self.pages}-in {self.current_page}-ci sehifesindedir'
    
    def __repr__(self):
        return f'{BookReader.reader_count} - {BookReader.readers}'

    def __len__(self) -> int:
        return BookReader.reader_count
    
    #classmethods, staticmethods
    @classmethod
    def add_age(cls, reader_name, birth_year, title, author, pages):
        age = date.today().year - birth_year
        return cls(birth_year, reader_name, title, author, pages,age)
    
    @staticmethod
    def isAdult(age: int):
        if age < 18:
            raise ValueError('Yas 18-den kicikdir')
        print('Yas 18den boyukdur')
        
    
        
# reader1 =  BookReader('Ali','Sefiller-1', 'Viktor Huqo', 400)

# print(reader1.readers)

# reader2 = BookReader('Vali', 'Sefiller-2', 'Viktor Huqo', 420)

# print(BookReader.reader_count)
# print(reader2.readers)
print('-------------------------------------------------')
# reader1 =  BookReader('Ali',2000,'Sefiller-1', 'Viktor Huqo', 400)
# reader1.read_pages(100)

# reader2 =  BookReader('Ali1',2003,'Sefiller-1', 'Viktor Huqo', 400)
# reader2.read_pages(110)
# print(reader1)
# print(str(reader1))
# print(reader1.__str__())

# print(repr(reader1))
# print(reader1.__repr__())

# print(len(reader1))
#classmethods
# reader2 =  BookReader('Ali1',2003,'Sefiller-1', 'Viktor Huqo', 400)
# print(reader2.age)

# readerc =  BookReader.add_age('Ali',2000,'Sefiller-1', 'Viktor Huqo', 400)
# print(readerc.age)

#staticmethods
# reader2 =  BookReader('Ali1',2003,'Sefiller-1', 'Viktor Huqo', 400)
# reader2.isAdult(15)
#

#Class principles: 
        #Inheritance
        #Encapsulation
        #Polymorphism
        #Abstraction

#parent class ( base class)

#child class ()


#Inheritance 

# class Person:
#     def __init__(self, name, surname, birth_year):
#         self.name = name
#         self.surname = surname
#         self.birth_year = birth_year
#     def get_fullname(self):
#         return f'{self.name} - {self.surname}'
#     def get_age(self):...
# #override
# class Student(Person):
#     def __init__(self, name, surname, birth_year, class_number):
#         Person.__init__(self, name, surname, birth_year)
#         self.class_number = class_number

    
# class Teacher(Person):
#     def __init__(self, name, surname, birth_year, work_experience):
#         Person.__init__(self, name, surname, birth_year)
#         self.work_experience = work_experience

# student1 = Student('Ali', 'Aliyev', 2000, '8B')
# print(student1.name, student1.birth_year)
# print(student1.get_fullname())

# teacher1 = Teacher('Nermin', 'Aliyev', 1980, 15)
# print(teacher1.name, teacher1.work_experience)
# print(teacher1.get_fullname())

#Polymorphism

class Animal:
    def sound(self):
        print('Every animal has sound')
    
class Dog(Animal):
    def sound(self):
        print( 'Haw haw')
    
class Cat(Animal):
    def sound(self):
        print('Miyaw Miyaw')
        
dog1 = Dog()
dog1.sound()

cat1 = Cat()
cat1.sound()

animal = Animal()
animal.sound()