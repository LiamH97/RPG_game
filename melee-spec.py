# Child class of hero
# Increased melee damage
# Powerful melee ability with CD of 3 turns
from hero import Hero
class Melee():
    Hero.melee_damage = Hero.melee_damage * 1.1
    
