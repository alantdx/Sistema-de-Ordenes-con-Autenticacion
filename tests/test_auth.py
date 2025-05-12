from fastapi.testclient import TestClient
from auth_service.main import app

client = TestClient(app)

def test_register_user():
    res = client.post("/register", json={"username": "test", "password": "testpass"})
    assert res.status_code == 200
    assert res.json()["msg"] == "User registered"