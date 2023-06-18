"""
Title: X-Men, the Unsung Hero
Class: CS30
Date: 15/06/2023
Coder's name: Kaitlynn Beston
Version: 4.0
"""


import main_funcs as m
import movement as mo
from player import user



# Main code
print("Welcome to X-Men, the Unsung Hero.")
m.check_save()
mo.print_map()
mo.location(user.x, user.y)
while True:
    act = m.main_menu()
    m.menu_actions(act)