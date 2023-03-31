# imports
import main_funcs as m
import sys


# global variables
character = {
    "name": "select",
    "hero name": "select",
    }


# character functions
# Setting character name and hero name.
def set_name():
    """Setting character name."""
    char_name = input("What is your name? \n You can also enter \"quit\" to exit. \n").title()
    if char_name == "Quit":
        print("Ok, farewell, future X-Man.")
        sys.exit()
    else:
        character["name"] = char_name
        print(f"Your name has been set to {char_name}")

def set_hero_name():
    """Sets the player's hero name."""
    h_name = input("Please choose a hero name. \n You may also enter \"quit\" to exit.\n").title()
    if h_name == "Quit":
        print("Ok, farewell, future X-Man.")
        sys.exit()
    else:
        character["hero name"] = h_name
        print(f"Your hero name is now {character['hero name']}.")
        


# function to interact with character menu
def char_acts():
    """Allows you to interact with your character.
    Changing their name, seeing info, etc."""
    m.display_menu("your character")
    category = m.user_action("your character")
    if category in m.menus["your character"]:
        if category == "info":
            print(f"name: {character['name']} \n Hero name: {character['hero name']}")
        elif category == "set name":
            set_name()
        elif category == "set hero name":
            set_hero_name()
