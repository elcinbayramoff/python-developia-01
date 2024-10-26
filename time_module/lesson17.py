import datetime

#date - Il ay Gun
#time - Saat deqiqe saniye millisaniye
#datetime - Il Ay Gun Saat Deqiqe saniye millisaniye
#timedelta - Deyisme

from datetime import date

# a = date(2024,10,5)
# b = str(5)
# print(type(b))

# now = date.today()

# print(now.year)
# print(now.month)
# print(now.day)

# print(type(now))

# a = date.fromtimestamp(3456000000)
# print(now)
# print(now.strftime('%A'))
# from datetime import date

# gun = int(input("Gunu daxil edin: "))
# ay = int(input("Ayi daxil edin: "))
# il = int(input("Ili daxil edin: "))

# a = date(il, ay, gun)

# print(a.strftime('%H')) 

# from datetime import time

# # a = time(12, 50,  45)
# indi = time(20,51,00)
# print(type(a.isoformat()))

# print(a.hour,a.minute,a.second, a.microsecond)

# print(indi.strftime('%I---- %M '))#08---- 51

from datetime import datetime

# now = datetime.now()
# a = datetime(2024,10, 15, 13, 25, 45)
# print(a)
a = '15-10-2024 13:25:45'

b = datetime.strptime(a, '%d-%m-%Y %H:%M:%S')
print(b.hour)