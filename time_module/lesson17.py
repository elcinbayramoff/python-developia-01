import datetime

#date - Il ay Gun
#time - Saat deqiqe saniye millisaniye
#datetime - Il Ay Gun Saat Deqiqe saniye millisaniye
#timedelta - Deyisme

from datetime import date

# a = date(2024,10,5) # il ay gun 
# print(type(a))

now = date.today()

# # print(now)
# print(now.year)
# print(now.month)
# print(now.day)

# print(type(now))

# a = date.fromtimestamp(3456000000)
# print(a)
# now = date.today()
# # print(now)
# print(now.strftime('%d.%m.%Y')) # 26.10.2024
# from datetime import date
# import time
# gun = int(input("Gunu daxil edin: "))
# ay = int(input("Ayi daxil edin: "))
# il = int(input("Ili daxil edin: "))

# a = date(il, ay, gun)
# # time.sleep(10)
# print(a.strftime("%A")) 


# from datetime import time
# a = time(hour=23,minute=25,second=12)
# print(a)
# a = time(12, 50,  45)
# print(type(a.isoformat()))

# print(a.hour,a.minute,a.second, a.microsecond)


from datetime import datetime

# now = datetime.now()
# print(now)
# a = datetime(2024,10,5,12,10,5,111)
# print(a)
# a = '15-10-2024 13:25:45'

# b = datetime.strptime(a, '%d-%m-%Y %H:%M:%S')
# print(b.hour)

#strftime - datetime obyektini alir, lazim olan hissesini qaytarir
#neticesi datetime obyektidir.


#strptime     
from datetime import datetime
# my_date = '26 January 2024' # 2024 Jan, 26
# format_date = '%d %B %Y'
# datetime_version = datetime.strptime(my_date, format_date)
# print(datetime_version.strftime('%Y %b, %d'))

#Istifadeciden gun ay il formatinda daxil etmesini isteyirik
# 21/10/2024 - Bu formati datetime obyektine cevir ve 2024, Oct 21, Wed
# date_str = input('Daxil et: ')
# my_format = '%d/%m/%Y'

# date_datetime = datetime.strptime(date_str, my_format)
# print(date_datetime.strftime('%Y, %b %d, %a'))