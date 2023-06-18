# Imports and global variables.
import items
import movement as mo
import tiles

import random


from player import user


# Weapons in a list.
weapon_list = [items.HockeyStick(), items.DudGun(), items.WolverineClaw(), items.Lockheed(), items.Sentinel(), items.Visor(), items.MuramasaBlade(), items.Soulsword()]

# Functions.
def describe_weapon(name):
    """Describes chosen weapon to the user."""
    d = getattr(name, "description", None)
    if d != None:
        print(d)
    else:
        print("Error printing weapon.")
def salvage_weapon():
    """Salvages weapon from debris in game."""
    selecting = "yes"
    while selecting == "yes":
        selection = random.randint(0, len(weapon_list)-1)
        if selection in user.inventory:
            selection = random.randint(0, len(weapon_list) -1)
        else:
            selection = weapon_list[selection]
            selecting = "no"
            print(f"You found {selection.name}!")
            describe_weapon(selection)
            user.inventory.append(selection)
            mo.gameMap[user.x][user.y] = tiles.SalvagedWeapon(user.x, user.y)
