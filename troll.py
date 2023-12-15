# Increased damage taken from melee
# Deals Melee damage - Face to face style fighting
# Reduced damage from spells
# No change on holy damage
from enemy_parent import Enemy
class Troll(Enemy):
    # reducing spell resist of Troll
     Enemy.spell_resist = Enemy.spell_resist * 2
     Enemy.melee_resist = Enemy.melee_resist / 2
     Enemy.meleedamage = Enemy.meleedamage * 2

print (Troll.spell_resist)
print (Troll.melee_resist)
print(Troll.meleedamage)