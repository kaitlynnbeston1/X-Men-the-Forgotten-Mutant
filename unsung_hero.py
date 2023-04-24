"""
Title: X-Men, the Unsung Hero
Class: CS30
Date: 31/03/2023
Coder's name: Kaitlynn Beston
Version: 3.1
"""


import main_funcs as m
import movement as mo



# Main code
print("Welcome to X-Men, the Unsung Hero.")
m.check_save()
mo.print_map()
mo.location(mo.row, mo.col)
while True:
    act = m.main_menu()
    m.menu_actions(act)