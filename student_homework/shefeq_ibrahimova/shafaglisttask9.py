# #Task1
# a = [1,3,5,6,8,9]
# for i in a:
#     print(i) 

#Task2
a = list(input("daxil et:"))
print(a)

#Task3
# a = [1,180,180,190,190,6]
# count=0
# say = 0
# for i in a:
#     if i==190:
#         count+=1
#     if i == 180:
#         say +=1
# print(count,say)

#Task4
# a = input("daxil et:").split()
# b =[]
# for i in a:
#     if a.count(i)>1:
#         b.append(i)
# if len(b)==0:
#     print("tekrarlanan element yoxdur")
# else:
#     print("tekrarlanan element var")

#Task5
# a=[1,2,6,7,4,8,9,1,4,3,2,7]
# en_boyuk=a[0]
# for i in a:
#     if i>en_boyuk:
#         en_boyuk=i
# print(en_boyuk)

#Task6
# a=[1,2,6,7,4,81,9,12,1,4,3,2,7,10]
# en_boyuk=a[0]
# for i in range(0,len(a)):
#     if a[i]>en_boyuk:
#         en_boyuk=a[i]
# print(a.index(en_boyuk))

#Task7
# a=[1,2,6,7,4,8,9,1,4,3,2,7]
# en_boyuk=a[0]
# en_kicik=a[0]
# for i in a:
#     if i>en_boyuk:
#         en_boyuk=i
#     if i<en_kicik:
#         en_kicik=i
# print(en_boyuk,en_kicik)

#Task8

#Task 9
# a = [1,-3,6,-9,2,-7,8]
# menfi=[]
# musbet =[]
# for i in a:
#     if i>0:
#         musbet.append(i)
#     if i<0:
#         menfi.append(i)
# print(musbet,menfi)

#Task10
# a = [2,-4,1,-6,8,-2]
# for i in a:
#     if i%2==0 and i<0:
#         print(i)

#Task11

#Task12
# sait="aiouüöıeə"
# a = input("soz daxil et:")
# sait_say=0
# samit_say=0
# for i in a:
#     if i in sait:
#         sait_say+=1
#     else:
#         samit_say+=1
# print(sait_say,samit_say)

