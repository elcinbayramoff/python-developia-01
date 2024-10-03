main_list = [1, 3, 5, 6, 1, 3, 7]

yeni_list=[]

for i in main_list:
    if i not in yeni_list:
        yeni_list.append(i)

print(main_list)
print(yeni_list)