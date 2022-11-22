# Brief: responsible for getting API data
# Functions needed:
#   1) Using the Pokemon API get a Pokemon based on its ID number
#   2) Create a dictionary (Julia: changed to a class/object) that contains the returned Pokemon's name, id, height,
#   weight, base_experience and other playing stat we decide on (★https://pokeapi.co/ )
#   3) Add 2nd API

import requests
from trump import Card
# Needs to be removed v
import random


def get_pokemon_info(pokemon_id):
    current_stats = {}
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)
    current_pokemon = response.json()
    pokemon_name = current_pokemon["name"].title()
    current_stats["height"] = current_pokemon["height"]
    current_stats["weight"] = current_pokemon["weight"]
    current_stats["xp"] = current_pokemon["base_experience"]
    pokemon_card = Card(pokemon_id, pokemon_name, current_stats)
    return pokemon_card


def get_starship_info(starship_id):
    current_stats = {}
    url = f"https://swapi.dev/api/starships/{starship_id}"
    response = requests.get(url)
    current_starship = response.json()
    starship_name = current_starship["name"]
    current_stats["cost"] = current_starship["cost_in_credits"]
    current_stats["length"] = current_starship["length"]
    current_stats["speed"] = current_starship["max_atmosphering_speed"]
    current_stats["cargo capacity"] = current_starship["cargo_capacity"]
    starship_card = Card(starship_id, starship_name, current_stats)
    return starship_card


starship_valid_ids = [2, 3, 5, 9, 10, 11, 12, 13, 15, 17, 21, 22, 23, 27, 28, 29, 31, 32, 39, 40, 41, 43, 47, 48,
                      49, 52, 58, 59, 61, 63, 64, 65, 66, 68, 74, 75]

for i in range(len(starship_valid_ids)):
    card_number = starship_valid_ids[i]
    next_card = get_starship_info(card_number)
    print(next_card)
