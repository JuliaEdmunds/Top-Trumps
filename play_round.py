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
import E_scores
import get_API_data

player_pokemons = []
computer_pokemons = []


def get_pokemons_data():
    # Min and max IDs, number of selected pokemons per player to generate the list of unique Pokemon ids
    min_number = 1
    max_number = 151
    num_pokemon_ids = 4
    pokemon_ids = random.sample(range(min_number, max_number + 1), num_pokemon_ids)

    # Getting pokemom info and assigning them to Player's and computer's stacks
    for i in range(num_pokemon_ids):
        pokemon_number = pokemon_ids[i]
        next_pokemon = get_API_data.get_pokemon_info(pokemon_number)
        if i <= 1:
            player_pokemons.append(next_pokemon)
        else:
            computer_pokemons.append(next_pokemon)


def choose_player_card():
    min_num = 1
    max_num = 2
    while True:
        first_to_print = player_pokemons[0]
        second_to_print = player_pokemons[1]
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


def choose_computer_card():
    first_pokemon_max_stat = max(computer_pokemons[0].stats.values())
    second_pokemon_max_stat = max(computer_pokemons[1].stats.values())

    if first_pokemon_max_stat > second_pokemon_max_stat:
        return computer_pokemons[0]
    else:
        return computer_pokemons[1]


def player_choose_stat(card):
    to_print = ", ".join(f'{key}: {value}' for key, value in card.stats.items())
    to_print_stats = "/".join(card.stats.keys())
    stat_chosen = input(f"Your pokemon stats are:\n{to_print}\n"
                        f"Decide which characteristic you would like to play with: {to_print_stats}? ").lower().strip()
    while stat_chosen not in card.stats:
        stat_chosen = input(f"Please choose a valid characteristic: {to_print_stats}! ").lower().strip()

    return stat_chosen


def check_score(player_card, computer_card, fighting_stat):
    player_power = player_card.stats[f"{fighting_stat}"]
    computer_power = computer_card.stats[f"{fighting_stat}"]
    print(f"You are fighting with {fighting_stat}! Do you think that {player_card.name} can beat your opponent?")
    time.sleep(1)
    print(f"Your opponent plays {computer_card.name}! Let's compare your stats:\nYour {fighting_stat}: {player_power}"
          f"\nOpponent's {fighting_stat}: {computer_power}")
    if player_power > computer_power:
        print(f"Your {player_card.name} wins! You gain {E_scores.Score.win.value} points :D")
        return E_scores.Score.win.value
    elif player_power < computer_power:
        print(f"Opponent's {computer_card.name} wins! You score {E_scores.Score.lost.value} point :(")
        return E_scores.Score.lost.value
    else:
        print(f"It's a draw! You gain {E_scores.Score.draw.value} points.")
        return E_scores.Score.draw.value


# This is a function to call from main to play round
def play_round(current_round_num):
    global player_pokemons, computer_pokemons
    print(f"Round {current_round_num}, fight!")
    get_pokemons_data()
    players_card = choose_player_card()
    computers_card = choose_computer_card()
    # Player starts and then player and computer alternate in choosing the fighting stat
    if current_round_num % 2 != 0:
        current_stat = player_choose_stat(players_card)
    else:
        current_stat_max = max(computers_card.stats.values())
        current_stat = (list(computers_card.stats.keys())[list(computers_card.stats.values()).index(current_stat_max)])

    # Reset and update variables ready for the next round
    player_pokemons.clear()
    computer_pokemons.clear()
    current_round_num += 1

    return check_score(players_card, computers_card, current_stat)
