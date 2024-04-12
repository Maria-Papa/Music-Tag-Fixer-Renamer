import os
from variables import red, green, orange, black
from renamer import RENAMER

def check_path(gui, p):
    if not os.path.isdir(p):
        gui.set_output_value("Please enter a correct file path...\n", red, True)
    else:
        folder = p
        gui.set_output_value(f"The directory is set to '{folder}'.\n", green, True)

def rename(folder_path, sd):
    renamer = RENAMER()
    renamer.main(folder_path, sd)

def start(gui):
    path   = gui.get_path_value()
    subdir = gui.get_subdir_value()

    check_path(gui, path)
    rename(path, subdir)

    # if subdir is False:
    #     gui.set_output_value(f"subdir: {subdir}\n")
    #     gui.set_output_value(f"path: {path}\n")
    # else:
    #     gui.set_output_value("TRUE\n")
