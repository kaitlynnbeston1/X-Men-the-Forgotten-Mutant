# imports
import items

class Player:
    def __init__(self):
        """
        Initializes player.
        """
        self.inventory = [items.Fists()]
        self.x = 0
        self.y = 0


    def most_powerful_weapon(self):
        """
        Gets the player's most powerful weapon.
        Used for attacking enemies.
        """
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon


    def show_inventory(self):
        """
        Presents the inventory to the user.
        """
        print("Your inventory:")
        print("Weapons")
        count = 1
        for item in self.inventory:
            if isinstance(item, items.Weapon):
                print(f"{count}. {item}")
                count += 1
        best_weapon = self.most_powerful_weapon()
        print(f"Your best weapon is: {best_weapon}.")
        print("Consumables")
        count = 1
        for item in self.inventory:
            if isinstance(item, items.Loot):
                print(f"{count}. {item}")
                count += 1
    def use_cons(self):
        """
        Uses consumable.
        """
        usable = []
        for item in self.inventory:
            if isinstance(item, items.Loot):
                usable.append(item)
        print("You can use the following  items:")
        count = 1
        for item in usable:
            print(f"{count}. {item}")
            count += 1
        selecting = "yes"
        i = "nul"
        while selecting != "no":
            try:
                i = int(input("Which item would you like to use? Enter its number."))
            except:
                print("Please enter a number.")
                continue
            if i > len(usable):
                print("Sorry, you can't select an item with that number. \n Please try again.")
            else:
                selecting = "no"
        ind = i-1
        item = usable[ind]
        print(f"You use the {item.name} and gain {item.health} HP!")
        rm = self.inventory.index(item)
        del self.inventory[rm]


        
            







    def move_north(self):
        """
        Moves the player north.
        """
        print("You walk north.")
        self.x += 1


    def move_south(self):
        """
        Moves the player south.
        """
        print("You walk south.")
        self.x -= 1


    def move_east(self):
        """
        Moves the player east.
        """
        print("You walk east.")
        self.y += 1


    def move_west(self):
        """
        Moves the player west.
        """
        print("You walk west.")
        self.y -= 1


user = Player()