import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2/"
TOKEN = "5cda374c3642222f50eabe2bf5a76d64"
HEADERS = {
    "trainer_token": TOKEN,
    "Content-Type": "application/json"
}

TRAINER_ID = "4573"  
TRAINER_NAME = "chento"  

def test_get_trainers_status_code():
    response = requests.get(f"{URL}trainers", headers=HEADERS, params={"trainer_id": TRAINER_ID})
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_trainer_name_in_response():
    response = requests.get(f"{URL}trainers", headers=HEADERS, params={"trainer_id": TRAINER_ID})
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    response_data = response.json()
    assert TRAINER_NAME in response_data["name"], f"Expected trainer name {TRAINER_NAME}, but got {response_data['name']}"

