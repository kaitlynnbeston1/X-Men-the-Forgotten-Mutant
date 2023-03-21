import sys
import main_funcs as m

# Global variables. 
map = [["start", "city section", "debris", "city section"], 
       ["debris", "city section", "debris", "boring"],
["boring", "city section", "base", "debris"],
       ["city section", "city section", "boring", "blackbird"]]
row = 0
col = 0

# Movement functions
def move(r, c):
    global row
    global col
    selecting = True
    while selecting:
        m.display_menu("walk")
        dir = m.user_action("walk") 
        if dir == "north":
            if r+1 == len(map[r]):
                print("Sorry, you can't go that way.")
                continue
            else:
                print("You walk north.")
                row += 1
                selecting = False
        elif dir == "south":
            if r == 0:
                print("Sorry, you can't go that way.")
            else:
                print("You walk south.")
                row -= 1
                selecting = False
        elif dir == "east":
            try:
                testvar = map[r][c+1]
            except IndexError:
                print("Sorry, you can't go that way.")
            else:
                print("You walk east")
                col += 1
                selecting = False
        elif dir == "west":
            if c == 0:
                print("Sorry, you can't go that way.")
            else:
                print("You walk west.")
                col -= 1
                selecting = False 
        else:
            print("Sorry, that's not a direction. Please try again.")


# defining function which prints location.
def location(r, c):
    """Describes the location at which the user has landed."""
    map_location = map[r][c]
    if map_location == "debris":
        print("You arrive at a destroyed portion of the city. \n You can see what looks to be weapons. \n You can't identify whether they belong to the x-men or the brotherhood, as they are caked in dirt. \n In the future, you may be able to salvage them from here. However, you do not yet have the skills to do so.")
    elif map_location == "boring":
        print("You arrive on a bare square of land. \n Nothing interesting seems to be here.")
    elif map_location == "start":
        print("You are at the start. You are in what looks like a city. \n Would you like to hear the game's story?")
        m.display_menu("yes_no")
        story = m.user_action("yes_no")
        if story == "yes":
            print("This city has been destroyed when Magneto, a dangerous mutant terrorist had attempted to take over before being stopped by the X-men. \n Unnamed mutant, it is your job to track down Magneto's secret base and end this once and for all. \n Secrets lie within this city, such as weapons or enimy encounters. \n Some may help, while others may hinder your progress.")
        elif story == "no":
            print("Ok, you may continue on your way.")
    elif map_location == "city section":
        print("You find yourself in a section of the city. \n Luckily, it hadn't been destroyed. You see buildings with ornate architecture. \n However, all appear to be empty, as the city had been evacuated.")
    elif map_location == "base":
        print("You've found the base of the Brotherhood. \n Once equipped with weapons, you may enter and take down Magneto and his allies. \n For now, you are forbidden from doing so because it's too risky.")
    elif map_location == "blackbird":
        print("You have arived at the Blackbird. The plane in which the X-men travel. \n Return here after Magneto has been defeated.")


# Combining all of these elements to create a working menu.
def menu_actions(menu):
    if menu == "walk":
        move(row, col)
        location(row, col)
    
print("Welcome to X-men, the forgotten mutant.")
location(row, col)
while True:
    act = m.main_menu()
    menu_actions(act)