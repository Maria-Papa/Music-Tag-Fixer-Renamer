import os
import mutagen
from api import API
from pprint import pprint
from dotenv import load_dotenv
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from variables import search_url, green

class METADATA_GETTER:
    def __init__(self, gui):
        # Load Spotify API client credentials from .env
        load_dotenv()
        client_id     = os.environ.get("CLIENT_ID")
        client_secret = os.environ.get("CLIENT_SECRET")

        self.api = API(client_id, client_secret)
        self.gui = gui

    def result(self):
        search = self.api.search_for_track(search_url, "Toto", "Africa")

        if "error" in search:
            pprint(search["error"]["message"])
        else:
            results = self.api.map_results(search)
            pprint(results)

    def main(self, file_meta):
        for meta in file_meta:
            file_name   = meta["file_name"]
            file_type   = meta["file_type"]
            file_path   = meta["file_path"]
            folder_path = meta["folder_path"]
   
            if file_type == mutagen.mp3.MP3:
                track = MP3(file_path)
                # self._handle_mp3(folder_path, track, file_name)
            elif file_type == mutagen.flac.FLAC:
                track = FLAC(file_path)
                # self._handle_flac(folder_path, track, file_name)
            else:
                self.gui.set_output_value(f"File type {file_type} is not supported yet...\n", green)
