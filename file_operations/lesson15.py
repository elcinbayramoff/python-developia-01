
# file = open('data.txt', 'r+')
# print(file.read()) 
# file.close()

# with open('data.txt', 'r+') as file: # İçindəkiləri saxlayır
#     print(file.read()) 

# a = ["1", "2", "3", "4",'5']    
# with open('data.txt', 'w+') as file: # İçini təmizləyir
#     file.writelines(a) 

# with open('data.txt', 'r+') as file:
#     print(file.read(5)) # İlk 5 simvolu oxuyur


# with open("data.txt", "r") as file:
#     data = file.readlines()
#     print(data)
#     for line in data:
#         print(line)


# Write ready functions to perform basic operations with files

# data = ['Bugün', 'şəhərə','gedirik']

# with open('data.txt', 'w') as file: #cd file_operations
#                                     #cd ..
#     file.writelines(data)

#Task
#Istifadəçi faylın adını və içinə yazılacaq
# datanı verir. Funksiya yazın və bu 
# əməliyyatı yerinə yetirin.

# def task(file_name, file_data):
#     with open(file_name, 'w') as file: 
#         file.write(file_data)
# name = input('Faylin adini daxil edin: ')
# data = input('Faylin datasini daxil edin: ')
# task(name, data)
# Faylın adını daxil edin: data1.txt
# Datanı daxil edin: Hello world



# -------------------------OS module ----------------------------------------

# import os

# if os.path.exists("data.txt"):
#     print("File exists!")
# else:
#     print("File does not exist.")
    
# import os

# os.mkdir("new_folder1") # Yeni folder yaratmaq  - makedirectory


# import os # Noqte oldugun yeri gosterir

# fayllarim = os.listdir(".") # list directories
# for i in fayllarim:
#     print(i)


import os

current_dir = os.getcwd() # get current working directory
print('--------',current_dir,'-------------------')


# import os

# os.chdir("new_folder") # change directory
# print('0--------------',os.getcwd())


# import os

# os.remove("data_copy.txt")

    
# import os

# if os.path.isfile("lesson14.py"):
#     print("It's a file!")
# else:
#     print("It's not a file.")
    
    
# import os

# if os.path.isdir("lesson14.py"):
#     print("It's a directory!")
# else:
#     print("It's not a directory.")
    
    
# import os

# file_size = os.path.getsize("insan.txt")
# print(file_size, "bytes")



# import os

# full_path = os.path.join("new folder",'main_dir')
# print(full_path)

# import os

# base_name = os.path.basename("/path/to/file.txt")
# print(base_name)  # Output: "file.txt"


# import os

# dir_name = os.path.dirname("/path/to/file.txt")
# print(dir_name)  # Output: "/path/to"
