userin_melumatlari = ["Ilkin", "Ilkin1234"]
username = input("Username'i daxil edin :")
password = input("Password'u daxil edin:")

if userin_melumatlari[0] == username.capitalize() and userin_melumatlari[1] == password:
    print("Giris edildi")
else:
    print("Məlumatlar yanlış daxil edildi")