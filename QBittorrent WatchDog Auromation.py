import time
import qbittorrentapi

#Before running this script, make sure you have the qbittorrent web setup and API enabled.
#To do that go on this open qbittorrent webui, go to Tools > Options > Web UI and enable it. Set a username and password for the WebUI.
#Then go to this website http://localhost:8080/ and log in with your credentials. If you can log in, then the script will work.
#After saving the whole code and running it perfectly make sure to rename the file type from .py to .pyw [ For example if the file name is qb_control.py make it qb_control.pyw ]
#Then double click the .pyw file and open it with python.It will automatically run in the background.You wont need to open VS code/whatever you have to make it open physically.
# Configure your WebUI credentials

HOST = "http://localhost:8080"
USERNAME = "your username"
PASSWORD = "your password"
CHECK_INTERVAL_SECONDS = 30  # Checks every 30 seconds

def run_watchdog():
    try:
        client = qbittorrentapi.Client(host=HOST, username=USERNAME, password=PASSWORD)
        client.auth_log_in()
        print("Connected to qBittorrent watchdog. Monitoring downloads...\n")
    except Exception as e:
        print(f"Initial connection failed: {e}")
        return

    while True:
        try:
            # Fetch all torrents
            torrents = client.torrents_info()

            for torrent in torrents:
                # Target states where downloads stop or stall unexpectedly
                target_states = [
                    "pausedDL",
                    "error",
                    "missingFiles",
                    "stoppedDL",
                    "stalledDL"
                ]

                if torrent.state in target_states and torrent.progress < 1.0:
                    print(f"[{time.strftime('%H:%M:%S')}] Detected inactive download: '{torrent.name}' (State: {torrent.state}). Resuming...")
                    client.torrents_resume(torrent_hashes=torrent.hash)
                    time.sleep(2)  # Short pause after triggering

        except qbittorrentapi.APIConnectionError:
            print("qBittorrent is closed or unreachable. Retrying in next cycle...")
        except Exception as e:
            print(f"Unexpected error: {e}")

        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    run_watchdog()
