#Tapsiriq 1

number = int(input("Bir ədəd daxil edin: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"{number}-in faktorialı:", factorial)



#Tapsiriq 2

n = int(input("Fibonacçi ardıcıllığı üçün bir ədəd daxil edin: "))

a, b = 0, 1
for _ in range(2, n+1):
    a, b = b, a + b

print(f"Fibonacçi ardıcıllığındakı {n}-ci elementi:", b)


#Tapsiriq 3

a = int(input("Bir ədəd daxil edin: "))
sade = True

if a < 2:
    sade = False
else:
    for i in range(2, a):
        if a % i == 0:
            sade = False
            break

if sade:
    print(f"{a} sadə ədəddir.")
else:
    print(f"{a} sadə ədəd deyil.")
