'''numune.1'''
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     @staticmethod
#     def adult(age):
#         return age > 18
    
# p1=Person('Ali',24)
# print(p1.name,p1.age)
# print(Person.adult(24))
    

'''numune.2'''
# from datetime import date
# class Person:
#     def __init__(self,name,age): 
#         self.name=name
#         self.age=age
        
#     @classmethod
#     def age_calculation(cls,name,dogumili):
#         return cls(name,date.today().year - dogumili)

# p1=Person.age_calculation('ali',2007)
# print(p1.name)      
# print(p1.age)




'''numune.3'''
# class Cars:
#     def __init__(self,car_name,model):
#         self.car_name=car_name
#         self.model=model
    
# class Favcar(Cars):
#     def __init__(self, car_name, model,color):
#         Cars.__init__(self,car_name, model)
#         self.color=color

# car1=Favcar('dodge challenger','srt hellcat','grey')

# print(car1.car_name)
# print(car1.color)
# print(car1.car_name,car1.model,car1.color)



'''numune.4'''
# class Car1:
#     def func(self):
#         print('dodge challenger')
# class Car2:
#     def func(self):
#         print('bmw')
# class Car3:
#     def func(self):
#         print('mercedes')

# cars=[Car1(),Car2(),Car3()]

# for i in cars:
#      i.func()

# class Car:
#     def func(self):
#         print('Something')

# class BMW(Car):
#     def __init__(self, model) -> None:
#         super().__init__()
#         self.model = model
#     def func(self):
#         print(self.model)

# class Mercedes(Car):
#     def __init__(self, model) -> None:
#         super().__init__()
#         self.model = model
#     def func(self):
#         print(self.model)
        
# b1 = BMW('123')
# m1 = Mercedes('456')
# cars = [b1, m1]

# for i in cars:
#     i.func()