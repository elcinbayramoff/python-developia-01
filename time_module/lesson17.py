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


# Tasks

#Task1
#27.10.2024 09:11

# from datetime import datetime

# now = datetime.now()
# formatted_now = now.strftime('%d.%m.%Y %H:%M')

# print(formatted_now)

#Task2

# from datetime import date, timedelta

# today = date.today()

# after_5 = today + timedelta(days=5)
# before_5 = today - timedelta(days=5)

# print(today,'\n',after_5,'\n',before_5)

#Task3

# from datetime import date

# ramazan = date(2025, 2, 28)
# today = date.today()

# diff = ramazan - today

# print(diff.days)

#Task4

# from datetime import date
# import random
# A = []
# today = date.today()
# date_format = "%d %B %Y"
# for i in range(5):
#     # if today.month in ay_30:
#     #     day_limit = 30
#     # elif today.month in ay_31:
#     #     day_limit = 31
#     # else:
#     #     day_limit = 29
    
#     a = date(today.year, today.month,random.randint(1, 28))
#     print(a.strftime(date_format))


#Task5

import random
from datetime import datetime, timedelta,date
now = datetime.now()


while True:
    
    user = input('Imtahan tarixini gün-ay-il formasında daxil edin: ')
    date_obj = datetime.strptime(user, '%d-%m-%Y')
    if date_obj > now:
        print("\nDoğru daxil edildi. İndi isə görüş vaxtını təyin edin")
        weeks = 3
        while True:
            date_tom = date_obj + timedelta(weeks=weeks)
            print('\n',date_tom)
            user = input('Uygundur/Uygun deyil: ')  
            if user == 'Uygundur':
                print("\nGörüş təyin edildi.")
                print(date_tom.strftime('%d %B %Y, %A'))
                break
            else:
                weeks+=1
                print("\nYeni görüş vaxtı:")
        break
    
    else:
        print('\nNövbəti günlərdən biri olmalıdır.')  