# 🌐 Internet Speed Logger API

A lightweight FastAPI-based project to monitor and log internet speed. This API measures download and upload speeds, logs them, and provides endpoints to retrieve historical speed data. Ideal for tracking internet performance over time.

---

## 📁 Project Structure

. ├── pycache/ # Compiled Python files ├── logs/ # Directory to store log files ├── tests/ │ └── test_speed_api.py # Unit tests for the API ├── utils/ │ ├── pycache/ │ └── speed_checker.py # Utility for checking internet speed ├── venv/ # Virtual environment (not tracked in Git) ├── .gitignore # Specifies files/folders to be ignored by Git ├── main.py # Entry point of the FastAPI application ├── README.md # Project documentation ├── requirements.txt # List of dependencies


---

## 🚀 Features

- Measure **download** and **upload** speeds.
- Log internet speed data in a structured format.
- API endpoints to trigger speed checks and view results.
- Modular code with utility and test separation.
- Lightweight and fast using **FastAPI**.

---

## 🛠️ Setup & Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/internet-speed-logger.git
cd internet-speed-logger

Create and activate a virtual environment

python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run the FastAPI app

uvicorn main:app --reload

Running Tests
To run tests located in the tests/ directory:

pytest tests/

📌 API Endpoints

Method	Endpoint	Description
GET	/	Welcome message
GET	/check-speed	Runs a speed test and returns download/upload MBps

📡 Example Usage
🔹 1. Test the API with curl
Get welcome message:

curl http://127.0.0.1:8000/
Trigger internet speed check:

curl http://127.0.0.1:8000/check-speed
🔹 2. Test the API with Postman
Open Postman.

Create a GET request to: http://127.0.0.1:8000/check-speed

Click Send.

You’ll get a response like:

{
  "download_speed_mbps": 47.36,
  "upload_speed_mbps": 18.92
}
🧰 Tech Stack
Python 3.9+

FastAPI – API framework

Uvicorn – ASGI server

Speedtest-cli – Internet speed test tool

Pytest – Testing framework