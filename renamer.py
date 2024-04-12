import os
import re
import mutagen
from mutagen.mp3 import MP3
from mutagen.flac import FLAC

class RENAMER:
    def __init__(self) -> None:
        pass

    def _lowercase_match(self, match):
        """Lowercase the whole regular expression match group."""
        return match.group().lower()

    def _title(self, value):
        titled = value.title()
        titled = re.sub(r"([a-z])'([A-Z])", self._lowercase_match, titled)  # Fix Don'T
        titled = re.sub(r"\d([A-Z])", self._lowercase_match, titled)  # Fix 1St and 2Nd
        return titled

    def _prettify(self, str):
        str = str.strip()
        str = self._title(str)
        return str 

    def _rename(self, path, current_name, new_name):
        current_file = path + "\\" + current_name
        new_file     = path + "\\" + new_name

        print(f"Renaming '{current_name}' to '{new_name}'...")
        os.rename(current_file, new_file)

    def _handle_mp3(self, path, track, file):
        # Artist
        if ("TPE1" in track.keys()):
            artist = str(track.get("TPE1"))
            artist = self._prettify(artist)

        # Track Title
        if ("TIT2" in track.keys()):
            title = str(track.get("TIT2"))
            title = self._prettify(title)

        if artist and title:
            new_name = artist + " - " + title + ".mp3"
            self._rename(path, file, new_name)

    def _handle_flac(self, path, track, file):
        # Artist
        if ("artist" in track.keys()):
            artist = str(track.get("artist")[0])
            artist = self._prettify(artist)

        # Track Title
        if ("title" in track.keys()):
            title = str(track.get("title")[0])
            title = self._prettify(title)

        if artist and title:
            new_name = artist + " - " + title + ".flac"
            self._rename(path, file, new_name)

    def main(self, folder_path, sub_dirs):
        for file_name in os.listdir(folder_path):
            file_path = folder_path + "\\" + file_name

            if os.path.isdir(file_path) and sub_dirs:
                # Recursive Call
                self.main(file_path, True)
            elif os.path.isfile(file_path):
                file      = mutagen.File(file_path)
                file_type = type(file)

                if file_type == mutagen.mp3.MP3:
                    track = MP3(file_path)
                    self._handle_mp3(folder_path, track, file_name)
                elif file_type == mutagen.flac.FLAC:
                    track = FLAC(file_path)
                    self._handle_flac(folder_path, track, file_name)
                else:
                    print(f"File type {type} is not supported yet...")
