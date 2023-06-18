# Weapons as classes/objects
class Weapon:
    """
    Superclass for all weapons.
    """
    def __init__(self):
        self.name = "weapon constructor"
        self.description = "Just a constructur. Does nothing."
    def __str__(self):
        return self.name


class Fists(Weapon):
    """
    Simulating game character's fists.
    """
    def __init__(self):
        self.name = "Fists"
        self.description = "Your fists. Really not that powerful, but may do against weak opponents."
        self.damage = 1
    

class HockeyStick(Weapon):
    """
    Simulation of a crappy hockey stick.
    """
    def __init__(self):
        self.name = "hockey stick"
        self.description = "This isn't a weapon at all! \n It's just some random hockey stick a civilian dropped whilst fleeing. \n Use this in battle only if you want to inflict the damage of a newborn kitten."
        self.damage = 2
    

class DudGun(Weapon):
    """
    Simulation of a dud gun.
    """
    def __init__(self):
        self.name = "dud gun"
        self.description = "An extremely mangled gun. May be able to hit your opponents with it."
        self.damage = 5


class WolverineClaw(Weapon):
    """
    Simulation of Wolverine's broken claw.
    """
    def __init__(self):
        self.name = "Wolverine's claw"
        self.description = "One of Wolverine's claws. He must have lost it in battle. \n It may not be the most powerful weapon you'll find, but it may be a good makeshift spear or weak sword."
        self.damage = 10


class Lockheed(Weapon):
    """
    Simulation of Lockheed.  The dragon, not the company!
    """
    def __init__(self):
        self.name = "Lockheed"
        self.description = "Not a weapon, but a creature who will loyally fight alongside you. \n A purple alien dragon who is capable of flame attacks."
        self.damage = 25
    

class Sentinel(Weapon):
    """
    Simulation of a sentinel robot.
    """
    def __init__(self):
        self.name = "sentinel"
        self.description = "One of the many centinals that the government had created in an attempt to destroy the X-Men. \n Beast reprogrammed it in such a way that it now helps the X-Men in battle with its centinal blasts."
        self.damage = 40
    

class Visor(Weapon):
    """
    Simulates Cyclops's visor.
    """
    def __init__(self):
        self.name = "Cyclops's visor"
        self.description = "Cyclops's visor. \n Somehow, he managed to use his eye blasts to charge the visor so someone without his power could use it. \n Can only be used a certain number of times."
        self.damage = 75


class MuramasaBlade():
    def __init__(self):
        self.name = "muramasa blade"
        self.description = "A blade which formerly belonged to Wolverene. Can circumvent healing abilities."
        self.damage = 100


class Soulsword(Weapon):
    """
    Simulates Magic's soulsword.
    """
    def __init__(self):
        self.name = "soulsword"
        self.description = "a sword which is strong enough to defeat entities as powerful as demons."
        self.damage = 215
    

# Loot/boosters
class Loot:
    """
    Base class for loot tiles.
    """
    def __init__(self):
        """
        Initializes base class.
        """
        self.name = "loot"
        self.health = 0
    def __str__(self):
        return self.name


class Small(Loot):
    """ 
    A small loot charge.
    """
    def __init__(self):
        """
        Initializes the class.
        """
        super().__init__()
        self.name = "Small health boost"
        self.description = "A bottle labeled \"Small Boost\" in black font. \n The liquid inside is a dull blue."
        self.health = 10


class Medium(Loot):
    """
    A medium health booster.
    """
    def __init__(self):
        """
        Initializes the object.
        """
        super().__init__()
        self.name = "Medium health boost"
        self.description = "A potion bottle labeled \"Medium boost\" in a shimmery silver font. \n The liquid inside is a brilliant deep blue that sparkles in the sunlight."
        self.health = 20


class Large(Loot):
    """
    A large health booster.
    """
    def __init__(self):
        super().__init__()
        self.name = "Large health boost"
        self.description = "A slightly large potion bottle labeled \"Large boost\" in a brilliant gold font. The letters are also written in elegant cursive. \n Inside the bottle sits a brilliant gold fluid that seems to be bright enough to light up a room."
        self.health = 40
