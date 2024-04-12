import os
from variables import red, green, black, separator
from renamer import RENAMER

def check_path(gui, p):
    if not os.path.isdir(p):
        gui.set_output_value("Please enter a correct file path...\n", red, True)
    else:
        folder = p
        gui.set_output_value(f"The directory is set to '{folder}'.\n", green, True)
        gui.set_output_value(separator, green, True)

def rename(gui, folder_path, sd):
    renamer = RENAMER(gui)
    renamer.main(folder_path, sd)

def start(gui):
    path   = gui.get_path_value()
    subdir = gui.get_subdir_value()

    check_path(gui, path)
    rename(gui, path, subdir)
    gui.set_output_value(separator, green, False)
    gui.set_output_value("Renaming process done!", green, False)
