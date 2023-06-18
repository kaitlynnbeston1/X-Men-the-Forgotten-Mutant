# imports
from player import user

import sys

import main_funcs as m
import menus as me


# global variables


# character functions
# Setting character name and hero name.
def set_name():
    """Setting character name."""
    char_name = input("What is your name? \n You can also enter \"quit\" to exit. \n").title()
    if char_name == "Quit":
        print("Ok, farewell, future X-Man.")
        sys.exit()
    else:
        user.name = char_name
        print(f"Your name has been set to {char_name}")

def set_hero_name():
    """Sets the player's hero name."""
    h_name = input("Please choose a hero name. \n You may also enter \"quit\" to exit.\n").title()
    if h_name == "Quit":
        print("Ok, farewell, future X-Man.")
        sys.exit()
    else:
        user.heroName = h_name
        print(f"Your hero name is now {user.heroName}.")
        

# creating your character.
def create_char():
    print("Welcome to X-men, the Unsung Hero!")
    print("Before you begin your journey to become an X-Man, there's some information I'll need to know.")
    set_name()
    set_hero_name()
    print(f"Pleased to meet you, {user.name}... Or should I say, {user.heroName}. \n Now, let your quest begin!")


# function to interact with character menu
def char_acts():
    """Allows you to interact with your character.
    Changing their name, seeing info, etc."""
    me.display_menu("your character")
    category = m.user_action("your character")
    if category in me.menus["your character"]:
        if category == "info":
            print(f"name: {user.name} \n Hero name: {user.heroName}")
        elif category == "set name":
            set_name()
        elif category == "set hero name":
            set_hero_name()
