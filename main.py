from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.speed_checker import check_speed
from datetime import datetime
import webbrowser
import threading
import time

app = FastAPI(title="Internet Speed Logger API")

# Optional: Allow CORS if you want to call API from a frontend app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory log storage
logs = []

# Auto-open Swagger UI on app start
def open_browser():
    time.sleep(1)  # Give the server a second to start
    webbrowser.open("http://127.0.0.1:8000/docs")

@app.on_event("startup")
def startup_event():
    threading.Thread(target=open_browser).start()

@app.get("/check-speed", tags=["Speed Test"])
def run_speed_check():
    return check_speed()

@app.post("/log-status", tags=["Logging"])
def log_status(is_online: bool):
    timestamp = str(datetime.now())
    logs.append({"timestamp": timestamp, "status": "online" if is_online else "offline"})
    return {"message": "Status logged", "timestamp": timestamp, "is_online": is_online}

@app.get("/status", tags=["Logging"])
def get_status():
    if not logs:
        return {"status": "unknown", "message": "No data yet."}
    return {"latest_status": logs[-1]}

@app.get("/downtime-logs", tags=["Logging"])
def get_downtime_logs():
    return [log for log in logs if log["status"] == "offline"]

@app.get("/uptime-summary", tags=["Logging"])
def get_uptime_summary():
    total = len(logs)
    if total == 0:
        return {"summary": "No data"}
    online_count = sum(1 for log in logs if log["status"] == "online")
    offline_count = total - online_count
    uptime_percent = (online_count / total) * 100
    return {
        "total_checks": total,
        "online": online_count,
        "offline": offline_count,
        "uptime_percentage": f"{uptime_percent:.2f}%"
    }

