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
import helpers

player_cards = []
computer_cards = []


def get_card_data(deck_num):
    num_card_ids = 4

    if deck_num == 1:
        card_ids = get_API_data.get_random_pokemon_ids(num_card_ids)
        get_matching_card_data = get_API_data.get_pokemon_info
    else:
        card_ids = get_API_data.get_random_game_ids(num_card_ids)
        get_matching_card_data = get_API_data.get_nba_game_info

    # Getting card info and assigning them to Player's and computer's stacks
    for i in range(num_card_ids):
        card_number = card_ids[i]
        next_card = get_matching_card_data(card_number)
        if i <= 1:
            player_cards.append(next_card)
        else:
            computer_cards.append(next_card)


def choose_player_card():
    min_num = 1
    max_num = 2
    while True:
        first_to_print = player_cards[0]
        second_to_print = player_cards[1]
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
            helpers.clear()
            return player_cards[card_to_keep - 1]


def choose_computer_card():
    # For now computer chooses the card based on max value (usually weight for pokemon), to improve the app we would
    # have it recognize min and max of each trait, so it would choose highest normalized value
    first_card_max_stat = max(computer_cards[0].stats.values())
    second_card_max_stat = max(computer_cards[1].stats.values())

    if first_card_max_stat > second_card_max_stat:
        return computer_cards[0]
    else:
        return computer_cards[1]


def player_choose_stat(card):
    to_print = ", ".join(f'{key}: {value}' for key, value in card.stats.items())
    to_print_stats = "/".join(card.stats.keys())
    stat_chosen = input(f"Your card stats are: {to_print}\n"
                        f"\nDecide which trait you would like to play with: {to_print_stats}? ").lower().strip()
    while stat_chosen not in card.stats:
        stat_chosen = input(f"Please choose a valid trait: {to_print_stats}! ").lower().strip()

    return stat_chosen


def check_score(player_card, computer_card, fighting_stat):
    player_power = player_card.stats[f"{fighting_stat}"]
    if player_power == "unknown" or player_power == "n/a":
        player_power = random.randint(0, 1000)
    computer_power = computer_card.stats[f"{fighting_stat}"]
    if computer_power == "unknown" or computer_power == "n/a":
        computer_power = random.randint(0, 1000)
    helpers.clear()
    print(f"You are fighting with {fighting_stat}! Do you think that {player_card.name} can beat your opponent?")
    time.sleep(2)
    print(f"\nYour opponent plays {computer_card.name}! Let's compare your stats:\n\nYour {fighting_stat}: {player_power}"
          f"\nOpponent's {fighting_stat}: {computer_power}\n")
    time.sleep(4)
    if player_power > computer_power:
        print(f"Your {player_card.name} wins! You gain {E_scores.Score.win.value} points!")
        time.sleep(4)
        return E_scores.Score.win
    elif player_power < computer_power:
        print(f"Opponent's {computer_card.name} wins! You score {E_scores.Score.lost.value} point...")
        time.sleep(4)
        return E_scores.Score.lost
    else:
        print(f"It's a draw! You gain {E_scores.Score.draw.value} points.")
        time.sleep(4)
        return E_scores.Score.draw


# This is a function to call from main to play round, takes the round number and the deck number
def play_round(current_round_num, deck_num):
    global player_cards, computer_cards
    is_player_choosing_stats = current_round_num % 2 != 0
    helpers.clear()
    text_to_print = f"\nRound {current_round_num}, fight!"
    if is_player_choosing_stats:
        text_to_print += " (this round the player chooses the fighting trait)\n"
        print(text_to_print)
    else:
        text_to_print += " (this round the opponent chooses the fighting trait)\n"
        print(text_to_print)
    # TODO: currently hardcoded
    get_card_data(deck_num)
    players_card = choose_player_card()
    computers_card = choose_computer_card()
    # Player starts and then player and computer alternate in choosing the fighting stat
    if is_player_choosing_stats:
        current_stat = player_choose_stat(players_card)
    else:
        # For now computer chooses the stat based on max value (usually weight), to improve we would have in recognize
        # min and max of each trait, so it would choose highest normalized value
        current_stat_max = max(computers_card.stats.values())
        current_stat = (list(computers_card.stats.keys())[list(computers_card.stats.values()).index(current_stat_max)])

    # Reset and update variables ready for the next round
    player_cards.clear()
    computer_cards.clear()

    return check_score(players_card, computers_card, current_stat)
