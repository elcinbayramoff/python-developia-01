# A = "Salam"

# for herf in A: 
#     print(herf)

#range()

# for eded in range(0,10,2): # 0 2 4 6 8
    
#     print(eded)
    
    
# for icinde if istifadesi

# cem = 0
# for eded in range(10):#0,1,2,3,4,5,6,7,8,9
#     if eded % 2 == 0:
#         cem += eded #cem=0 + 0 = 0 + 2 = 2 + 4 = 6 + 6 = 12 + 8 = 20

# print(cem)

# 0-dan 15-e kimi tek ededlerin sayini tapin
# say = 0
# for eded in range(15):#0,1,2,3, 4, ...,13,14
    
#     if eded % 2 == 1:#1 3 5 7 9 11 13
#         say += 1 # 0 + 1 = 1 + 1 = 2
        
#     print(say) # 0, 1, 1, 2, 2 
# blok1
#     blok2
#         blok3
#     blok2
#         blok3
#     blok2
# blok1
#break
# for i in range(10):
#     if i == 4:
#         break
#     print(i)
#continue
# for i in range(10):
#     if i == 4:
#         continue
#     print(i)
#pass
# for i in range(10):
#     if i == 4:
#         pass
#     print(i)
        
# for i in range(4):
    
#     for j in range(3):
        
#         print("i:",i,"j:",j)

# for j in range(3):
#     print(j)
#Tapsiriq
# A = [["Eli", "ELiyev"],["Ali","Aliyev"],["Veli","Veliyev"]]



# for i in range(len(A)):#
#     element = A[i]
#     for j in range(len(element)):#
#         print(A[i][j])

# for element in A:
    
#     for j in element:
        
#         print(j, end=" ")
#     print()    

# A = [1, 2, -5, 2, 0 ,-8]

# say = 0
# for i in A:
    
#     if i < 0:
#         say += 1

# print(say)

'''
1 x 1
1 x 2
1 x 3
2 x 1
2 x 2
2 x 3
3 x 1
3 x 2
3 x 3


'''

# for i in range(1,4):
    
#     for j in range(1, 4):
        
#         print(f"{i} * {j} = {i*j}")