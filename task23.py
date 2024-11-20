class Computer:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    
    
    def __str__(self):
        return f"{self.marka} {self.model}"

class Laptop(Computer):
    def __init__(self, marka, model, pil_ömrü):
        super().__init__(marka, model) 
        self.pil_ömrü = pil_ömrü 
        
    def use_battery(self, amount: int):
        # if self.pil_ömrü < amount:
        #     raise ValueError('Daxil etdiyiniz qiymet pil omrunden coxdur')
        
        self.pil_ömrü -= amount
        self.pil_ömrü = max(self.pil_ömrü, 0)
        
    
    def __str__(self):
        return f"{self.marka} {self.model} pilömrü: {self.pil_ömrü}"
    
computer = Computer("msi", "katana")
print(computer)  

laptop = Laptop("casper", "excalibur", 24)
print(laptop)   

laptop.use_battery(10)
print(laptop)
