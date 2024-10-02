# my_list = ['Elchin','Bayramli']

# print(my_list[0])
# my_dict = {
#     'name':'Elchin',
#     'surname':'Bayramli'
# }

# print(my_dict['name'])
#constructorlar
#str()
#list()
#tuple()
#dict()
my_dict = {
    'name':'Elchin',
    'surname':'Bayramli',
    'age':10
}
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())#[('name', 'Elchin'), ('surname', 'Bayramli'), ('age', 10)]
# my_dict.clear()

# my_dict.pop('surname')
# print(my_dict)

#popitem()

# my_dict.popitem()
# print(my_dict)
my_dict = {
    'name':'Elchin',
    'surname':'Bayramli',
    'age':10
}
# del

 #item silmek
 
# del my_dict['surname']
# print(my_dict)

#dict-i silmek
# del my_dict
# print(my_dict)


# my_dict = {
#     'name':'Elchin',
#     'surname':'Bayramli',
#     'age':10
# }
# my_dict['uzunluq'] = 180 # yenisini yaratmaq

# print(my_dict)


#KEYS
# for acar in my_dict:
#     print(acar)

# for acar in my_dict.keys():
#     print(acar)

#VALUES
my_dict = {
    'esas yemek':['Hamburger','Doner'],
    'sup':['Tomat','Merce']
}

# for deyer in my_dict.values():
#     print(deyer)

# for key in my_dict: #key = 'name'
#     print(my_dict[key]) #print(my_dict['age'])

#Items
# my_dict = {
#     'name':'Elchin',
#     'surname':'Bayramli',
#     'age':10
# }
# for key, value in my_dict.items(): # ('name', 'Elchin')
#     print("Key:",key,"Value:",value)

# key, value = ('name', 'Elchin')

#Tapsiriq 1

kitabca = {
    'adam1':{
        'name':'Elchin',
        'phone':'12343'
    },
    'adam2':{
        'name':'Veli',
        'phone':'1111'
    },
    'adam3':{
        'name':'ELi',
        'phone':'2222'
    }
}

# for key in kitabca:
#     print(kitabca[key]['phone'])

# for value in kitabca.values():
#     print(value['phone'])

# print(kitabca['adam1']['phone'])

#Tapsiriq2
# a = input("Cümləni daxil edin: ")

# a = a.split()

# #['Salam', 'menim', 'Salam', 'elcindir']
# luget = {

# }
# for word in a:
    
#     if word in luget:
#         luget[word] += 1
#     else:
#         luget[word] = 1
# print(luget)

# {
#     'salam': 2, 
#     'men': 2, 
#     'elcin': 1, 
#     'necesen': 1
# }

# Tapsiriq 3

# luget = {
#     'go' : 'get',
#     'come' : 'gel',
#     'name' : 'ad',
#     'give' : 'ver',
#     'run' : 'qac'
# }
# sentence = input("Cumleni daxil edin: ")

# sentence = sentence.strip()

# sentence_words = sentence.split() #['go','come','name']

# for i in range(len(sentence_words)):
#     soz = sentence_words[i] #go
#     soz_tercume = luget[soz]  # get
#     sentence_words[i] = soz_tercume # ['get','gel','ad']


# tercume_cumle = ' '.join(sentence_words)

# print(tercume_cumle)
    