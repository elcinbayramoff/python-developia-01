# import pandas as pd

# a = [1, 7, 2]

# myvar = pd.Series(a, index = ['a','b','c'])
# print(myvar)
# my_dict = {
#       'a1' : 1,
#       'b1' : 7,
#       'c1' : 2
#   }
# myvar1 = pd.Series(my_dict)
# print(myvar1)

# import pandas as pd

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories, index = ["day1", 'day2'])

# print(myvar)

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# my_data = pd.DataFrame(data)
# print(my_data)
# print(my_data.loc[[0,1,2]])


#Task1

# def find_even_numbers(my_list: list):
#     even_list = []
#     for i in my_list:
#         if i % 2 == 0:
#             even_list.append(i)
#     return even_list

# data = [1,3,5,7]
# print(find_even_numbers(data))

#Task2
# lessons = {}
# while True:
#     subject = input('Fenni daxil edin(exit): ')
#     if subject == 'exit':
#         result = 0
        
#         for i in lessons.values():
#             result += i
#         ortalama = result / len(lessons.values())
        
#         print('Ortalama: ', round(ortalama, 2))
#         break
    
#     grade = float(input('Qiymeti daxil edin: '))
#     lessons[subject] = grade
    
    
#Task 3
# employee1 = {'name':'Ali', 'salary':1000}
# employee2 = {'name':'VAli', 'salary':800}
# employee3 = {'name':'Vasif', 'salary':1000}
# employee4 = {'name':'Asif', 'salary':500}
# employee5 = {'name':'Agasif', 'salary':1000}

# A = [employee1, employee2, employee3, employee4, employee5]
# max_salary = -1
# max_items = []
# for employee in A:
#     if employee['salary'] > max_salary:
#         max_items.clear()
#         max_salary = employee['salary']
#         max_items.append(employee)
#     elif employee['salary'] == max_salary:
#         max_items.append(employee)
# print(max_items)

# print(max_items['name'])



import pandas as pd

data = pd.read_excel('pandas_module/datas2.xlsx')

# for k, v in data.items():
#     print(k)

# data.loc[4]

# data_f = data.to_dict('records')

# data_fn = data['Age']

# data_s = data.sort_values('First Name', ascending=False)

# print(data_s)

# data_a = data[data['Age']==32]
# print(data_a)
