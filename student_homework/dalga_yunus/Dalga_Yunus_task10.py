# # 1

# main_list = [1, 3, 5, 6, 1, 3, 7]

# new_list = list(set(main_list))

# print(new_list)



# # 2

# DATABASE = {
#     'username': 'aysuceferova',
#     'password': 'aysu123'
# }

# while True:

#     username = input("Username daxil edin: ")
#     password = input("Password daxil edin: ")

#     if username == DATABASE['username'] and password == DATABASE['password']:
#         print("Giriş edildi")
#         break
#     else:
#         print("Məlumatlar yanlış daxil edildi")



# # 3

# length = int(input("Uzunluğu daxil edin: "))

# for i in range(1, length + 1):
#     print('* ' * i)


# # 4

# number = int(input("Ədədi daxil edin: "))

# factorial = 1 

# for i in range(2, number + 1):
#     factorial *= i 

# print(f"Faktorial: {factorial}")



# 5

number = int(input("Ədədi daxil edin: "))

factorial = 1
a = 1
factorialdir = False 

while factorial < number:
    a += 1
    factorial *= a

if factorial == number:
    factorialdir = True
else:
    factorialdir = False

if factorialdir:
    print(f"{a}-ın faktorialıdır.")
else:
    print("Heç bir ədədin faktorialı deyil.")