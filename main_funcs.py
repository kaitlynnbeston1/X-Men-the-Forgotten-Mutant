import sys
import movement as mo
import inventory as i
import weapons as w
import your_character as yc


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


# menu interactions 
def menu_actions(menu):
    if menu == "walk":
        mo.move(mo.row, mo.col)
        mo.location(mo.row, mo.col)
    elif menu == "inventory":
        i.read_inventory()
    elif menu == "your character":
        yc.char_acts()
