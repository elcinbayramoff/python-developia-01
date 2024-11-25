try:
    a = int(input("Cut eded daxil edin: "))
    
    if a % 2 == 1:
        raise ValueError('Tek eded daxil etdiniz')
    
    print('Dogru daxil etdiniz')
    
except Exception as e:
    raise ValueError(e)



# raise ValueError('Eded daxil edin')