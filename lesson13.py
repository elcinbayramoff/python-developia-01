#Exception handling
# 5 / 0


# try:
#     5 / 0 # olmaz
    
# except:
#     print('Error- 0-a bölmək olmaz')


# try:
#     5 / 0 # olmaz
    
# except ZeroDivisionError:
#     print('Error- 0-a bölmək olmaz')






#Exceptions

#Try - except 

#Try - except - else

# try:
#     print(5 / 2) # olar
    
# except:
#     print('Error- 0-a bölmək olmaz')
    
# else:
#     print('İşlədi')



#Try - except - else - finally

# try:
#     print(5 / 2) # olar
    
# except:
#     print('Error- 0-a bölmək olmaz')
    
# else:
#     print('Try işləyərsə işləyəcək')
# finally:
#     print('Həmişə işləyəcək')

# try:
#     print(5 / 0) # olar
    
# except:
#     print('Error- 0-a bölmək olmaz')
    
# else:
#     print('Try işləyərsə işləyəcək')
# finally:
#     print('Həmişə işləyəcək')




#Checking 2 exceptions

# try:
#     a = int(input("Birinci eded: "))
#     b = int(input("Ikiinci eded: "))
#     a.upper()
#     print(a / b)
    
# except ZeroDivisionError:
#     print('Error- 0-a bölmək olmaz')
    
# except ValueError:
#     print('Eded daxil etmelisiniz!')

# except:
#     print('Error var')

#Checking multiple exceptions at the same time
# try:
#     a = int(input("Birinci eded: "))
#     b = int(input("Ikiinci eded: "))
#     print(a / b)
    
# except (ZeroDivisionError, ValueError):
#     print('Ya 0-a bolmusan ya Deyer xetasi var')
    



#Common Python exceptions

#ValueError str int
...
#TypeError str + int
# try:
#     a = 'Salam'
#     b = 4
#     print(a + b)
# except TypeError:
#     print('Stringle sadece string toplanir')

#IndexError
# try: 
#     A = [1, 2, 3]

#     print(A[7])
# except IndexError:
#     print('Index dogru deyil')

#KeyError
# try:
#     my_dict = {
#         'a':5,
#         'b':7
#     }

#     my_dict['c']

# except KeyError:
#     print('Bele acar soz yoxdur')


#ZeroDivisionError
...
#AttributeError

# try:
#     a = 12
#     a.upper()
# except AttributeError:
#     print('Bele metod yoxdur ve ya dogru daxil edilmeyib')

#Exception as e

# try:
#     a = 12
#     a.upper()
# except AttributeError as e:
#     print(e)

# try:
#     a = 12
#     a = a + 'Salam'
# except Exception as e:
#     print(e)

#raise

# raise AttributeError('Duz deyil')

# def bolme(a, b):
#     if b == 0:
#         raise ZeroDivisionError('0-a BOLME!!!!')
    
#     else:
#         print(a/b)

# bolme(4, 0)

#annotation

# def annotate(a: str, b: str):
#     a = a.lower()
#     b = b.upper()
#     print(a, b)

# annotate('Salam', "Sagol")
# b = 'Salam'

# a: str = b

