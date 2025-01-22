from pypresence import Presence
import time
import requests
import json
from requests.auth import HTTPBasicAuth

client_id = "" # < put your discord app id here
vlc_url = "http://localhost:8080/requests/status.json"
vlc_pass = "" # < put your vlc password here
rpc = Presence(client_id)
rpc.connect()

def vlc_status_get():
    try:
        response = requests.get(vlc_url, auth=HTTPBasicAuth('', vlc_pass))
        response.raise_for_status()  # raise http errors if they occur
        data = json.loads(response.text)
        state = data.get("state", "stopped")

        meta = data.get("information", {}).get("category", {}).get("meta", {})
        title = meta.get("title", "Unknown Title")
        album = meta.get("album", "Unknown Album")
        filename = meta.get("filename", "Unknown File")

        # fallback
        if title == "Unknown Title":
            title = filename

        return state, title, album
    except requests.exceptions.RequestException as e:
        print(f"Error fetching VLC status!: {e}")
        return "stopped", None, None

try:
    while True:
        state, title, album = vlc_status_get()
        if state == "playing":
            rpc.update(
                state=f"From {album}",
                details=f"Listening to {title}",
                large_image="vlc_logo",
                large_text="VLC Media Player"
            )
        elif state == "paused":
            rpc.update(
                state="Paused",
                details=f"Listening to {title}" if title else "No song playing",
                large_image="vlc_logo",
                large_text="VLC Media Player"
            )
        else:
            rpc.clear()

        time.sleep(15) # < update every 15 seconds, you can config this, however its on recommended time because of discord guidelines
except KeyboardInterrupt:
    rpc.clear()
    print("Rich Presence stopped!" '\n' "CODE BY AVeemo(@veraveemo) ON DISCORD.")