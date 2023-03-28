import sys


# menus are important. Let's add them.
menus ={
    "main": ["walk", "character info", "inventory"],
    "walk": ["north", "south", "east", "west"],
    "yes_no": ["yes", "no"],
    "character info": ["name", ],
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
    elif name == "character info":
        print("What would you like to know about your character?")
    elif name == "yes_no":
        print("Which option would you like to select?")
    [print(action.title()) for action in menuvalues]


# User input function with error handling.
def user_action(section):
    """Gets user input and checks for bogus answers."""
    menuvalues = menus[section]
    correction = "none"
    action_inp = input("Enter any of these, or \"quit\" to exit: ")
    if action_inp in menuvalues or action_inp == "quit":
        if action_inp == "quit":
            print("Ok, farewell, future X-Man.")
            sys.exit()
        else:
            return action_inp
    else:
        correct = "no"
        attempts = 1
        while correct != "yes":
            if attempts == 1:
                print("That is not a valid option. Please try again")
            elif attempts > 1 and attempts <= 3:
                print("Sorry, this option is also incorrect. Please try again.")
            else:
                print("Ok, you must be joking. Please enter a VALID option.")
            display_menu(section)
            attempts += 1
            action_inp = input("Enter any of these, or \"quit\" to exit: ")
            if action_inp in menuvalues or action_inp == "quit":
                correct = 'yes'
                if action_inp == "quit":
                    print("Ok, farewell, future X-Man.")
                    sys.exit()
                else:
                    return action_inp
    
    
# Function which sends user back to main menu.
def main_menu():
    """For within other functions. Goes back to main menu."""
    display_menu("main")
    m = user_action("main")
    return m


