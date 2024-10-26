import random


#Random

# print(random.random()) #0.7023237798395706

# Randint
# random_eded = random.randint(-2, 2) # [-2, 2]
# print(random_eded)

# uniform

# random_eded = random.uniform(2, 6) # 3.8724422761302146
# print(random_eded)

#Shuffle
# A = [1, 2, 3, 4, 5]

# random.shuffle(A)

# print(A)

#Choice
# A = [1, 2, 3, 4, 5]

# rand_elemnt = random.choice(A)

# print(rand_elemnt)

# A = [1, 2, 3, 4, 5]

# rand_elementler = random.choices(A, k=2)

# print(rand_elementler)
# import random
# def zer():
#     a = random.randint(1, 6)
#     b = random.randint(1, 6)
#     return [a, b]

# zerler = zer()
# print(f'Zer 1: {zerler[0]}, Zer 2: {zerler[1]}')


# import random

# def card_generator(n=10):
#     cards = []
    
#     for i in range(n):
#         card = random.sample(range(1, 31), k=7)
#         cards.append(card)
        
#     return cards

# cards = card_generator()

# players = ['Ceyhane', 'Shefeq', 'Rufet', 'Dilek', 'Dalga', 'Demir', 'Reshad', 'Raul']

# # for i in range(len(players)):
# #     print(players[i],cards[i])
# user_input = input('Type end to stop: ')
# cixmis_ededler = []

# while user_input!='end':
#     eded = random.randint(1, 30)
#     if eded not in cixmis_ededler:
#         cixmis_ededler.append(eded)
#         print('Eded: ', eded)
        
#         if len(cixmis_ededler) == 30:
#             print('Oyun bitdi')
#             break
        
#         user_input = input('Type end to stop: ')
#     else:
#         continue

# import random

# def taskagit():
#     A = ['Tas', 'Kagit', 'Makas']
#     player1 = random.choice(A)
#     player2 = random.choice(A)
#     print('Player1: ', player1, 'Player2: ', player2)
#     if player1 == 'Tas' and player2 == 'Kagit':
#         print('Player 2 qalib')
#     elif player1 == 'Tas' and player2 == 'Makas':
#         print('Player 1 qalib')
#     elif player1 == 'Kagit' and player2 == 'Tas':
#         print('Player 1 qalib')
#     elif player1 == 'Kagit' and player2 == 'Makas':
#         print('Player 2 qalib')
#     elif player1 == 'Makas' and player2 == 'Tas':
#         print('Player 2 qalib')
#     elif player1 == 'Makas' and player2 == 'Kagit':
#         print('Player 1 qalib')
        
# taskagit()


import random
# A = [random.randint(1,5) for i in range(10)]
# print(A)
# A = []
# for i in range(10):
#     A.append(random.randint(1,5))
# print(A)

# A = [random.randint(1,5) for i in range(10)]
# print(A)



#TASKSSSS
#TASK1
# import random

# n = int(input("Sayi daxil edin: "))

# A = [random.randint(1,20) for i in range(n)]
# print("Esas list: ", A)

# print("Sortlanmis: ", sorted(A))

#Task2


# n = int(input("Uzunlugu daxil edin: "))

# A = [random.randint(0,100) for i in range(n)]
# print(A)
# cem = sum(A)

# ededi_orta = cem/n

# print('Ededi orta: ', ededi_orta)

#Task3

# import string

# boyuk_herf = string.ascii_uppercase
# kicik_herf = string.ascii_lowercase
# reqem = string.digits
# umumi = boyuk_herf + kicik_herf + reqem

# def password_generator():
#     A = [random.choice(umumi) for _ in range(4)]
#     print(A)
#     password = ''.join(A)
#     reqem_var, kicik_var, boyuk_var = False, False, False
    
#     for i in password:
#         if i in reqem:
#             reqem_var = True
#         if i in kicik_herf:
#             kicik_var = True
#         if i in boyuk_herf:
#             boyuk_var = True
    
#     if reqem_var and kicik_var and boyuk_var:
#         return password
    
#     else:     
#         return password_generator()

# print(password_generator()) # AkxR2Xk8

#Task4 


# random_eded = random.randint(1, 30)
# a = int(input('1 30 arasi eded daxil edin: '))

# while True:
    
#     if a == random_eded:
#         print("Qazandiniz")
#         break 
#     elif a < random_eded:
#         print('Yuxari eded daxil edin: ')
#         a = int(input('1 30 arasi eded daxil edin: '))
#     else:
#         print('Asagi eded daxil edin: ')
#         a = int(input('1 30 arasi eded daxil edin: '))

#Tasks
# import random

# n = int(input('Sayi daxil edin: '))
# A = []
# while len(A) != n:
#     rand_eded = random.randint(1,n) 
#     print(rand_eded, A)
#     if rand_eded not in A:
#         A.append(rand_eded)
# print(A)





