# Increased damage taken from spell
# Deals Melee damage
# Reduced damage from melee
# No change on holy damage
from enemy_parent import Enemy
class Orc(Enemy):
    # reducing spell resist of orc
     Enemy.spell_resist = Enemy.spell_resist / 2
     Enemy.melee_resist = Enemy.melee_resist * 2
     Enemy.meleedamage = Enemy.meleedamage * 2

print (Orc.spell_resist)
print (Orc.melee_resist)
print(Orc.meleedamage)