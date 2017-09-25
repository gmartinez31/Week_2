#!/usr/bin/env python
# In this simple RPG game, the hero fights the goblin. He has the options to:
# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
from random import uniform

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    #maybe? if name == "Zombie": alter health code?
    def alive(self):
        return self.health > 0
            
    def attack(self, enemy):
        enemy.health -= self.power
        if enemy.health <= 0:
            print("{} took {} damage from {}!".format(enemy.name, self.power, self.name))
            print("{} killed the {}!".format(self.name, enemy.name))
        else:    
            print("{} took {} damage from {}!".format(enemy.name, self.power, self.name))
    
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))
        


class Hero(Character):
    def __init__(self):
        super().__init__('Hero', 10, 5)
        while self.attack:
            random_num = int(uniform(1,10))
            if random_num <= 2:
                self.power *= 2
                break

class Goblin(Character):
    def __init__(self):
        super().__init__('Goblin', 6, 2)
        

class Medic(Character):
    def __init__(self):
        super().__init__('Medic', 8, 4)

    def damage_received(self, enemy):
        random_num2 = int(uniform(1,10))
        if random_num2 <= 2 and enemy.attack:
            self.health += 2
            print("Medic gained +2 health!")


class Shadow(Character): #right now this is set to 10% hit rate on Shadow instead of having it getting hit every 10 turns. Alter that with a counter.
    def __init__(self):
        super().__init__('Shadow', 1, 4)

    def damage_received(self, enemy):
        # incomplete and incorrect code for receiving damage one out of ever ten times
        # counter = 0
        # while counter:
        #     counter += 1
        #     if counter < 10:
        #         enemy.attack = False
        #         print('Shadow took no damage!')

        #     elif counter = 10:
        #         return enemy.attack
        #     else:
        #         pass
        #         break

        # code for 10% chance of getting hit. This one works but only for the inital, enemy attack. Fix that.
        random_num = int(uniform(1,10))
        if random_num <= 1:
            return enemy.attack
        else:
            enemy.attack = False;
            print('Shadow took no damage!')

# class Zombie(Character):
#     def __init__(self):
#         super().__init__('Zombie', #infinte health, power)
        
medic = Medic()
hero = Hero()
goblin = Goblin()
shadow = Shadow()

def fight():
    print()
    print("Choose your Fighter! ")
    print("(a) Hero ")
    print("(b) Goblin ")
    print('(c) Medic ')
    print('(d) Shadow ')
    fighter = input('')
    actfighter = str(fighter)
    if actfighter.lower == 'a':
        return main(hero, goblin)
    elif fighter.lower == 'b':
        return main(goblin, hero)
    elif fighter.lower == 'c':
        return main(medic, goblin)
    elif fighter.lower == 'd':
        return main(shadow, goblin)
    else:
        print("Invalid input {}".format(fighter))

def main(fighter1, rival):
    while fighter1.alive() and rival.alive():
        fighter1.print_status()
        rival.print_status()
        print()
        print("What do you want to do?")
        print("1. fight")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            fighter1.attack(rival)
        elif raw_input == "2":
            #do nothing
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if rival.health > 0:
            # Goblin attacks hero
            rival.attack(fighter1)  #<-- this will not work for shadow code so might have to make a diff function for that
            #instead it would be shadow.damage_received.(rival or fighter depending on input selection)           
fight()