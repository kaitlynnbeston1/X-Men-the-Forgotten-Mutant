import sys
import random
import main_funcs as m

# Global variables.
map_tiles = {
    "boring":{
    "description": "You arrive on a bare square of land. \n Nothing interesting seems to be here."
    },
    "debris":{
    "description": "A pile of debris from the battle lies before you. \n There appears to be a weapon lost within. \n Searching now...",
    },
    "city section": {
    "description": "You find yourself in a section of the city. \n Luckily, it hadn't been destroyed. You see buildings with ornate architecture. \n However, all appear to be empty, as the city had been evacuated.",
    },
    "start": {
    "description": "You are at the start. You are in what looks like a city. \n Would you like to hear the game's story?",
    },
    "blackbird": {
    "description": "You have arived at the Blackbird. The plane in which the X-men travel. \n Return here after Magneto has been defeated."
    },
    "base": {
    "description": "You've found the base of the Brotherhood. \n Once equipped with weapons, you may enter and take down Magneto and his allies. \n For now, you are forbidden from doing so because it's too risky."
    },
    "salvaged weapon": {
    "description": "A pile of debris. \n You already salvaged a weapon from here. \n Now, it's just a pile of rubble.",
    },
}


weapons = {
    "lockheed": {
    "description": "Not a weapon, but a creature who will loyally fight alongside you. \n A purple alien dragon who is capable of incredible flame attacks.",
    },
    "a sentinel": {
    "description": "One of the many centinals that the government had created in an attempt to destroy the X-Men. Beast reprogrammed it in such a way that it now helps the X-Men in battle with its centinal blasts." 
    },
    "the muramasa blade": {
    "description": "A blade which formerly belonged to Wolverene. Powerful enough to circumvent healing abilities.",
    },
    "the soulsword": {
    "description": "a sword which is powerful enough to defeat entities as powerful as demons.",
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


character = {
    "name": "select",
    "hero name": "select",
    "inventory": [],
}


map = [["start", "city section", "debris", "city section"], 
       ["boring", "city section", "debris", "boring"],
["boring", "city section", "base", "debris"],
       ["debris", "city section", "boring", "blackbird"]]
row = 0
col = 0


# Functions relating to weapons:
def describe_weapon(name):
    """Describes chosen weapon."""
    if name in weapon_list:
        print(weapons[name]["description"])
    else:
        print(f"It appears the programmer who made this game didn't add the weapon {name} to the game. Contact them, or be more careful how you enter words, I suppose.")


def salvage_weapon():
    """Salvages weapon from debris in game."""
    global row
    global col
    selection = random.randint(0, len(weapons.keys())-1)
    if selection in character["inventory"]:
        selection = random.randint(0, len(weapons.keys())-1)
    else:
        selection = weapon_list[selection]
        print(f"You found {selection}!")
        describe_weapon(selection)
        character["inventory"].append(selection)
        map[row][col] = "salvaged weapon"



# Movement functions
def move(r, c):
    global row
    global col
    selecting = True
    while selecting:
        m.display_menu("walk")
        dir = m.user_action("walk") 
        if dir == "north":
            if r+1 == len(map[r]):
                print("Sorry, you can't go that way.")
                continue
            else:
                print("You walk north.")
                row += 1
                selecting = False
        elif dir == "south":
            if r == 0:
                print("Sorry, you can't go that way.")
            else:
                print("You walk south.")
                row -= 1
                selecting = False
        elif dir == "east":
            try:
                testvar = map[r][c+1]
            except IndexError:
                print("Sorry, you can't go that way.")
            else:
                print("You walk east")
                col += 1
                selecting = False
        elif dir == "west":
            if c == 0:
                print("Sorry, you can't go that way.")
            else:
                print("You walk west.")
                col -= 1
                selecting = False 
        else:
            print("Sorry, that's not a direction. Please try again.")


# defining function which prints location and interacts.
def location(r, c):
    """Describes the location at which the user has landed."""
    map_location = map[r][c]
    if map_location in map_tiles.keys():
        print(map_tiles[map_location]["description"])
        if map_location == "start":
            m.display_menu("yes_no")
            story = m.user_action("yes_no")
            if story == "yes":
                print(f"This city has been destroyed when Magneto, a dangerous mutant terrorist had attempted to take over before being stopped by the X-men. \n {character['hero name']}, it is your job to track down Magneto's secret base and end this once and for all. \n Secrets lie within this city, such as weapons or enimy encounters. \n Some may help, while others may hinder your progress.")
            elif story == "no":
                print("Ok, you may continue on your way.")
        elif map_location == "debris":
            salvage_weapon()
    

# Combining all of these elements to create a working game.
def menu_actions(menu):
    if menu == "walk":
        move(row, col)
        location(row, col)
    
print("Welcome to X-men, the Unsung Hero!")
char_name = input("First thing's first, what is your name? ")
print(f"Hello {char_name}, pleased to meet you!")
character["name"] = char_name
h_name = input("Ok, if you one day hope to join the X-Men, you'll also need a hero name. Please choose one now: ")
print(f"{h_name}... I like it! Now, let's begin!")
character["hero name"] = h_name
location(row, col)
while True:
    act = m.main_menu()
    menu_actions(act)