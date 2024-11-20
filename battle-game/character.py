from weapons import hand, Weapon

class Character:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.max_health = health
        self.defaul_weapon = hand
        self.weapon: Weapon = weapon
        
    def attack(self, target):
        target.health -= self.weapon.damage
        print(f'{self.name} {target.name}-e {self.weapon.damage} qeder zerer yetirdi')
    
    def show_hp(self):
        return f'{self.name} - {self.health}/{self.max_health}'      #Hero - 80/100

    def is_alive(self):
        return self.health > 0


class Hero(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health, weapon)
    
    def equip(self, weapon):
        prev_weapon = self.weapon
        self.weapon = weapon
        print(f'{self.name} silahını {prev_weapon.name}-dan {self.weapon.name}-a deyisdi')
    
    def drop(self):
        prev_weapon = self.weapon
        self.weapon = self.defaul_weapon
        print(f'{self.name} silahını {prev_weapon.name}-dan {self.weapon.name}-a deyisdi')
    
class Enemy(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health, weapon)
        