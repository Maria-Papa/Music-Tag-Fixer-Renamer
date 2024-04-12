def start(gui):
    subdir = gui.get_subdir_value()

    if subdir is False:
        gui.set_output_value("FALSE\n")
    else:
        gui.set_output_value("TRUE\n")
        