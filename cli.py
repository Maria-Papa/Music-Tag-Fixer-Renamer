import os
import mutagen
from metadata_getter import METADATA_GETTER
from variables import red, green, separator
from renamer import RENAMER

class CLI:
    def __init__(self):
        self.file_meta = []

    def check_path(self, gui, p):
        if not os.path.isdir(p):
            gui.set_output_value("Please enter a correct file path...\n", red, True)
            return False
        else:
            return True
    
    def list_dir_and_handle(self, gui, folder_path, sub_dirs=False):
        for file_name in os.listdir(folder_path):
            file_path = folder_path + "\\" + file_name

            if os.path.isdir(file_path) and sub_dirs:
                # Recursive Call
                self.list_dir_and_handle(gui, file_path, True)
            elif os.path.isfile(file_path):
                file      = mutagen.File(file_path)
                file_type = type(file)
                file_dict = {
                    "file_name": file_name,
                    "file_type": file_type,
                    "file_path": file_path,
                    "folder_path": folder_path
                }
                self.file_meta.append(file_dict)

    def rename(self, gui, file_meta):
        renamer = RENAMER(gui)
        renamer.main(file_meta)

    def get_metadata(self, gui, file_meta):
        metadata_getter = METADATA_GETTER(gui)
        metadata_getter.main(file_meta)

    def start(self, gui, start_type):
        path   = gui.get_path_value()
        subdir = gui.get_subdir_value()

        if self.check_path(gui, path) is True:
            self.list_dir_and_handle(gui, path, subdir)

            if start_type == "get_meta":
                self.get_metadata(gui, self.file_meta)

            if start_type == "fix_meta":
                print("fix_meta")

            if start_type == "rename":
                # print("rename")
                self.rename(gui, self.file_meta)
                gui.set_output_value(separator, green, False)
                gui.set_output_value("Renaming process done!\n", green, False)
