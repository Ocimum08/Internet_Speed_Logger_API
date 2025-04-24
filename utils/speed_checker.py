import speedtest
from datetime import datetime
import os

def check_speed():
    # Initialize Speedtest
    st = speedtest.Speedtest()
    download = st.download() / 1_000_000  # Convert to Mbps
    upload = st.upload() / 1_000_000
    ping = st.results.ping

    result = {
        "download_speed_mbps": round(download, 2),
        "upload_speed_mbps": round(upload, 2),
        "ping_ms": round(ping, 2)
    }

    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)

    # Append log to file
    with open("logs/speed_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {result}\n")

    return result
