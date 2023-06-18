#imports
import items
import movement as mo
import tiles
from player import user

import random


# Globals 
loot_list = [items.Small(), items.Medium(), items.Large()]


def describe_loot(name):
    """
    Describes chosen loot to the user.
    """
    d = getattr(name, "description", None)
    if d != None:
        print(d)
    else:
        print("Error printing loot.")


def get_loot():
    """
    Collects loot.
    """
    selection = random.randint(0, len(loot_list)-1)
    selection = loot_list[selection]
    print(f"You found {selection.name}!")
    describe_loot(selection)
    user.inventory.append(selection)
    mo.gameMap[user.x][user.y] = tiles.RadedBuilding(user.x, user.y)
