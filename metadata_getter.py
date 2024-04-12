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

        self.metadata = []

    def _handle_mp3(self, track):
        # Artist
        if ("TPE1" in track.keys()):
            artist = str(track.get("TPE1"))
        # Track Title
        if ("TIT2" in track.keys()):
            title = str(track.get("TIT2"))

        return (artist, title)

    def _handle_flac(self, track):
        # Artist
        if ("artist" in track.keys()):
            artist = str(track.get("artist")[0])
        # Track Title
        if ("title" in track.keys()):
            title = str(track.get("title")[0])

        return (artist, title)

    def _search_meta(self, artist, title):
        search = self.api.search_for_track(search_url, artist, title)

        if "error" in search:
            pprint(search["error"]["message"])
        else:
            results = self.api.map_results(search)
            # pprint(results)
            self.metadata.append(results)

    def main(self, file_meta):
        for meta in file_meta:
            # file_name   = meta["file_name"]
            file_type   = meta["file_type"]
            file_path   = meta["file_path"]
            # folder_path = meta["folder_path"]
   
            if file_type == mutagen.mp3.MP3:
                track = MP3(file_path)
                res   = self._handle_mp3(track)
            elif file_type == mutagen.flac.FLAC:
                track = FLAC(file_path)
                res   = self._handle_flac(track)
            else:
                self.gui.set_output_value(f"File type {file_type} is not supported yet...\n", green)

            self._search_meta(res[0], res[1])

        self.gui.set_output_value(self.metadata)
