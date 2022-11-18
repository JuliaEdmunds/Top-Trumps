# Brief: responsible for getting API data
# Functions needed:
#   1) Using the Pokemon API get a Pokemon based on its ID number
#   2) Create a dictionary (Julia: changed to a class/object) that contains the returned Pokemon's name, id, height,
#   weight, base_experience and other playing stat we decide on (★https://pokeapi.co/ )

import requests
from pokemon_card import Pokemon


def get_pokemon_info(pokemon_id):
    current_stats = {}
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)
    current_pokemon = response.json()
    pokemon_name = current_pokemon["name"].title()
    current_stats["height"] = current_pokemon["height"]
    current_stats["weight"] = current_pokemon["weight"]
    current_stats["xp"] = current_pokemon["base_experience"]
    pokemon_card = Pokemon(pokemon_id, pokemon_name, current_stats)
    return pokemon_card



