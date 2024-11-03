import json
#Loads
# json_data = '{"name":"Elchin", "married":false}'

# python_data = json.loads(json_data)

# print(python_data)
# print(python_data['name'])

#Dumps

python_data = {
    'surname':'Bayramli',
    'name':"Elchin",
    'married' : False
}

# json_data = json.dumps(python_data)
# print(type(json_data))

# json_data = json.dumps(python_data, indent=4)
# print(json_data)

# json_data = json.dumps(python_data, indent=4, separators=['/','-'])

# print(json_data)

# json_data = json.dumps(python_data, indent=4, sort_keys=True)
# print(json_data)



#dump()

# data = '{"name":"Elchin","surname":"Bayramli", "age":66, "married":false}'
# python_data = json.loads(data)

# with open('data.json','w') as f:
#     json.dump(python_data, f, indent=4)

#load()

# with open('data.json') as f:
#     data = json.load(f)

# print(data['married'])


# data = {
#  "name": "Elçin",
#  "surname": "Bayramli",
#  "age": 66,
#  "married": False
# }

# with open('data.json','w', encoding='UTF-8') as f:
#     json.dump(data, f, indent=4, ensure_ascii=False)

data = {
 "name": "Elçin",
 "surname": "Bayramli",
 "age": 66
}
# with open('data.json', 'w', encoding='UTF-8') as f:
#     json.dump(data,f, indent=4,ensure_ascii=False)

# with open('data.json') as f:
#     data = json.load(f)
    
# with open('data.json', 'w') as f:
#     data['married'] = False
#     json.dump(data, f, indent=4, ensure_ascii=False)
# data = {
#  "name": "Elçin",
#  "surname": "Bayramli",
#  "age": 66
# }
    
# with open('data.json', 'w+', encoding='UTF-8') as f:
#     json.dump(data,f, indent=4,ensure_ascii=False)
#     f.seek(0)
#     data = json.load(f)

# with open('data.json', 'w') as f:
#     data['married'] = False
#     json.dump(data, f, indent=4, ensure_ascii=False)
    