# Brief: responsible for getting API data
# Functions needed:
#   1) Using the Pokemon API get a Pokemon based on its ID number
#   2) Create a dictionary (Julia: changed to a class/object) that contains the returned Pokemon's name, id, height,
#   weight, base_experience and other playing stat we decide on (★https://pokeapi.co/ )
#   3) Add 2nd API

import requests
import random
from trump_card import Card


def get_random_pokemon_ids(num_card_ids):
    # Min and max IDs, number of selected pokemons per player to generate the list of unique Pokemon ids
    min_number = 1
    max_number = 151
    card_ids = random.sample(range(min_number, max_number + 1), num_card_ids)
    return card_ids


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


def get_random_game_ids(num_card_ids):
    # Max nba games IDs currently
    min_number = 1
    max_number = 40000
    card_ids = random.sample(range(min_number, max_number + 1), num_card_ids)
    return card_ids


def get_nba_game_info(game_id):
    current_stats = {}
    url = f"https://www.balldontlie.io/api/v1/games/{game_id}"
    response = requests.get(url)
    current_game = response.json()
    game_name = current_game["home_team"]["full_name"] + " vs " + current_game["visitor_team"]["full_name"]
    current_stats["home score"] = current_game["home_team_score"]
    current_stats["visitor score"] = current_game["visitor_team_score"]
    current_stats["season"] = current_game["season"]
    nba_game_card = Card(game_id, game_name, current_stats)
    return nba_game_card
