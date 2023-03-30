import main_funcs as m
import movement as mo
import your_character as yc



# Combining all of these elements to create a working game.
print("Welcome to X-men, the Unsung Hero!")
print("Before you begin your journey to become an X-Man, there's some information I'll need to know.")
yc.set_name()
yc.set_hero_name()
print(f"Pleased to meet you, {yc.character['name']}... Or should I say, {yc.character['hero name']}. \n Now, let your quest begin!")
mo.location(mo.row, mo.col)
while True:
    act = m.main_menu()
    m.menu_actions(act)