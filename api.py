import requests

class API:

    def __init__(self, client_id, client_secret):
        self.client_id     = client_id
        self.client_secret = client_secret
        self.access_token  = self._get_access_token()

    def _get_access_token(self):
        """Posts a request to get the access token."""
        # Authorization Data
        auth_url = "https://accounts.spotify.com/api/token"
        data     = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        # Getting an Access Token
        auth_response      = requests.post(auth_url, data=data)
        status_code        = auth_response.status_code
        auth_response_data = auth_response.json()

        if status_code == 200:
            access_token = auth_response_data.get("access_token")
            
            return access_token
        else:
            print(auth_response_data["error_description"])

            return 0

    def _get_headers(self):
        """The headers for the GET request"""
        access_token = self.access_token
        headers      = {
            "Authorization": "Bearer {token}".format(token=access_token),
            "Content-Type" : "application/json"
        }

        return headers

    def _build_params(self, artist, track):
        """Builds the parameters as described in https://developer.spotify.com/documentation/web-api/reference/search.

        Args:
            artist (str): The name of the artist.
            track (str): The name of the track.

        Returns:
            dict: A dictionary
        """
        params = {
            "q"     : artist + " " + track,
            "artist": artist,
            "track" : track,
            "type"  : "track", # Allowed values: "album", "artist", "playlist", "track", "show", "episode", "audiobook"
            "limit" : 1,
            "offset": 0
        }

        return params

    def search_for_track(self, search_url, artist, track):
        # Setting up headers and params for a GET request
        headers = self._get_headers()
        params  = self._build_params(artist, track)

        result = requests.get(search_url, 
                    headers=headers, 
                    params=params)
        data   = result.json()
        items  = data

        return items

    def map_results(self, search):
        """_summary_

        Args:
            search (_type_): _description_

        Returns:
            _type_: _description_
        """
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
