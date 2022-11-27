# Brief: responsible for getting API data
# Functions needed:
#   1) Using the Pokémon API get a Pokémon based on its ID number
#   2) Create a dictionary (Julia: changed to a class/object) that contains the returned Pokémon name, id, height,
#   weight, base_experience and other playing stat we decide on (★https://pokeapi.co/ )
#   3) Add 2nd API

import requests
import random
from trump_card import Card


def get_random_pokemon_ids(num_card_ids):
    # Min and max IDs, number of selected Pokémon per player to generate the list of unique Pokémon ids
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


def get_random_nba_player_ids(num_card_ids):
    # Since not all nba players have valid stats I have run a standalone get_valid_api_ids for this API to get the list
    # of valid ids and saved it in a text file
    with open("valid_nba_player_ids.txt", "r") as valid_nba_player_ids_string:
        contents = valid_nba_player_ids_string.read()

    # Converting text file string into a list of ints
    list_of_ids_as_strings = contents.split(", ")
    valid_nba_player_ids = [eval(i) for i in list_of_ids_as_strings]

    card_ids = random.sample(valid_nba_player_ids, num_card_ids)
    return card_ids


def get_nba_player_info(nba_player_id):
    current_stats = {}
    url = f"https://www.balldontlie.io/api/v1/players/{nba_player_id}"
    response = requests.get(url)
    current_player = response.json()
    current_player_name = current_player["first_name"] + " " + current_player["last_name"]
    height_feet = current_player["height_feet"]
    height_inches = current_player["height_inches"]
    height_in_cm = height_feet * 30.48 + height_inches * 2.54
    current_stats["height"] = round(height_in_cm, 2)
    weight_in_kg = current_player["weight_pounds"] / 2.205
    current_stats["weight"] = round(weight_in_kg, 2)
    current_stats["team id"] = current_player["team"]["id"]
    nba_player_card = Card(nba_player_id, current_player_name, current_stats)
    return nba_player_card


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
