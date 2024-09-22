# Tapşırıq 1

eli = int(input("Əlinin yaşını daxil edin: "))
ekrem = int(input("Əkrəmin yaşını daxil edin: "))

if eli > ekrem:
    print("Əli böyükdür.")
elif eli < ekrem:
    print("Əkrəm böyükdür.")
else:
    print("Əli və Əkrəm eyni yaşdadır.")



# Tapşırıq 2

iscinin_yasi = int(input("İşçinin yaşını daxil edin: "))

if 25 <= iscinin_yasi <= 40:
    print("Uyğundur.")
else:
    print("Uyğun deyil.")



# Tapşırıq 3

eded = int(input("Ədədi daxil edin: "))

if eded % 2 == 0:
    print("Cütdür.")
else:
    print("Təkdir.")
