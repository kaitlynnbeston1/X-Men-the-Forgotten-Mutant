# imports
import pickle
import os

import movement as mo
import your_character as yc
import inventory as i


path = os.getcwd() # file's path
savefile_path = f"{path}/savefile.pickle" # where the save file is located.


# functions
def save():
    """Saves user data to a pickle file.
    Allows user to pick up where they left off.
    """
    data = {
    "row": mo.row,
    "col": mo.col,
    "map": mo.map,
    "name": yc.character["name"],
    "hero": yc.character["hero name"],
    "inv": i.inventory,
}

    try:
        pickle.dump(data, open("savefile.pickle", "wb"))
    except:
        print("An error has occured whilst saving. \n Please contact the developper. \n If you are the developper, get to work!")
    else:
        print("Data saved.")
    finally:
        print("finished saving.")

# loading the file
def load_save():
    """Loads saved data."""
    global data
    print("Loading data...")
    try:
        data = pickle.load(open("savefile.pickle", "rb"))
        mo.row = data["row"]
        mo.col = data["col"]
        mo.map = data["map"]
        yc.character["name"] = data["name"]
        yc.character["hero name"] = data["hero"]
        i.inventory = data["inv"]
    except:
        print("There was an error loading your save file. \n Please contact the developer. \n If that is you, you know what to do!")
    else:
        print("Save file loaded successfully!")
    finally:
        print("Loading of save file complete!")
