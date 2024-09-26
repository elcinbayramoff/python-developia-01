#For dovru

# a="Salam"
# for adi in a:
#    print(adi)

# a="Python"
# for i in a:
#     print(i)

# herf="Azerbaycan"
# for i in herf:
#     print(i)

# b=[10,20,30,40,50]
# for i in b:
#     print(i)

# _____________________________________________________________________

#RANGE() funksiyasi

# for eded in range(15):
#     print(eded)

# for i in range (3,10):
#     print(i)

# for i in range(1,10,3):
#     print(i)


  
# for eded in range(1,7,3):
#     eded+=1
#     print(eded)

# for eded in range(10):
#     print(eded)

# cem=0
# for eded in range(15):
#    if eded %2==1:
#       cem+=1
#       print(cem)

#5-den 15-e qeder cut ededler

# for i in range(5,15):
#     if i %2 ==0:
#         print(i)

#1-den 20-e qeder tek ededler

# for eded in range (1,15):
#     if eded % 2==1:
#         print(eded)

# for eded in range(20):
#     if eded % 2==0:
#         print(eded)

#0-dan 25-e qeder cut ededlerin cemi
# cem=0
# for eded in range(25):
#     if eded%2==0:  #2+0=2, 4+2=6, 6+6=12, 8+12=20 ......
#         cem+=eded
#         print("Cem:", cem)

#7-den 21-e qeder tek ededlerin cemi 21 de daxil olmaqla
# cem=0
# for eded in range (7,22):
#     if eded%2==1:
#         cem+=eded
#         print("Cem:",cem)
#1-den 15-e qeder cut ededlerin cemi 15 de daxil olmaqla
# cem=0
# for i in range(1,16):
#     if i %2 == 0:
#         cem+=i
#         print("Cem:",cem)

#1-den 15-e qeder tek ededlerin cemi 15 de daxil olmaqla

# cem=0
# for i in range(1,16):
#     if i %2==1:
#         cem+=i
#         print("Cem:",cem)

#-----------------------------------------------------------

#BREAK verilmis iterasiyada daxilinde oldugu dovru tamamile dayandirir

# for i in range (10):
#     if i==4:
#         break
#     print(i)

# for i in range (4,20):
#     if i ==11:
#         break
#     print(i)


#continue- Verilmiş iterasiyada dövr daxilində
#özündən sonrakı sətrləri keçərək növbəti iterasiyaya
#başlayır.

# for i in range (10):
#     if i==4:
#         continue
# print(i)



# for i in range (24):
#     if i ==21:
#         continue
#     print(i)

#-------------------------------------------------------------
# a="python"
# for herf in a:
#     print(herf)
#     if herf =="h":
#         break

# a=("Kitab", "Defter", "Qelem")
# for i in a:
#     print(i)
#     if i =="Defter":
#         break

  #pass- Əsasən, kod blokunu müvəqqəti olaraq boş
#buraxmaq üçün istifadə edilir, iterasiyaya təsir etmir  
# for i in range(7):
#     pass
#     print(i)
#------------------------------------------------------


#WHILE dovr
#"Hello World" yazisini 10 defe ekrana cixarin
# a=0
# while a <10:
#     print("Hello World")
#     a+=1



#2- den 7-e kimi ededleri ekrana cixarin
# i=2
# while i <8:
#     print(i)
#     i+=1

# 1den 10a kimi ededler
# i=1
# while i <11:
#     print(i)
#     i+=1
    

# i=0
# while i < 15:
#     i += 1
#     if i ==6:
#         continue
#     print(i)

# i=0
# while i<10:
#     i+=1
#     if i ==7:
#         continue
#     print(i)

# a=3
# while a< 13:
#     a+=1
#     if a==12:
#         continue
#     print(a)

# 
#Olar
# i = 1
# while i < 6:
#     print(i)
#     i +=1



# while True:
#     print("Python")
#--------------------------------
#Tapsiriq 1
#Ededin regemlerinin sayini tapin
# a=23456
# i =0 
# while a >0:
#     a=a//10
#     print(a)
#     i+=1

# a=1236
# saygac=0
# while a>0:
#     a=a//10
#     print(a)
#     saygac+=1






