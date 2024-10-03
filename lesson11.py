x = 5  #global
y = 10 #global
def outer():
    x = 10 # enclosing
    print("Inside Outer 1:")
    print("X:",x,"Y:",y)
    def inner():
        # nonlocal x
        x = 20 #local scope
        y = 3  #local scope 
        print("Inside inner 1:")
        print("X:",x,"Y:",y)
        
    inner()
    print("Inside outer 2:")
    print("X:",x,"Y:",y)
outer()
print("Inside Global:")
print("X:",x,"Y:",y)    


# def func1(a,b,c=40): # c=40 defaul arqument
#     print(a,b,c)
    
    
# func1(1, 2, c = 5) # c=5 -> keyword argument, 1 və 2 positional

#Tapsiriq1
# import math
# def area(radius):
#     area_value = math.pi * radius ** 2
#     print(area_value)

# area(2)

#keyword-only *

# def func2(*,a, b):
#     print(a,b)
    
# # func2(1, 3) # olmazzz
# func2(a=1, b=3) # olarrr

#positional-only /

# def func3(a, b,/):
#     print(a,b)

# # func3(a=3, b=5) # olmazzz
# func3(1, 5) # olarrr


#İki ədəd positional-only, 1 ədəd keyword-only arqument tələb edən, 
# 1 ədəd default parametr alan bir funksiya yazın. Nəticə olaraq daxil 
# edilmiş bütün parametrləri ekrana çıxarın.

# def task2(a, b, /,d=40, *, c):
#     print(a,b,d,c)

# task2(1, 2, 5, c=20)

# *args arbitrary arguments
# def kids(kid1, kid2,*usaqlar): # args
#     print(kid1)
#     print(kid2)
#     print(usaqlar)
    
# kids('A','B','C','D','E','F','G','H')

# **kwargs arbitrary keyword arguments


# def kids(kid1, *usaqlar1, **usaqlar2):
#     print(kid1)
#     print(usaqlar1)
#     print(usaqlar2)
    
# kids('A', 'C', 'D', kid2='B')    


# def kids(kid1, *args, **kwargs):
#     print(kid1)
#     print(args)
#     print(kwargs)
    
# kids('A', 'C', 'D', kid2='B')    


#Task3

# def task3(*args): # args=(1, 3, 5)
#     for i in args:
#         print(i)
        
# task3(1, 3, 5)

# def task3(**kwargs): # kwargs={'name':'Ali','surname':'Valiyev'}
#     for key,value in kwargs.items():
#         print(key,value)
        
# task3(a=1, b=3, c=5)


# #return 

# def cem(a, b):
#     netice = a + b
#     return netice
    
# def ededi_orta(cemleri, sayi):
#     result = cemleri / sayi
#     return result

# cem1 = cem(5,8)
# ededi_orta1 = ededi_orta(cem1, 2)

# print(ededi_orta1)

# def cem(a, b):
#     netice = a + b
#     return netice
#     print(a,b)# Icra edilmir

# cem1 = cem(5,8)
# print(cem1)

# def ededler():
#     for i in range(5):
#         if i == 3:
#             return i
#         print(i)
        
# eded = ededler()
# print("Eded",eded)



#Global Scope
# def esas():
#     #Enclosing scope
#     #
#     #
#     # 
#     def asili():
#         #Local scope
#         pass
#     #
#     #
#     asili()

# esas()