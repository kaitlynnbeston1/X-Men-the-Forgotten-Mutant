# imports
import main_funcs as m
import menus as me
import weapons as w
import loot as l
import your_character as yc
import tiles
from player import user


gameMap = [[tiles.Start(0, 0), tiles.Loot(0, 1), tiles.Debris(0, 2), tiles.Enemy(0, 3)], 
       [tiles.Boring(1, 0), tiles.Debris(1, 1), tiles.Loot(1, 2), tiles.Boring(1, 3)],
[tiles.Enemy(2, 0), tiles.Boring(2, 1), tiles.Enemy(2, 2), tiles.Debris(2, 3)],
       [tiles.Loot(3, 0), tiles.Boring(3, 1), tiles.Boring(3, 2), tiles.Blackbird(0, 3)]]
            

# Functions.
def print_map():
    """Prints map to external file"""
    num = 0
    with open("printed_map.txt", "w") as f:
        f.write("Tile legend: \n")
        for title in tiles.map_tiles:
            f.write(f"{title.name} \n")
            f.write(f"{title.description} \n ")
        f.write("Map: \n")
        for t in gameMap:
            num += 1
            f.write(f"row {num}: \n")
            for index in t:
                f.write(f"{index.name} \n")
        

# Movement function.
def move(r, c):
    """
    Function which moves your character on the game's map.
    r and c represent the coordenates of your character.
    """ 
    selecting = True
    while selecting:
        me.display_menu("walk")
        dir = m.user_action("walk") 
        if dir == "north":
            if r+1 == len(gameMap[r]):
                print("Sorry, you can't go that way.")
                continue
            else:
                user.move_north()
                selecting = False
        elif dir == "south":
            if r == 0:
                print("Sorry, you can't go that way.")
            else:
                user.move_south()
                selecting = False
        elif dir == "east":
            try:
                testvar = gameMap[r][c+1]
            except IndexError:
                print("Sorry, you can't go that way.")
            else:
                user.move_east()
                selecting = False
        elif dir == "west":
            if c == 0:
                print("Sorry, you can't go that way.")
            else:
                user.move_west()
                selecting = False 
        else:
            print("Sorry, that's not a direction. Please try again.")


# Location printing and interaction.
def location(r, c):
    map_location = gameMap[r][c]
    if map_location.name == "debris":
        map_location.describe()
        w.salvage_weapon()
        gameMap[r][c] = tiles.SalvagedWeapon(r, c)
    elif map_location.name == "Abandoned building":
        map_location.describe()
        l.get_loot()
        gameMap[r][c] = tiles.RadedBuilding(user.x, user.y)
    else:
        map_location.describe()
