# Global variables.
inventory = []


# Functions
def read_inventory():
    print("Here is your inventory:")
    for item in inventory:
        print(item.title())

