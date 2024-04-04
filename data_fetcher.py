############################ IMPORTS ############################
import os
from pprint import pprint
import requests
from dotenv import load_dotenv

########################### VARIABLES ###########################
# Load Spotify API client credentials from .env
load_dotenv()
client_id     = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Base URL of all Spotify API endpoints
base_url   = "https://api.spotify.com/v1/"
search_url = base_url + "search"

########################### FUNCTIONS ###########################
def get_access_token():
    # Authorization Data
    auth_url = "https://accounts.spotify.com/api/token"
    data     = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    # Getting an Access Token
    auth_response      = requests.post(auth_url, data=data)
    auth_response_data = auth_response.json()
    access_token       = auth_response_data.get("access_token")

    return access_token

def get_headers():
    access_token = get_access_token()
    headers      = {
        "Authorization": "Bearer {token}".format(token=access_token),
        "Content-Type" : "application/json"
    }
    return headers

def build_params(artist, track):
    params = {
        "q"     : artist + " " + track,
        "artist": artist,
        "track" : track,
        "type"  : "track", # Allowed values: "album", "artist", "playlist", "track", "show", "episode", "audiobook"
        "limit" : 1,
        "offset": 0
    }
    return params

def search_for_track(search_url, artist, track):
    # Setting up headers and params for a GET request
    headers = get_headers()
    params  = build_params(artist, track)

    result = requests.get(search_url, 
                 headers=headers, 
                 params=params)
    data   = result.json()
    items  = data

    return items

def build_results(search):
    results = {}

    track   = search["tracks"]["items"][0]
    album   = track["album"]
    artist  = album["artists"][0]
    images  = album["images"]

    results["track_name"]      = track["name"]
    results["artist_name"]     = artist["name"]
    results["track_number"]    = track["track_number"]
    results["album_name"]      = album["name"]
    results["album_image_640"] = images[0]["url"]
    results["album_image_300"] = images[1]["url"]
    results["album_image_64"]  = images[2]["url"]

    return results

############################# CODE ##############################
search  = search_for_track(search_url, "Toto", "Africa")
results = build_results(search)

pprint(results)
