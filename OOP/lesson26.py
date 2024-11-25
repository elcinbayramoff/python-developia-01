class Product:
    def __init__(self,category: str, name: str, price: float):
       self.category = category
       self.name = name
       self.price = price
    
    def __repr__(self):
        return f'[{self.category}]- {self.name}'


class Person:
    def __init__(self, name: str, surname: str, age: int, citizen: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.citizen = citizen 

            
class Shop:
    def __init__(self, name: str, location: str, owner: Person, products: list = []):
        self.name = name
        self.location = location
        self.owner = owner
        self.products = products
        self.__balance = 0
    
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount.")
    
    def add_product(self, product: Product):
        self.products.append(product)
        
    def discard_product(self, product: Product):
        self.products.remove(product)
        
    def buy_product(self,product: Product):
        if self.__balance < product.price:
            print('Balans kifayet deyil')
            return
        self.add_product(product)
        self.__balance -= product.price
            
    def sell_product(self,product: Product):
        if product not in self.products:
            print('Belə məhsul yoxdur')
            return
        self.discard_product(product)
        self.__balance += product.price + product.price * self.percentage          

class ElectronicShop(Shop):
    product_categories = ['computer', 'phones', 'headphones']
     
    def __init__(self, name: str, location: str, owner: Person, percentage: float, products: list = []):
        super().__init__(name, location, owner, products)
        self.percentage = percentage
        
class FoodShop(Shop):
    product_categories = ['meals', 'drinks', 'snacks']
    
    def __init__(self, name: str, location: str, owner: Person, percentage: float, products: list = [], ):
        super().__init__(name, location, owner, products)       
        self.percentage = percentage
        
class ClothShop(Shop):
    product_categories = ['trousers', 'shirts', 'hats']
    
    def __init__(self, name: str, location: str, owner: Person, percentage: float, products: list = [], ):
        super().__init__(name, location, owner, products)  
        self.percentage = percentage


person1 = Person('Ali','Aliyev',30,'azerbaijani')

product1 = Product('phones', 'Telefon', 120)
product2 = Product('drinks', 'Süd',1.20)
product3 = Product('shirts', 'Qısaqol', 25)

clothshop1 = ClothShop('Newyorker', 'Baki', person1, 1)
clothshop1.add_product(product2)
clothshop1.add_product(product1)

# print(clothshop1.products)
clothshop1.sell_product(product1)
clothshop1.buy_product(product3)
print(clothshop1.balance)
print(clothshop1.products)
# print(shop1._Shop__balance)
        
#1-ci hisse 
'''
Product
- category
- name
- price

Person
- name
- surname
- citizen
- age
'''

#2-ci hisse 
'''
Shop 
 - name
 - location
 - products = []
 - owner 
annotasiya
'''

#3-cu hisse
'''
add_item()
discard_item()
balance = 

'''