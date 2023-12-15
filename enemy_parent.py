# Main enemy class
# Contains attributes such as Intro talk, health, resistances, damage dealt, when health reaches 0 encounter ends and player exp increased
import random
class Enemy():
    # Setting base stats of enemy
    melee_resist = 10
    spell_resist = 10
    holydamage = 10
    spelldamage = 10
    meleedamage = 10
    holy_resist = 10
    
    def __init__(self):
        self.hp = random.randrange(50,100) # enemy spawns with random health between 50 and 100
        

