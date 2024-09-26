# 1

# number = int(input("Ədədi daxil edin: "))

# cem = 0

# while number > 0:
#     reqem = number % 10  
#     cem += reqem
#     number = number // 10  

# print("Rəqəmlərin cəmi:", cem)



# 2

# number = int(input("Ədədi daxil edin: "))

# qonsu_var = False

# reqem1 = number % 10
# number = number // 10

# while number > 0:
#     reqem2 = number % 10  
#     if reqem2 == reqem1:  
#         qonsu_var = True
#         break  
#     reqem1 = reqem2  
#     number = number // 10  

# if qonsu_var:
#     print("Ədəddə iki qonşu rəqəm bərabərdir.")
# else:
#     print("Ədəddə iki qonşu rəqəm bərabər deyil.")



# 3

number = int(input("Ədədi daxil edin: "))

a, b = 0, 1

print("Fibonacci ədədləri:")
while a <= number:
    print(a, end=" ")
    a, b = b, a + b
