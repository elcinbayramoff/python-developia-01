# import pandas
# mydataset={
#     'cars':['bmw','volvo','ford'],
#     'passings':[3,7,2]
# }
# myvar=pandas.DataFrame(mydataset)
# print(myvar)

# myvar1=pandas.Series(mydataset)
# print(myvar1)




# import pandas as pd
# a=['1','7','2']
# myvar=pd.Series(a)
# print(myvar)


# import pandas as pd
# a=['1','2','3','4']
# myvar=pd.Series(a)
# print(myvar)


# import pandas as pd
# a=['1','7','2']
# myvar=pd.Series(a,index=['x','y','z'])
# print(myvar)
# print(myvar['y'])


# import pandas as pd
# calories={'day1':420,'day2':380,'day3':390}
# myvar=pd.Series(calories)
# print(myvar)
# myvar1=pd.Series(calories,index=['day1','day3'])
# print(myvar1)




# import pandas as pd
# data={

#     'calories':[420,380,390],
#     'duration':[50,40,45]
# }
# df=pd.DataFrame(data)
#print(df)
#print(df.loc[0])
#print(df.loc[[0,2]])




# import pandas as pd
# data={
#     'calories':[420,380,390],
#     'duration':[50,40,45]
# }

# df=pd.DataFrame(data,index=['day1','day2','day3'])
# print(df)
# print(df.loc['day2'])



# with open('data.json','w')as file:
#     file.write('aaaa')


# import pandas as pd
# df=pd.read_csv('data.json')
# new_df=df.dropna()
# print(new_df.to_string())



# import pandas as pd
# df=pd.read_csv('data.json')
# df.dropna(inplace=True)
# print(df.to_string)
