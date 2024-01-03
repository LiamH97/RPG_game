# Main enemy class
# Contains attributes such as Intro talk, health, resistances, damage dealt, when health reaches 0 encounter ends and player exp increased
import random
class Enemy():
    def __init__(self, melee_resist = 10, spell_resist = 10, holy_resist = 10,holydamage = 10,spelldamage = 10,meleedamage =10):
    # Setting base stats of enemy
        self.melee_resist = melee_resist
        self.spell_resist = spell_resistttt
        self.holydamage = holydamage
        self.spelldamage = spelldamage
        self.meleedamage = meleedamage
        self.holy_resist = holy_resist
        self.hp = random.randrange(50,100) # enemy spawns with random health between 50 and 100

## Creating the ORC class:
# Increased damage taken from spell
# Deals Melee damage
# Reduced damage from melee
# No change on holy damage
        
class Orc(Enemy):
    def __init__(self):
        super().__init__()
        self.spell_resist *= .9
        self.meleedamage *= 1.3
        self.melee_resist *= 1.1

## Creating the Troll class:
# Increased damage taken from melee
# Deals Melee damage - Face to face style fighting but has significant damage bonus from melee and reduced resistane to melee 
# Reduced damage from spells
# No change on holy damage
class Troll(Enemy):
    def __init__(self):
        super().__init__()
        self.melee_resist *= .8
        self.meleedamage *= 1.2
        self.spell_resist *= 1.1

## Defining Undead class
#Undead are vunerable to holy, have higher spell resist, no impact on melee
# Undead deal spell damage 
class Undead(Enemy):
    def __init__(self):
        super().__init__()
        self.spelldamage *= 1.3
        self.spell_resist *= 1.1
        self.holy_resist *= .7
