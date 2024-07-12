import requests

URL = "https://api.pokemonbattle.ru/v2/"

HEADERS = {
    "trainer_token": "5cda374c3642222f50eabe2bf5a76d64",  
    "Content-Type": "application/json"
}

# Создание покемона
create_pokemon_url = f"{URL}pokemons"
create_pokemon_payload = {
    "name": "Buba",
    "photo_id": 1
}

response_create = requests.post(create_pokemon_url, headers=HEADERS, json=create_pokemon_payload)
print(response_create.json())

pokemon_id = response_create.json().get("id")

# Смена имени покемона
update_pokemon_url = f"{URL}pokemons"
update_pokemon_payload = {
    "pokemon_id": pokemon_id,
    "name": "NewBuba"
}

response_update = requests.put(update_pokemon_url, headers=HEADERS, json=update_pokemon_payload)
print(response_update.json())

# Поймать покемона в покебол
catch_pokemon_url = f"{URL}trainers/add_pokeball"
catch_pokemon_payload = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(catch_pokemon_url, headers=HEADERS, json=catch_pokemon_payload)
print(response_catch.json())
