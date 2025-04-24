from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_speed():
    response = client.get("/speed")
    assert response.status_code == 200
    assert "download_speed_mbps" in response.json()
    assert "upload_speed_mbps" in response.json()
