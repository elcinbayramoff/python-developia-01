from character import Character, Hero, Enemy
from weapons import sword, bow, hand


hero = Hero('Hero', 100, sword)
enemy = Enemy('Enemy', 100, bow)

while True:
    print('\n------------------------------------------')
    print(hero.show_hp())
    print(enemy.show_hp())
    
    hero.attack(enemy)
    enemy.attack(hero)
    if not hero.is_alive():
        print(f'{enemy.name} qazandi')
        break
    
    if not enemy.is_alive():
        print(f'{hero.name} qazandi')
        break
    
    change_weapon = input(f'1.Qılınc 2. Ox 3. Əl\n')
    if change_weapon:
        if change_weapon == '1':
            hero.equip(sword)
        elif change_weapon == '2':
            hero.equip(bow)
        elif change_weapon == '3':
            hero.drop()
