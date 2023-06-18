
# Changelog

*Items marked with (M) are the version to be marked.*

## v1.0 (M)
Name: X-men, the Forgotten Mutant
- added: map,  nested lists
- added: global variables row and col
- added: continuous play
- added: main menu
- added: a module which contains widely used functions called main_funcs.
- added: "walk" as a main menu option
- added: dictionary of menus that can be used throughout the program.
- added: move() function
- added: function to describe location.
- added: quit feature in user_action() within the main_funcs module.
- fixed: movement so player can not walk off "map"

## v2.0
Name: X-Men, the Unsung Hero
- changed: name of this project from "X-Men, the Forgotten Mutant" to "X-Men, the Unsung Hero" 
- Changed: Map locations are now in a nested dictionary instead of if-statements.
- changed : Quitting message from "ok, goodbye" to "Ok, farewell, future X-Man." because apparently boring language just isn't cutting it.
- added: weapons, descriptions, and the ability to carry said weapons.
- added: character selections.
- added:opportunity to select a hero name.
- added: a dictionary to keep track of character info.

## v2.1 (M)
- fixed: The inability to quit when creating your hero.
- fixed: The fact that not all quit messages were the same. 
- added: A character submenu.
- added: ability to see what's in your inventory from the menu.
- changed: order of map tiles so the debris tiles aren't so close together.

## V 3.0
- fixed: functions are separated into modules.
- fixed: A bug where you could still get duplicate items. 
- changed: Refined character selection in the beginning.
- changed: The menu "character info" is now "your character."
- added: You can now change your character's name and hero name.

## V3.1
- fixed: All functions have docstrings now in order to conform to pep-8.
- added: A header to the unsung_hero.py file.

## V3.2 (M)
- changed: Map now prints to an external file.

## V4.0 (M)
- Changed: Menus are now separate from the main functions
- aded: character creation is now separate from the game code
- added: save feature which uses try, accept, else, finally

v5.0
- fixed: Reformatted the changelog using markdown commands
-added: Consumables
- fixed: Everything primarily uses classes.