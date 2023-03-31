# Global variables.
inventory = []


# Functions
def read_inventory():
    """Function to read the inventory to the user."""
    print("Here is your inventory:")
    for item in inventory:
        print(item.title())

