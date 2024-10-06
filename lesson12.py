#Rekursiya


# def func(a):
#     if a < 1:
#         return
#     print(a)
#     func(a-1)
    
# func(12)

# a = 5 # rekursiyasiz
# b = 1
# for i in range(1, 6):
#     b *= i
# print(b)

def faktorial(a):
    if a <= 1:
        return a
    
    return a*faktorial(a-1)    # 5 * 4 * 3 * 2 * 1

print(faktorial(5))