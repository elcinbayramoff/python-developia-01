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


