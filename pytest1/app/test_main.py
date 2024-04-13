# pytest1/tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)



def test_create_user():
    user_data = {
        "id": 7,
        "first_name": "John",
        "last_name": "Doe",
        "gender": "Male",
        "password": "password",
        "username": "test1",
        "status": "active",
        "create_at": "2024-04-12"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201

def test_read_user():
    response = client.get("/users/3")
    assert response.status_code == 404  # Assuming user with ID 1 does not exist initially

def test_delete_user():
    response = client.delete('user/55')
    assert response.status_code == 404

def test_update_user():
    user_data = {
        "id": 44,
        "first_name": "John",
        "last_name": "Doe",
        "gender": "Male",
        "password": "password",
        "username": "24244",
        "status": "active",
        "create_at": "2024-04-12"
    }
    response = client.put("/user/3", json=user_data)
    assert response.status_code == 404

