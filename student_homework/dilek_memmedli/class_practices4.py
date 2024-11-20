# class Isciler:
#     def __init__(self,name,surname,age):
#         self.name=name 
#         self.surname=surname
#         self.age=age
#     def show_info(self):
#         print(f'ad:{self.name}  soyad:{self.surname}   age:{self.age}')

# Isci1=Isciler('ali','aliyev','30') 
# print(Isci1.name)

# Isci1.show_info()




#class variables-instance variable

# class Isci:
#     zam=1.1
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary


# isci1=Isci('ali','1000')
# isci1.zam=1.2

# print(isci1.__dict__)
# print(Isci.__dict__)
# print(Isci.zam)
# print(isci1.zam)



# class Isciler:
#     isci_sayi=0
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         Isciler.isci_sayi+=1

# print(Isciler.isci_sayi)
    
# isci1=Isciler('ali',1000)
# #print(isci1.name)

# print(Isciler.isci_sayi)





# class Person:
#     say=0
#     def __init__(self,name,surname,age):
#         self.name=name
#         self.surname=surname
#         self.age=age
#         Person.say+=1

#     def show_info(self):   #instance method
#         return f"ad: {self.name}  soyad:{self.surname}"
    
# p1=Person('ali','aliyev',30)

# print(p1.show_info())
# print(Person.show_info(p1))

# print(Person.say)



#classmethodu/staticmethod

# from datetime import date
# class Person:
#     def __init__(self,name,age) :
#         self.name=name
#         self.age=age


#     @classmethod
#     def calculation(cls,name,birth_year):
#         return cls(name,date.today().year - birth_year )
#     @staticmethod
#     def adult(age):
#         return age>18

    
# p1=Person.calculation('ali',1999)
# print(p1.name,p1.age)


# print(Person.adult(20))





#inheritance
# class calisan:
#     zam=1.1
#     def __init__(self,isim,soyisim,maas):
#         self.isim=isim
#         self. soyisim=soyisim
#         self.maas=maas
#         self.mail= isim+soyisim+'@sirket.com'
#     def show_info(self):
#         return "ad:{}  soyad:{}  maas:{}  mail:{}".format(self.isim,self.soyisim,self.maas,self.mail)
    

# c1=calisan('ali','aliyev',5000)
# c2=calisan('veli','veliyev',6000)

# class yazilimci(calisan):
#     ##zam=1.2self.isim=isim
#     def __init__(self, isim, soyisim, maas,dil):
#         super().__init__(isim, soyisim, maas)
    
#         self. soyisim=soyisim
#         self.maas=maas
#         self.mail= isim+soyisim+'@sirket.com'
#         self.dil=dil
#     def show_info(self):
#         return "ad:{}  soyad:{}  maas:{}  mail:{} dil:{}".format(self.isim,self.soyisim,self.maas,self.mail,self.dil)
    
# y1=yazilimci('ayse','ayseyev',7000,'python')
# print(y1.mail)

# print(c1.zam)
# print(y1.zam)


# print(c1.show_info())
# print(y1.show_info())
# print(y1.dil)
# print(y1.show_info())








