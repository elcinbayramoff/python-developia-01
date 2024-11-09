#Task1

# A = ['Salam', 'Mənim', 'Adım', 'Əlidir']
# # a = '/'.join(A)
# # print(a)
# A = [i +' ' for i in A]

# with open('exam-2/data1.txt', 'w+', encoding='UTF-8') as f:
#     f.writelines(A)
#     f.seek(0)
#     data = f.read()

# with open('exam-2/data2.txt', 'w+', encoding='UTF-8') as f:
#     data = data.split()
#     data_new = ','.join(data)
#     f.write(data_new)


#Task2

# import pandas as pd
# import json
# df = pd.read_excel('employee.xlsx', usecols=['EEID','Full Name', 'Job Title', 'Department'])

# # for k,v in df.items():
# #     print(v)
# DATABASE = {}

# for i in range(10):
#     a = {
#         'full_name': df.loc[i]['Full Name'],
#         'job_title': df.loc[i]['Job Title'],
#         'department': df.loc[i]['Department']
#     }
#     eeid = df.loc[i]['EEID']
#     DATABASE[eeid] = a
    
    
# data = json.dumps(DATABASE,indent=4)
# print(data)

#Task3
# star_count = None
# for i in range(13):
    
#     if i <= 2:
#         star_count = 5
#         print('* ' * star_count)
#     if 2< i <= 6:
#         star_count -= 1
#         print('* ' * star_count)
#     if 6< i <= 9:
#         star_count += 1
#         print('* ' * star_count)
    
#     if 9 < i <= 12:
#         star_count = 5            
#         print('* ' * star_count)

#Task4
# import json

# DICTIO = {
#     'come' : 'gel',
#     'book' : 'kitab',
#     'pen' : 'qelem'
# }
# try:
#     user = input('Sozu daxil edin(ingilisce): ')
#     print(DICTIO[user])
# except KeyError:
#     print('Lugetde yoxdur')
    
# with open('exam-2/data.json', 'w+', encoding='UTF-8') as f:
#     json.dump(DICTIO, f, indent=4, ensure_ascii=False)

#Task5
from datetime import datetime
A = []
format1 = '%d.%m.%Y'
while True:
    user = input('Date-i daxil edin(exit): ')
    if user == 'exit':
        for date_str in A: # 15.10.2024
            date1 = datetime.strptime(date_str, format1)
            date_f = datetime.strftime(date1, '%Y, %B %d, %a')
            print(date_f)
        
        
        break

    A.append(user)
