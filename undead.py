# Undead are vunerable to holy, have higher spell resist, no impact on melee
# Undead deal spell damage

from enemy_parent import Enemy
class Undead(Enemy):
    # reducing spell resist of Undead
     Enemy.spell_resist = Enemy.spell_resist * 2
     Enemy.holy_resist= Enemy.holy_resist/ 2
     Enemy.spelldamage = Enemy.spelldamage * 2

print (Undead.spell_resist)
print (Undead.holy_resist)
print(Undead.spelldamage)