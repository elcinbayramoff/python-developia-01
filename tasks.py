#Task9_1
# A = [1, 2, 2, 5,'Salam', True, 4.5]

# #A[0] = 1
# # f"A[{index}] = {dəyər}"

# for i in A:
#     pass

# for i in range(len(A)):
#     index = i
#     value = A[i]
#     print(f"A[{index}] = {value}")

#Task9_2

# length = int(input("Uzunluğu daxil edin: "))
# A = []

# for i in range(length):
    
#     value = int(input(f"A[{i}] = "))
#     A.append(value)

# print(A)

#Task9_3

# A = [170, 200, 190, 220, 250, 180, 190, 180]
# saygac = 0
# for i in A:

#     if i == 180 or i == 190:
#         saygac += 1 
# print("Say:",saygac)
    
    
# for i in range(len(A)):
#     index = i
#     deyer = A[i]

# Task 9_4
#Variant1
# A = [1, 2, 3, 2, 5]
# eyni_varmi = False
# for i in range(len(A)):

#     for j in range(i+1,len(A)):
#         print(A[i], A[j])
#         if A[i] == A[j]:
#             eyni_varmi = True
#             break
# if eyni_varmi == True:
#     print("Eyni var")
# else:
#     print('Eyni yoxdu')

#Variant2

# A = [1, 2, 3, 5]
# set_A = set(A)
# set_A = list(set_A)

# if A == set_A: # Eyni eded yoxdur
#     print("Eyni yoxdur")
# else:
#     print("Eyni var")

# Task 9_5

# A = [1, 2, 5, 3, 7, 9, 1]

# max_eded = A[0]

# for i in A:
#     if i > max_eded: 
#         max_eded = i # max_eded = 9
# print(max_eded)

# # max_eded = max(A)
# # print(max_eded)

# Task 9_6

# A = [1, 2, 5, 9, 3, 7, 9, 1]

# max_eded = A[0]

# for i in A:
#     if i > max_eded: 
#         max_eded = i # max_eded = 9
# print(A.index(max_eded))

# Task 9_7

# A = [1, 2, 5, -3, -5, 9, 3, 7, 9, 1]

# min_eded = A[0]

# for i in A:
#     if i < min_eded: 
#         min_eded = i # min_eded = -5
# print(min_eded)


# Task 9_8

# A = [1,2,3,4,5,6]

# A_1 = A[:len(A)//2]
# A_2 = A[len(A)//2:]

# A_1.sort(reverse=True)
# A_2.sort(reverse=True)

# A = A_1 + A_2
# print(A)

#Task9_9

# A = [1, -2, 5, -3,0,  -5, 9, 3, 7, 9, 1]
# A_musbet = []
# A_menfi = []

# for i in A:
#     if i > 0:
#         A_musbet.append(i)
#     elif i < 0:
#         A_menfi.append(i)
#     else:
#         pass

# A = A_menfi + A_musbet
# print(A)

#Task9_10

# A = [1, -2, 5, -3,0,-6,  -5, 9, 3, 7, 9, 1]

# for i in A:
#     if i < 0 and i % 2 == 0:
#         print(i)

#Task9_11

# a = int(input("Eded daxil et: "))
# sadedirmi = True

# for i in range(2, a): #a % a = 0 range(2, 2) hec bir netice qaytarmir
#     if a % i == 0:
#         sadedirmi = False
#         break
# print(sadedirmi)

#Task9_12

# soz = input('Sozu daxil edin: ') # Salam

# sait_saygac = 0
# samit_saygac = 0

# saitler = 'aeoiu'
# samitler = 'qwrtypsdfghjklzxcvbnm'

# for i in soz:
#     if i.lower() in saitler:
#         sait_saygac += 1
#     elif i.lower() in samitler:
#         samit_saygac += 1
# print("Saitler:",sait_saygac,"Samitler:",samit_saygac)

#Task10_2
# DATABASE = {
# 'username' : 'aysuceferova',
# 'password' : 'aysu123'
# }
 
#Asan

# ad = input('Adi daxil edin: ')
# kod = input('Kodu daxil edin: ')

# if ad != DATABASE['username'] or kod != DATABASE['password']:
#     print('Dogru melumatlar daxil edilmedi')
    
# else:
#     print("Giris edildi")

#orta

# ad = input('Adi daxil edin: ')
# kod = input('Kodu daxil edin: ')

# while ad != DATABASE['username'] or kod != DATABASE['password']:
#     print('Dogru melumatlar daxil edilmedi')
    
#     ad = input('Adi daxil edin: ')
#     kod = input('Kodu daxil edin: ')
# print('Giris edildi')

#Task10_3

# '''
# *
# * *
# * * *
# * * * *

# '''

# length = int(input("Uzunlugu daxil edin: "))

# for i in range(1, length+1):
#     print('*'*i)