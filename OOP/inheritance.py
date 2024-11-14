#Inheritance:
#       Single
#       Multiple
#       Multilevel inheritance
#       Hierarchial inheritance
#       Hybrid inheritance


#Base class, Parent class
#Child class



#
# class Person: # Base, Parent
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
        
#     def get_fullname(self):
#         return f'{self.name} {self.surname}'

# class Student(Person): #child class
#     def __init__(self, name: str, surname: str, age: int, status: bool):
#         super().__init__(name, surname, age)
#         self.status = status

#     def get_fullname(self):
#         return f'{self.surname} {self.name}'
    
    
# student1 = Student('Ali','Aliyev', 18, True)
# self.name -> student1.name
# print(student1.name)
# print(student1.surname)
# print(student1.status)
# print(student1.get_fullname())

#Inheritance:
#       Single + 
#       Multiple 
#       Multilevel inheritance
#       Hierarchial inheritance
#       Hybrid inheritance


#Grandparent
#Parent
#Child

#Multiple inheritance
# class Parent1:
#     def greet(self):
#         print('It is Parent1')

# class Parent2:
#     def welcome(self):
#         print('It is Parent2')

# class Child(Parent1, Parent2):
#     def func(self):
#         print('It is Child')
        
# child1 = Child()
# child1.greet()
# child1.welcome()
# child1.func()

# class Par1:
#     def greet(self):
#         print('It is Parent1')

# class Parent2:
#     def greet(self):
#         print('It is Parent2')

# class Child(Par1, Parent2):
#     def welcome(self):
#         # Parent1.greet(self) #Olmazz
#         super().greet()
#         print('It is Child')
        
# Child -> Parent1 -> Parent2
# child1 = Child()
# child1.welcome()
# child1.greet()
# MRO - Method Resolution Order 
# print(Child.mro())
#super()



#Multilevel

# class GrandParent:
#     def greet1(self):
#         print('It is Grand')
        
# class Parent(GrandParent):
#     def greet2(self):
#         print('It is Parent')

# class Child(Parent):
#     ...

# child1 = Child()
# # print(Child.mro())
# child1.greet1()
# child1.greet2()


#Hierarchial inheritance

# class Parent:
#     def greet(self):
#         print('It is Parent')
    
# class Child1(Parent):
#     def func1(self):
#         print('It is ch1')

# class Child2(Parent):
#     def func2(self):
#         print('It is ch2')
    
# child1 = Child1()
# child1.greet()
# child1.func1()


# child2 = Child2()
# child2.greet()
# child2.func2()


# class A:
#     def greet(self):
#         print('A')

# class B(A):
#     pass

# class C(A):
#     pass

# class D(C):
#     pass

# class E(B, D):
#     pass

#B A D C A
#B D C A 
#Eger C A-dan inheritance gotururse [<class '__main__.E'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
#Eger C A-dan inheritance goturmurse [<class '__main__.E'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.D'>, <class '__main__.C'>, <class 'object'>]
#MRO E -> Class E, Class B, Class A, Class D, Class C
# print(E.mro())
# e = E()
# e.greet()