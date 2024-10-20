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