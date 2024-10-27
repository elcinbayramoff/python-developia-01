#Task1

# import os

# if os.path.exists('file_operations/insan123.txt'):
#     with open('file_operations/insan123.txt', 'r') as f:
#         data = f.read()
#         print(data)

# else:
#     print('Fayl movcud deyil')
        
#Task2

# def write_to_txt(file_name, data: list):
#     with open(file_name, 'w') as file:
#         for i in data:
#             file.write(f'{i}\n')
        
# A = ['a', 'b', 'c', 'd', 'e', 'f']
# write_to_txt('file_operations/new.txt',A)  


#Task3

# soz = input('Sozu daxil edin: ')

# with open('file_operations/new.txt') as f:
#     data = f.read()

# if soz == data:
#     print('Dogru texmin etmisiniz.')
# else:
#     print('Yanlisdir')