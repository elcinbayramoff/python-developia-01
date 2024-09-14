# Tapşırıq 1

massiv = [4, 2, 1, 5, 7, 3, 6, 8]

massiv.sort()

middle = len(massiv) // 2
massiv[middle-2:middle+2] = massiv[middle-2:middle+2][::-1]

print(massiv)


# Tapşırıq 2

isci_siyahisi = []

ad1 = input("1-ci işçinin adını daxil edin: ")
soyad1 = input("1-ci işçinin soyadını daxil edin: ")
ad_soyad1 = ad1 + " " + soyad1
isci_siyahisi.append(ad_soyad1)

ad2 = input("2-ci işçinin adını daxil edin: ")
soyad2 = input("2-ci işçinin soyadını daxil edin: ")
ad_soyad2 = ad2 + " " + soyad2
isci_siyahisi.append(ad_soyad2)

ad3 = input("3-cü işçinin adını daxil edin: ")
soyad3 = input("3-cü işçinin soyadını daxil edin: ")
ad_soyad3 = ad3 + " " + soyad3
isci_siyahisi.append(ad_soyad3)

isci_nomresi = int(input("Neçənci işçini görmək istəyirsiniz? ")) - 1

print(f"Seçdiyiniz işçi: {isci_siyahisi[isci_nomresi]}")


# Tapşırıq 3

def polindrom_yoxlayan(lst):
    return lst == lst[::-1]

list1 = [1, 2, 2, 2, 1]
list2 = [5, 4, 5, 4, 5]
list3 = [9, 8, 7, 6, 5]

print(f"{list1} polindromdur? {polindrom_yoxlayan(list1)}")
print(f"{list2} polindromdur? {polindrom_yoxlayan(list2)}")
print(f"{list3} polindromdur? {polindrom_yoxlayan(list3)}")


# Tapşırıq 4

my_list = [1, 2, 3, 4, 5]

new_list = my_list[::-1]

print(new_list)
