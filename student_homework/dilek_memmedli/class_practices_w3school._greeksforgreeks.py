# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# person1=Person('john',36)
# print(person1.name)
# print(person1.age)



# class Person:
#     def __init__(self,name,age): 
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name}({self.age})"
# p1=Person("john",36)
# print(p1)



# class Person:
#     def _init_(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(self):                               #burda self evezine basqa seylerde yaza bileerik
#         print('hello my name is'+self.name)
# p1=Person('john',36)
# p1.myfunc() 



# class Dog:
#     attr1='mammal'
#     attr2='dog'

#     def fun(self):
#         print('i am dog',self.attr1)
#         print('i am dog',self.attr2)

# Rodger=Dog()
# print(Rodger.attr1)
# Rodger.fun()



# class GFG:
#     def __init__(self,name,company):
#         self.name=name
#         self.company=company
#     def show(self):
#         print('hello my name is '+self.name+' and i work in '+self.company+'.')

# obj=GFG('john','greeksforgreeks')
# obj.show()




# class Person:
#     def __init__(self,name):
#         self.name=name
#     def f(self):
#         print('my name is '+self.name)
# p1=Person('dilek')
# p1.f()



# class GFG:
#     def __init__(self,name,company):
#         self.name=name
#         self.company=company
#     def __str__(self) :
#         return f"my name is {self.name} and i work in {self.company}." 
# obj=GFG('john','greeksforgreeks')
# print(obj)



# class dog:
#     animal='dog'

#     def __init__(self,breed,color):

#         self.breed=breed
#         self.color=color

# rodger= dog('pug','brown')
# buzo=dog('bulldog','black')

# print('rodger details:')
# print('rodger is a ' ,rodger.animal)
# print('breed:',rodger.breed)
# print('color:',rodger.color)




class Dog:
    animal='dog'

    def __init__(self,breed):
        self.breed=breed

    def setColor(self,color):
        self.color=color
    def getColor(self):
        return self.color
rodger=Dog('pug')
rodger.setColor('brown')
#print(rodger.getColor())


