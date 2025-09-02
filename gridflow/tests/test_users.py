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
    return data["id"]

def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


# def test_list_routes():
#     routes = [r.path for r in app.routes]
#     print("Registered routes:", routes)
#     assert "/users/" in routes

def test_update_user():
    # First, create a user
    response = client.post(
        "/users/",
        json={"name": "Bob", "email": "bob@example.com", "password": "test456"}
    )
    user_id = response.json()["id"]

    # Now update the user
    response = client.put(
        f"/users/{user_id}",
        json={"name": "Bobby"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Bobby"


def test_delete_user():
    # First, create a user
    response = client.post(
        "/users/",
        json={"name": "Charlie", "email": "charlie@example.com", "password": "test789"}
    )
    user_id = response.json()["id"]

    # Delete the user
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "User deleted successfully"

    # Verify user no longer exists
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404