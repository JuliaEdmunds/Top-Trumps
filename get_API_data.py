# Brief: responsible for getting API data
# Functions needed:
#   1) Using the Pokemon API get a Pokemon based on its ID number
#   2) Create a dictionary (Julia: changed to a class/object) that contains the returned Pokemon's name, id, height,
#   weight, base_experience and other playing stat we decide on (★https://pokeapi.co/ )
#   3) Add 2nd API

import requests
import random
from decimal import *
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
    # of valid ids
    valid_nba_player_ids = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29,
                            30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53,
                            54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78,
                            79, 80, 81, 82, 83, 84, 85, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102,
                            103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 120, 121,
                            122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139,
                            140, 141, 142, 143, 145, 146, 147, 148, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159,
                            160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177,
                            178, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 191, 192, 193, 194, 195, 196, 197,
                            199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216,
                            217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 233, 234, 235,
                            236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 254,
                            255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272,
                            273, 274, 275, 276, 277, 278, 279, 280, 282, 283, 284, 285, 286, 287, 288, 289, 290, 292,
                            293, 294, 295, 296, 297, 298, 299, 300, 302, 303, 304, 305, 306, 307, 308, 310, 313, 314,
                            315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 326, 327, 328, 330, 331, 332, 333, 334,
                            335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 349, 350, 351, 352, 353,
                            354, 355, 356, 357, 358, 359, 360, 361, 361, 362, 363, 364, 365, 366, 367, 369, 370, 371,
                            372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 383, 385, 386, 387, 389, 390, 391, 393,
                            394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411,
                            412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 428, 429, 431,
                            432, 433, 434, 435, 436, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 449, 450, 451,
                            452, 453, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470,
                            471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488,
                            489, 490, 491, 492, 493]
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
