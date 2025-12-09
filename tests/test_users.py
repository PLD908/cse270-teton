import requests

BASE_URL = "http://127.0.0.1:8000/users/"

def test_valid_admin_credentials():
    """
    Test 1:
    Call /users/?username=admin&password=qwerty
    Expect HTTP 200
    """
    params = {
        "username": "admin",
        "password": "qwerty"
    }
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 200


def test_invalid_admin_credentials():
    """
    Test 2:
    Call /users/?username=admin&password=admin
    Expect HTTP 401
    """
    params = {
        "username": "admin",
        "password": "admin"
    }
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 401