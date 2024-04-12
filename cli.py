import os
from variables import red, green, separator
from renamer import RENAMER

def check_path(gui, p):
    if not os.path.isdir(p):
        gui.set_output_value("Please enter a correct file path...\n", red, True)
    else:
        folder = p
        gui.set_output_value(f"The directory is set to '{folder}'.\n", green)
        gui.set_output_value(separator, green)

def rename(gui, folder_path, sd):
    renamer = RENAMER(gui)
    renamer.main(folder_path, sd)

# def fix(gui, folder_path, sd):
#     renamer = RENAMER(gui)
#     renamer.main(folder_path, sd)

def start(gui, start_type):
    path   = gui.get_path_value()
    subdir = gui.get_subdir_value()

    check_path(gui, path)

    if start_type == "rename":
        rename(gui, path, subdir)
        gui.set_output_value(separator, green, False)
        gui.set_output_value("Renaming process done!", green, False)
    # if start_type == "fix":
    #     # fix()
    #     print("FIX")
