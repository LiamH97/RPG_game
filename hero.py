#Parent hero class
#Contains attributes for hero:
    #Health
    # Available attacks and damage of each attack
    # EXP/Level - damage incrased by 5% per level
class Hero():
    def __init__(self, health = 300 ,holy_damage = 15,melee_damage = 20,spell_damage = 20,spell_resist = 10,melee_resist = 10):
        self.health = health
        self.holy_damage = holy_damage
        self.melee_damage = melee_damage
        self.spell_damage = spell_damage
        self.spell_resist = spell_resist
        self.melee_resist = melee_resist
#Defining Holy class 
# Increased holy damage
class Holy(Hero):
    def __init__(self,heal):
        super().__init__()
        self.holy_damage *= 1.5
        self.heal = self.health * .1
holy_heal = Holy(heal = 0) # add a cooldown of 3 rounds for this ability in the game flow on main.py

#Define Melee Class
## Increased melee damage
# Powerful melee ability on a CD
class Melee(Hero):
    def __init__(self,slash):
        super().__init__()
        self.melee_damage *= 1.5
        self.melee_resist *= 1.1
        self.slash = self.melee_damage * 1.5
sweeping_slash = Melee(slash=0) # add a cooldown of 2 rounds for this ability in the game flow on main.py

#Define Spell Class
## Increased spell damage
# Powerful spellpower ability on a CD
class Spell(Hero):
    def __init__(self, pyro):
        super().__init__()
        self.spell_damage *= 1.5
        self.pyro = self.spell_damage * 1.5 # This needs a 3 + round CD
pyro_blast = Spell(pyro = 0) 
print(pyro_blast.pyro)
        