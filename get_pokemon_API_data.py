# Brief: responsible for getting API data
# Functions needed:
#   1) Using the Pokemon API get a Pokemon based on its ID number
#   2) Create a dictionary that contains the returned Pokemon's name, id, height, weight, base_experience and other
#      playing stat we decide on (★https://pokeapi.co/ )

import requests


def get_pokemon_info(pokemon_id, current_dict):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)
    current_pokemon = response.json()
    current_dict["id"] = pokemon_id
    current_dict["name"] = current_pokemon["name"].title()
    current_dict["height"] = current_pokemon["height"]
    current_dict["weight"] = current_pokemon["weight"]
    current_dict["xp"] = current_pokemon["base_experience"]



