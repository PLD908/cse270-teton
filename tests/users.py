import requests

BASE_URL = "http://127.0.0.1:8000/users/"

def check_user_credentials(username, password):
    params = {"username": username, "password": password}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("valid", False)

    return False
