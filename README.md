# RPG_game
an RPG game where you encounter enemies that you have to defeat.
Different techniques are more effective on different enemies
Main enemy class with child classes for different types
    Troll - 200% damage from melee - 50% from spell, normal 100% from holy
    Orc - 200% damage from spell, 50% melee, 100% holy
    Undead - 200% from holy damage, 50% from spell, 100% melee
Hero class with subclasses
    Melee spec - increased melee damage
    Holy spec - increased holy damage
    Spell spec - increased spell damage
Player select a class with description of each class, player doesn't see enemy types.
During encounter output damage delt, with information on how the enemy resists or is effected by damage
Store enemy new health
Enemy attacks reduce your health
Holy spec can heal themselves - increase health var

Possible idea to incorporate Polymorphism concept from OOP
    A player can drink a one-time potion to allow them to take abilities from another spec. 
    i.e a melee class can drink the potion and act as a holy class for 1 fight only
