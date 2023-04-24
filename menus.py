# menus are important. Let's add them.
menus ={
    "main": ["walk", "your character", "inventory"],
    "walk": ["north", "south", "east", "west"],
    "yes_no": ["yes", "no"],
    "your character": ["info", "set name", "set hero name"],
    "inventory": [],
} 


# Making said menus functional.
# Function to display menus. 
def display_menu(name):
    """Displays chosen menu to user."""
    menuvalues = menus[name]
    if name == "main":
        print("What would you like to do? ")
    elif name == "walk":
        print("Which direction would you like to go?")
    elif name == "your character":
        print("Choose an action to take relating to your character.")
    elif name == "yes_no":
        print("Which option would you like to select?")
    [print(action.title()) for action in menuvalues]




