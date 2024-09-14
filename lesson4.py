#Listlerin deyisilmesi

# A = ["alma", "armud", "heyva", "ananas"]

# A[0:2] = ["nar","ciyelek"]
# print(A)

# A = ["alma", "armud", "heyva", "ananas"]

# A[0:2] = ["nar"]
# print(A)

# A = [10, 30, 50, 70]

#insert
# A.insert(2,40)
# print(A)

#append()
# A.append(80)
# print(A)

#extend
# A=[1,2,3]
# B=[4,5,6]
# B.extend(A)
# print(B)

#Toplama
# A=[1,2,3]
# B=[0]

# C = A+B
# print(C)

#Element silinmesi

#remove
# A = ["A","B","C","D"]
# A.remove("C")
# print(A)

#pop
# A.pop()
# print(A)

#del

# del A[0]

#Sorting
# A= [3,1,2,5]
# print(A.sort())
# print(A)
# print(sorted(A))
# print(A)

# A= [3,1,2,5]
# A1 = sorted(A[0:2])
# A2 = A[2:]
# A = A1 + A2

# print(A)

# A.sort(reverse=True)
# print(A)

# A.reverse()
# print(A)


#Tapsiriq
# [4,2,1,5,7,3,6,8] # List sortlanacaq, daha sonra ortadaki 4 eded tersine sortlanacq
# [1,2,6,5,4,3,7,8] # Netice

# a = [1, 2, 3, 4]
# b = [4, 3, 2, 1]
# b.reverse()
# print(a == b)

#1 tapsiriq
# A =[3,1,4,5,6,2,7,8]
# A.sort()#[1,2,3,4,5,6,7,8]

# A[2:6] = sorted(A[2:6],reverse=True)
# print(A)


#2 tapsiriq

# main_list = []

# isci1_ad = input("1.Adi daxil edin:")
# isci1_soyad = input("1.Soyadi daxil edin: ")
# main_list.append([isci1_ad,isci1_soyad])

# isci2_ad = input("2.Adi daxil edin:")
# isci2_soyad = input("2.Soyadi daxil edin: ")
# main_list.append([isci2_ad,isci2_soyad])

# isci3_ad = input("3.Adi daxil edin:")
# isci3_soyad = input("3.Soyadi daxil edin: ")
# main_list.append([isci3_ad,isci3_soyad])
# num = int(input("Necenci? ")) #num=1
# print(main_list)
# print(main_list[num-1]) #main_list[0]

#Tapsiriq polindrome

# A = [1,2,2,1] # [4,3,2,1]

# print(A == A[::-1])

#Kopyalama
import copy
A = [[1,2],[3,4]]
B = copy.deepcopy(A) # [1,2,3,4]
A[0][0] = 5

print(A)
print(B)
