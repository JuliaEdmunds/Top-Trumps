# Brief: play a round of the game
# Functions needed:
#   1) Get a random Pokemon for the player and another for their opponent passing random ID into get_API_data file
#      (Generate a random number between 1 and 151 to use as the Pokemon ID number)
#       SHOULD: Get 2 random Pokemon and let the player decide which one that they want to use
#       COULD: Allow the opponent (computer) to get 2 random Pokemon and let it decide which one to use
#   2) Ask the user which stat they want to use (id, height or weight) (players always goes 1st)
#      COULD: Allow the opponent (computer) to choose a stat that they would like to compare (alternating starting order)
#   3) Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
#   4) Record the outcome of each round (who won)

import random
import time
import get_pokemon_API_data

# Dictionaries for 4 pokemons - to be filled with a function -> get_pokemon_info()
player_first_pokemon = {"id": 0, "name": " ", "height": 0, "weight": 0, "xp": 0}
player_second_pokemon = {"id": 0, "name": " ", "height": 0, "weight": 0, "xp": 0}
computer_first_pokemon = {"id": 0, "name": " ", "height": 0, "weight": 0, "xp": 0}
computer_second_pokemon = {"id": 0, "name": " ", "height": 0, "weight": 0, "xp": 0}

player_pokemons = []
computer_pokemons = []


def strip_to_raw_stats(card_info):
    card_info.pop("id")
    card_info.pop("name")
    return card_info


def get_pokemons_data():
    min_number = 1
    max_number = 151
    num_pokemon_ids = 4
    pokemon_ids = random.sample(range(min_number, max_number + 1), num_pokemon_ids)

    for i in range(num_pokemon_ids):
        pokemon_number = pokemon_ids[i]
        if i == 0:
            get_pokemon_API_data.get_pokemon_info(pokemon_number, player_first_pokemon)
            # TO DO: I don't understand why "player_first_pokemon" was changed
            raw_stats = strip_to_raw_stats(player_first_pokemon)
            player_pokemons.append(raw_stats)
        elif i == 1:
            get_pokemon_API_data.get_pokemon_info(pokemon_number, player_second_pokemon)
            raw_stats = strip_to_raw_stats(player_second_pokemon)
            player_pokemons.append(raw_stats)
        elif i == 2:
            get_pokemon_API_data.get_pokemon_info(pokemon_number, computer_first_pokemon)
            raw_stats = strip_to_raw_stats(computer_first_pokemon)
            computer_pokemons.append(raw_stats)
        else:
            get_pokemon_API_data.get_pokemon_info(pokemon_number, computer_second_pokemon)
            raw_stats = strip_to_raw_stats(computer_second_pokemon)
            computer_pokemons.append(raw_stats)


def choose_a_card():
    min_num = 1
    max_num = 2
    while True:
        first_to_print = ", ".join(f'{key}: {value}' for key, value in player_first_pokemon.items())
        second_to_print = ", ".join(f'{key}: {value}' for key, value in player_second_pokemon.items())
        card_to_keep = input(f"You can choose between two cards. Look at the stats and think carefully which one you "
                             f"want to keep:\n1. {first_to_print}\n2. {second_to_print}\nThe card you don't choose "
                             f"will be discarded. So do you want to keep card 1 or 2? ")
        try:
            card_to_keep = int(card_to_keep)
        except ValueError:
            print("This is not a valid number...")
            time.sleep(1)
            continue

        if card_to_keep < min_num or card_to_keep > max_num:
            print(f"{card_to_keep} in not a valid card number.")
            time.sleep(1)
            continue

        else:
            return player_pokemons[card_to_keep - 1]


# def play_game():
get_pokemons_data()
players_card = choose_a_card()
computers_card = max(computer_pokemons, key=lambda x: list(x.values()))

print(player_pokemons)
print(players_card)
print(computer_pokemons)
print(computers_card)
