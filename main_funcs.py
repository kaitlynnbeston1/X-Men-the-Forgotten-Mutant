import sys
import os

import menus as me
import weapons as w
import your_character as yc

from player import user


# function to save when user quits
def user_quitting():
    """
    Prints a message when the user quits, saves, then exits the program.
    """
    print("Ok, farewell, future X-Man.")
    from saving import save
    save()
    sys.exit()


# User input function with error handling.
def user_action(section):
    """Gets user input and checks for bogus answers."""
    menuvalues = me.menus[section]
    correction = "none"
    action_inp = input("Enter any of these, or \"quit\" to exit: ")
    if action_inp in menuvalues or action_inp == "quit":
        if action_inp == "quit":
            user_quitting()
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
            me.display_menu(section)
            attempts += 1
            action_inp = input("Enter any of these, or \"quit\" to exit: ")
            if action_inp in menuvalues or action_inp == "quit":
                correct = 'yes'
                if action_inp == "quit":
                    user_quitting()
                else:
                    return action_inp
    
    
# Function which sends user back to main menu.
def main_menu():
    """For within other functions. Goes back to main menu."""
    me.display_menu("main")
    m_act = user_action("main")
    return m_act


# function to save thanks to stupid circular imports.
def save_game():
    from saving import save
    save()


# Function to load a save.
def check_save():
    """
    Asks user if they would like to start a game and acts accordingly.
    """
    from saving import savefile_path
    if os.path.exists(savefile_path) == True:
        print("It looks like you have an existing game. \n Would you like to continue?")
        me.display_menu("yes_no")
        choice = user_action("yes_no")
        if choice == "yes":
            from saving import load_save
            load_save()
        else:
            print("Ok, starting over.")
            yc.create_char()
    else:
        yc.create_char()


# menu interactions 
def menu_actions(menu):
    """Enables menu interaction."""
    if menu == "walk":
        import movement as mo
        mo.move(user.x, user.y)
        mo.location(user.x, user.y)
    elif menu == "inventory":
        me.display_menu("inventory")
        x = user_action("inventory")
        if x == "show inventory":
            user.show_inventory()
        elif x == "use consumable":
            user.use_cons()
    elif menu == "your character":
        yc.char_acts()
    elif menu == "story":
        with open("storyline.txt") as text:
            contents = text.read()
        print(contents)

