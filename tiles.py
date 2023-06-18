# Imports
from player import user

import sys


# A basic base class.
class MapTile:
    """
    Parent class for map tiles.
    """


    def __init__(self, x, y):
        """
        Initializes the class.
        """
        self.x = x
        self.y = y
        self.name = "map tile"
        self.description = "A useless map tile. The silly programmer who made this game apparently doesn't know how to use classes. Please forgive her lack of attention to detail."


    def __str__(self):
        return self.name


    def describe(self):
        """
        Describes the tile to the user.
        """
        print(self.description)


# All major map tiles.
class Boring(MapTile):
    """
    Tile that does nothing for the player.
    """


    def __init__(self, x, y):
        """
        Initializes the object.
        """
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.name = "Boring tile"
        self.description = "You come across an empty field. Nothing to see here."


class Loot(MapTile):
    """
    A building in the invaded city that you can rade for supplies.
    """
    def __init__(self, x, y):
        """
        Initializes the object.
        """
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.name = "Abandoned building"
        self.description = """You find an undestroyed building that lookes to be some kind of shop. 
        The architecture is some of the best you have ever seen, with ornate stone carvings and elegant collumns.
        Rading some supplies..."""


class Debris(MapTile):
    """
    Some debris that stores a weapon for the user to collect.
    """
    def __init__(self, x, y):
        """
        Initializes the object.
        """
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.name = "debris"
        self.description = "A pile of debris from the battle lies before you. \n There appears to be a weapon lost within. \n Searching now..."


class Enemy(MapTile):
    """
    A class with an unspecified enemy that you can interact with.
    """
    def __init__(self, x, y):
        """
        Initializes the object.
        """
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.name = "Enemy tile"
        self.description = f"You come across a member of the Brotherhood!"
    def describe(self):
        """
        Makes user attack.
        Describes tile.
        """
        print(self.description)
        mpw = user.most_powerful_weapon()
        if mpw.name == "Lockheed" or mpw.name == "Wolverine's claw" or mpw.name == "Cyclops's visor":
            print(f"You attack with {mpw}!")
        else:
            print(f"You attack with your {mpw}!")


class SalvagedWeapon(MapTile):
    """ 
    Tile for a weapon once it has been salvaged.
    """
    def __init__(self, x, y):
        """
        Initializes object.
        """
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.name = "Useless debris"
        self.description = "A pile of debris. \n You already salvaged a weapon from here. \n Now, it's just a pile of rubble."


class RadedBuilding(MapTile):
    """
    Tile for a loot tile once you have raded.
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.name = "Raded building"
        self.description = "An undestroyed building in the city. \n You have already raded it."


class DefeatedEnemy(MapTile):
    """
    Tile for when enemy is defeated.
    """
    def __init__(self, x, y):
        """
        Initializes object.
        """
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.name = "Defeated enemy"
        self.description = "The unconscious body of one of the Brotherhood lies in frunt of you. \n You have defeated them, for now."


class Blackbird(MapTile):
    """
    Victory tile.
    """
    def __init__(self, x, y):
        """
        Initializes object.
        """
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.name = "Blackbird"
        self.description = "You have arived at the Blackbird. The plane in which the X-men travel. \n You are now officially an X-man! Thanks for playing."
    def describe(self):
        print(self.description)
        sys.exit()
        

class Start(MapTile):
    """ 
    The game's start tile.
    """


    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.name = "Start tile"
        self.description = "You are at the start, in a city that has been taken over. \n GO to the story section in the main menue to learn more."
        

map_tiles = [Start("nul", "nul"), Boring("nul", "nul"), Loot("nul", "nul"), RadedBuilding("nul", "nul"), Debris("nul", "nul"), SalvagedWeapon("nul", "nul"), Enemy("nul", "nul"), DefeatedEnemy("nul", "nul"), Blackbird("nul", "nul")]
