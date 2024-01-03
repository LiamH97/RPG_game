# Main enemy class
# Contains attributes such as Intro talk, health, resistances, damage dealt, when health reaches 0 encounter ends and player exp increased
import random
class Enemy():
    def __init__(self, melee_resist = 10, spell_resist = 10, holy_resist = 10,holydamage = 10,spelldamage = 10,meleedamage =10):
    # Setting base stats of enemy
        self.melee_resist = melee_resist
        self.spell_resist = spell_resist
        self.holydamage = holydamage
        self.spelldamage = spelldamage
        self.meleedamage = meleedamage
        self.holy_resist = holy_resist
        self.hp = random.randrange(50,100) # enemy spawns with random health between 50 and 100

# Creating the ORC class:
# Increased damage taken from spell
# Deals Melee damage
# Reduced damage from melee
# No change on holy damage
        
class Orc(Enemy):
    def __init__(self):
        super().__init__()
        self.spell_resist *= .9
        self.meleedamage *= 1.1
        self.melee_resist *= 1.1