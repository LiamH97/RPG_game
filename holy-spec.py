# Child class of hero
# Increased holy damage
# Heal ability with CD of 3 turns
from hero import Hero
class Holy(Hero):
    Hero.holy_damage = Hero.holy_damage * 1.1