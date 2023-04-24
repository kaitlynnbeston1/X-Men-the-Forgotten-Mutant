# imports
import main_funcs as m
import menus as me
import weapons as w
import your_character as yc


# global variables.
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


map = [["start", "city section", "debris", "city section"], 
       ["boring", "debris", "city section", "boring"],
["boring", "city section", "base", "debris"],
       ["debris", "city section", "boring", "blackbird"]]
            

row = 0
col = 0


# Functions.
def print_map():
    """Prints map to external file"""
    num = 0
    with open("printed_map.txt", "w") as f:
        f.write("Tile legend: \n")
        for title, dict in map_tiles.items():
            f.write(f"{title} \n")
            for d, description in dict.items():
                f.write(f"{d} \n")
                f.write(f"{description} \n")
        f.write("Map: \n")
        for t in map:
            num += 1
            f.write(f"row {num}: \n")
            for index in t:
                f.write(f"{index} \n")
        

# Movement function.
def move(r, c):
    """Function which moves your character on the game's map. 
    r and c represent the coordenates of your character. 
    r meaning row and c meaning collumn."""
    global row
    global col
    selecting = True
    while selecting:
        me.display_menu("walk")
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


# Location printing and interaction.
def location(r, c):
    """Describes the location at which the user has landed.
    Also enables interactions with various locations.
    r and c represent user coordenates."""
    map_location = map[r][c]
    if map_location in map_tiles.keys():
        print(map_tiles[map_location]["description"])
        if map_location == "start":
            me.display_menu("yes_no")
            story = m.user_action("yes_no")
            if story == "yes":
                print(f"This city has been destroyed when Magneto, a dangerous mutant terrorist had attempted to take over before being stopped by the X-men. \n {yc.character['hero name']}, it is your job to track down Magneto's secret base and end this once and for all. \n Secrets lie within this city, such as weapons or enimy encounters. \n Some may help, while others may hinder your progress.")
            elif story == "no":
                print("Ok, you may continue on your way.")
        elif map_location == "debris":
            w.salvage_weapon()
