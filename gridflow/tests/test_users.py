from fastapi.testclient import TestClient
from gridflow.main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/",
        json={"name": "Alice", "email": "alice@example.com", "password": "test123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "alice@example.com"
    assert "id" in data

def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


# def test_list_routes():
#     routes = [r.path for r in app.routes]
#     print("Registered routes:", routes)
#     assert "/users/" in routes