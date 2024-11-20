
#Public - Hər kəsə açıq
#Protected - Qorunmuş
#Private - Gizli



# class Person:
#     def __init__(self, name,age, pin_code) -> None:
#         self.name = name # public
#         self._age = age #protected
#         self.__pin_code = pin_code # private

# p1 = Person('Nagi',18, '12345678')
# print(p1._age)
# print(p1.__pin_code) # OLMAZZZ
#Name-mangling
# p1._Person__pin_code = 111111
# print(p1._Person__pin_code)




# class EncapsulationExample:
#     def __init__(self):
#         self.public_var = "I am Public" 
#         self._protected_var = "I am Protected"  
#         self.__private_var = "I am Private"      

#     def show_vars(self):
#         print(f"Public: {self.public_var}")
#         print(f"Protected: {self._protected_var}")
#         # self.__private_var = 'Deyisildim'
#         print(f"Private: {self.__private_var}")

# obj = EncapsulationExample()
# # print(obj._EncapsulationExample__private_var)
# # obj.show_vars()

# print(obj.public_var)  

# print(obj._protected_var)  

# # print(obj.__private_var)  # Raises AttributeError

# print(obj._EncapsulationExample__private_var)  # Allowed, but not recommended


# class BankAccount:
#     def __init__(self, initial_balance):
#         self.__balance = initial_balance  # Private attribute

#     # Getter method
#     def get_balance(self):
#         return self.__balance

#     # Setter method
#     def set_balance(self, amount):
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             print("Invalid balance amount.")


# account = BankAccount(100)
# # print(account.get_balance())  # 100

# account.set_balance(150)
# # print(account.get_balance())  # 150

# account.set_balance(-20)  # Invalid balance amount.
# # account._BankAccount__balance = 'Salam'
# print(account.get_balance()) 
#@property

# class Person:
#     def __init__(self, age):
#         self.age = age

#     @property    
#     def is_adult(self):
#         if self.age > 18:
#             return True
#         else:
#             return False
    
#     def change_age(self):
#         self.age = 25    
    
# p1 = Person(20)
# print(p1.is_adult)







# class BankAccount:
#     def __init__(self, initial_balance):
#         self.__balance = initial_balance
#     # Getter method using @property decorator
#     @property
#     def balance(self):
#         return self.__balance

#     # Setter method using @balance.setter decorator
#     @balance.setter
#     def balance(self, amount):
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             print("Invalid balance amount.")



# # # # Usage
# account = BankAccount(100)
# print(account.balance)  # 100

# account.balance = 150
# print(account.balance)  # 150

# # account.balance = -20  # Invalid balance amount.


# class BankAccount:
#     def __init__(self, initial_balance):
#         self._balance = initial_balance

#     # Define getter function
#     def get_balance(self):
#         return self._balance

#     # Define setter function
#     def set_balance(self, amount):
#         if amount >= 0:
#             self._balance = amount
#         else:
#             print("Invalid balance amount.")

#     # Create a property for balance using property()
#     balance = property(get_balance, set_balance)

# # # Usage
# account = BankAccount(100)
# print(account.balance)  # 100, uses get_balance function

# account.balance = 150   # Uses set_balance function
# print(account.balance)  # 150

# account.balance = -20   # Invalid balance amount.
