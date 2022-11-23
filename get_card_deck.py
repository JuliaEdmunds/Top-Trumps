# Lets the player choose between the card decks
import E_decks
import time
import helpers


def choose_deck():
    deck_values = set(item.value for item in E_decks.Deck)
    deck_choices = ""

    for deck in E_decks.Deck:
        deck_choices += f"{deck.value} {deck.name}\n"
    while True:
        chosen_deck = input(f"You can choose between {len(E_decks.Deck)} different decks of cards:\n{deck_choices}\n"
                            f"Please choose you deck: ")
        try:
            chosen_deck = int(chosen_deck)
        except ValueError:
            print("This is not a valid number...")
            time.sleep(1)
            continue

        if chosen_deck not in deck_values:
            print(f"{chosen_deck} in not a valid card number.")
            time.sleep(1)
            continue

        else:
            print(f"\nGreat you have chosen the {E_decks.Deck(chosen_deck).name} deck. Enjoy the game!")
            time.sleep(3)
            helpers.clear()
            return chosen_deck
