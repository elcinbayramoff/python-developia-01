import random

class Character:
    def __init__(self, name, health, coins, skills, location=None):
        self.name = name
        self.health = health
        self.coins = coins
        self.skills = skills
        self.weapon: Weapon = None
        self.armor: Armor = None
        self.location = location

    def attack(self, target):
        if self.weapon:
            damage = self.weapon.damage
            target.take_damage(damage)
            print(f"{self.name} attacks {target.name} with {self.weapon.name} for {damage} damage!")
        
        elif self.weapon.range < abs(self.location-target.location):
            print(f"{self.name} attacks {target.name} with {self.weapon.name} but target is too far")
        
        else:
            print(f"{self.name} has no weapon to attack with!")

    def take_damage(self, damage):
        if self.armor:
            damage -= damage * self.armor.defense

            damage = max(damage, 0)  # Damage cannot go below 0
        self.health -= damage
        health = max(self.health, 0)
        print(f"{self.name} takes {damage} damage! Health is now {health}.")

    def is_alive(self):
        return self.health > 0

    def equip_weapon(self, weapon):
        if self.coins >= weapon.cost:
            self.weapon = weapon
            self.coins -= weapon.cost
            print(f"{self.name} equipped {weapon.name}. Coins left: {self.coins}")
        else:
            print(f"{self.name} cannot afford {weapon.name}!")

    def equip_armor(self, armor):
        if self.coins >= armor.cost:
            self.armor = armor
            self.coins -= armor.cost
            print(f"{self.name} equipped {armor.name}. Coins left: {self.coins}")
        else:
            print(f"{self.name} cannot afford {armor.name}!")

class Weapon:
    def __init__(self, name, damage, range, cost):
        self.name = name
        self.damage = damage
        self.range = range
        self.cost = cost

class Armor:
    def __init__(self, name, defense, cost):
        self.name = name
        self.defense = defense
        self.cost = cost

# Initialize characters, weapons, and armors
def setup_game():
    characters = [
        Character("Warrior", health=100, coins=100, skills="Charge"),
        Character("Archer", health=80, coins=100, skills="Precision Shot"),
        Character("Mage", health=70, coins=100, skills="Fireball")
    ]

    weapons = [
        Weapon("Sword", damage=20, range=1, cost=50),
        Weapon("Bow", damage=15, range=3, cost=50),
        Weapon("Staff", damage=25, range=2, cost=60)
    ]

    armors = [
        Armor("Shield", defense=10, cost=40),
        Armor("Leather Armor", defense=5, cost=30),
        Armor("Robe", defense=3, cost=20)
    ]

    return characters, weapons, armors

def player_setup(player_name, characters, weapons, armors):
    print(f"Player {player_name}, choose your character:")
    for i, char in enumerate(characters):
        print(f"{i + 1}. {char.name} - Health: {char.health}, Coins: {char.coins}, Skills: {char.skills}")
    choice = int(input("Enter the number of your choice: ")) - 1
    player_character = characters[choice]

    while True:
        print(f"Player {player_name}, choose your weapon:")
        for i, weapon in enumerate(weapons):
            print(f"{i + 1}. {weapon.name} - Damage: {weapon.damage}, Range: {weapon.range}, Cost: {weapon.cost}")
        choice = input("Enter the number of your choice: ")
        if choice == '':
            break
        choice = int(choice) - 1
        player_character.equip_weapon(weapons[choice])

    print(f"Player {player_name}, choose your armor:")
    for i, armor in enumerate(armors):
        print(f"{i + 1}. {armor.name} - Defense: {armor.defense}, Cost: {armor.cost}")
    choice = int(input("Enter the number of your choice: ")) - 1
    player_character.equip_armor(armors[choice])

    return player_character

def battle(player1, player2):
    print(f"\nThe battle begins! {player1.name} vs {player2.name}")
    while player1.is_alive() and player2.is_alive():
        print("\nPlayer 1's turn:")
        player1.attack(player2)
        if not player2.is_alive():
            print(f"{player2.name} has been defeated! Player 1 wins!")
            break

        print("\nPlayer 2's turn:")
        player2.attack(player1)
        if not player1.is_alive():
            print(f"{player1.name} has been defeated! Player 2 wins!")
            break

def main():
    characters, weapons, armors = setup_game()

    print("Welcome to the War Game!")
    player1 = player_setup("1", characters, weapons, armors)
    player2 = player_setup("2", characters, weapons, armors)

    battle(player1, player2)

if __name__ == "__main__":
    main()
