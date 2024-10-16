#Yeni insan.txt fayli yaradin və içi
# ----------------------------------------------------------------

#Insan1
#Insan2

'''
a - Faylin içindəkiləri silmir, sadəcə sonuna əlavə edir
w - Faylın içindəkiləri silir, yeni datanı yazır.
r(default) - Sadəcə Faylları oxumaq üçündür
x - Sadəcə faylları yaratmaq üçündür.
'''
'''
f = open('insan.txt','a') # Icindekileri silmir
f.write('Insan1')
f.close()
'''
# f = open('insan.txt','w') # Icindekileri silir tezden yazir
# f.write('Insan1')
# f.close()

#MUTLEQ FILE ACANDAN SONRA BAGLAAA
# f = open('insan.txt','w') # Icindekileri silir tezden yazir
# f.write('Insan1\nInsan2')
# f.close()


# f = open('insan.txt','r')
# f.seek(2)
# data = f.read()
# print(f.tell())
# data = f.readlines() #['Insan1\n', 'Insan2\n', 'Insan3']
# print(f.tell())
# for i in data:
#     print(i.strip('\n'))


# f = open('insan.txt', 'w+')
# f.write('Salam Insan')
# print(f.tell())#Kursorun harda oldugunu deyir
# f.seek(3)
# print(f.tell())
# print(f.read())
# print(f.tell())
# f.close()

# f = open('insan.txt', 'w+')
# f.write('Salam Insan Necesen')
# f.seek(0)
# data = f.read()
# f.seek(0)
# data = data[:6] + 'Ozel ' + data[6:]
# f.write(data)

# f.close()

#t - text
#b - binary

# f = open('insan.txt','r')
# print(str(f))
"""
w - write
r - read
a - append
x - Fayllari yaratmaq
w+ - 
r+ -

"""
"""
t - text
b - binary
"""
# file = open('insan.txt','w+')

# file.write("Salamlari her kese")

# print(file.read())

# file.close()



# f = open('insan.txt', 'w+')
# f.write('Salam Insan')
# f.seek(0)
# data = f.read()
# print(data)
# f.close()

# f = open('insan.txt', 'w+')
# data = f.read()
# print(data)
# f.seek(0)
# f.write('Salam Insan')
# f.close()


# #Task1
# f = open('new.txt', 'w')
# f.write('Hello World')
# f.close()

#Task2

# f = open('data.txt') # default read(r)

# data = f.readlines()
# print(data)
# for i in range(len(data)):
#     print(i+1,"------", data[i])

# f.close()

#Task3
# f = open('data.txt') 
# data = f.read()
# f.close()

# file = open('data_copy.txt', 'w')
# file.write(data)
# file.close()

#Task4
# f = open('insan.txt', 'r')
# data = f.read()

# data1 = data.split()

# print(len(data1))
