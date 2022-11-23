# Lets the player choose between 2 card decks: Pokemon (1) or NBA (2)
import E_decks
import time
import helpers


def choose_deck():
    pokemon_deck_name = E_decks.Deck.Pokemon.name
    pokemon_deck_value = E_decks.Deck.Pokemon.value
    nba_deck_name = E_decks.Deck.NBA.name
    nba_deck_value = E_decks.Deck.NBA.value
    while True:
        chosen_deck = input(f"You can choose between 2 different decks of cards: {pokemon_deck_name} (recommended for "
                            f"easier playthrough) or {nba_deck_name} (recommended for more advanced players).\nPlease "
                            f"type {pokemon_deck_value} for {pokemon_deck_name} deck or {nba_deck_value} for "
                            f"{nba_deck_name} deck ")
        try:
            chosen_deck = int(chosen_deck)
        except ValueError:
            print("This is not a valid number...")
            time.sleep(1)
            continue

        if chosen_deck < pokemon_deck_value or chosen_deck > nba_deck_value:
            print(f"{chosen_deck} in not a valid card number.")
            time.sleep(1)
            continue

        else:
            helpers.clear()
            return chosen_deck
