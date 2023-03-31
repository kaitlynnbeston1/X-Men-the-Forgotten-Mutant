# Imports and global variables.
import random
import inventory as i
import movement as mo 

# global variables
weapons = {
    "lockheed": {
    "description": "Not a weapon, but a creature who will loyally fight alongside you. \n A purple alien dragon who is capable of incredible flame attacks.",
    },
    "a sentinel": {
    "description": "One of the many centinals that the government had created in an attempt to destroy the X-Men. Beast reprogrammed it in such a way that it now helps the X-Men in battle with its centinal blasts." 
    },
    "the muramasa blade": {
    "description": "A blade which formerly belonged to Wolverene. Can circumvent healing abilities.",
    },
    "the soulsword": {
    "description": "a sword which is strong enough to defeat entities as powerful as demons.",
    },
    "wolverine's claw": {
    "description": "One of Wolverine's claws. He must have lost it in battle. \n It may not be the most powerful weapon you'll find, but it may be a good makeshift spear or weak sword.",
    },
    "cyclops's visor": {
    "description": "Cyclops's visor. \n Somehow, he managed to use his eye blasts to charge the visor so someone without his power could use it.",
    },
    "a hockey stick": {
    "description": "This isn't a weapon at all! \n It's just some random hockey stick a civilian dropped whilst fleeing. \n Use this in battle only if you want to inflict the damage of a newborn kitten.",
    },
    "a dud gun": {
    "description": "An extremely mangled gun. Does absolutely nothing.",
    },
}


weapon_list = list(weapons.keys())


# Functions.
def describe_weapon(name):
    """Describes chosen weapon to the user."""
    if name in weapon_list:
        print(weapons[name]["description"])
    else:
        print(f"It appears the programmer who made this game didn't add the weapon {name} to the game. I'd recommend getting in contact with them.")


def salvage_weapon():
    """Salvages weapon from debris in game."""
    selecting = "yes"
    while selecting == "yes":
        selection = random.randint(0, len(weapons.keys())-1)
        if selection in i.inventory:
            selection = random.randint(0, len(weapons.keys())-1)
        else:
            selecting = "no"
            selection = weapon_list[selection]
            print(f"You found {selection}!")
            describe_weapon(selection)
            i.inventory.append(selection)
            mo.map[mo.row][mo.col] = "salvaged weapon"
