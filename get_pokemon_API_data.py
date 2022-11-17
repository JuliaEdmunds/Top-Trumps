# Brief: responsible for getting API data
# Functions needed:
#   1) Using the Pokemon API get a Pokemon based on its ID number
#   2) Create a dictionary that contains the returned Pokemon's name, id, height, weight, base_experience and other
#      playing stat we decide on (★https://pokeapi.co/ )

import requests
import random

# Included hardcoded data, so I can test this file in separation (without calling it from "main") for now
min_number = 1
max_number = 151
num_pokemon_ids = 2
hardcoded_ID = random.sample(range(min_number, max_number + 1), num_pokemon_ids)

# Empty stats for 2 pokemons - to be filled with a function -> get_pokemon_info()
first_pokemon_stats = {
    "id": 0,
    "name": " ",
    "height": 0,
    "weight": 0,
    "xp": 0
}

second_pokemon_stats = {
    "id": 0,
    "name": " ",
    "height": 0,
    "weight": 0,
    "xp": 0
}


def get_pokemon_info(pokemon_id, current_dict):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)
    current_pokemon = response.json()
    current_dict["id"] = pokemon_id
    current_dict["name"] = current_pokemon["name"].title()
    current_dict["height"] = current_pokemon["height"]
    current_dict["weight"] = current_pokemon["weight"]
    current_dict["xp"] = current_pokemon["base_experience"]


for i in range(num_pokemon_ids):
    pokemon_number = hardcoded_ID[i]
    if i == 0:
        get_pokemon_info(pokemon_number, first_pokemon_stats)
    else:
        get_pokemon_info(pokemon_number, second_pokemon_stats)
