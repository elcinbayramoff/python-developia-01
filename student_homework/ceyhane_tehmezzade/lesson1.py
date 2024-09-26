#tapshiriq1

# x1=float(input("x1:"))
# x2=float(input("x2:"))

# y1=float(input("y1:"))
# y2=float(input("y2:"))

# kvadratlar_cemi=(x2-x1)**2+(y2-y1)**2
# import math
# cavab=math.sqrt(kvadratlar_cemi)
# print("Netice:",cavab)

#tapshiriq2

# a=int(input("Ededi daxil edin:"))
# reqem1=a%10
# reqem2=(a//10)%10
# reqem3=a//100

# print(reqem3,",",reqem2,",",reqem1)

# a="Tehmezzade"
# print(a[5])     #z
# print(a[3:6])   #mez
# print(a[ :7])   #Tehmezz
# print(a[2:-3])  #hmezz
# print(a[1:4:2])  #em
# print(a[4:1:-1]) #ehm

#Stringlerun toplanmasi

# a="Ceyhane"
# b="Tehmezzade"
# c1=a+b     
# c2=a+" "+b 
# print(c1)   #CeyhaneTahmezzade
# print(c2)   #Ceyhane Tahmezzade

#Stringlerin deyisdirilmesi

# a="excell"  #'c'-ni 't'ile evez edek
# Deyisdirilmis_a=a[ :2]+"t"+a[3: ]
# print(Deyisdirilmis_a)  #cavab: extell

#Sringlerin formatlasdirilmasi

# a=int(input("Ededi daxil edin:"))

# txt=f'hello{12}' #hello12
# print(txt)

# qiymet=35
# endirim=0.10
# sert=f'Qiymeti {qiymet*endirim} AZN-dir.'
# print(sert)  #Qiymeti 3.5 AZN-dir.


#Replace funksiyasi

# a='Lesson'
# modified_a=a.replace("s","c")
# print(modified_a)   #leccon


# print("world".capitalize()) #World
# print("world".upper())  #WORLD
# print("WORLD".titler())   #world
# print("World".swapcase())  #wORLD

#string metodlari

# print("hesablamalar".find("hesablamalar")) #10   
# print("hesablamalar".rindex("b"))  #4
# print("hesablamalar".replace("b","l"))  #hesallamalar
# print("hesablamalar".count("l"))   #2


# a=[3,1,4,5,6,2,7,8]
# a.sort()
# a[2:6]=sorted(a[2:6],reverse=True)
# print(a)