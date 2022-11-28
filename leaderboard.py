# Here we need to write to a csv file the name and score of the winner if it's within the top 5 scores
# Create following functions:
#   1) Check if the score is eligible to show in the leaderboard
#   2) Write current name, score and deck (either Pokémon or NBA) to a leaderboard (sort by score) - comment update

import csv
import helpers
import time
import tabulate
import E_decks


def table_print(dataset):
    header = dataset[0].keys()
    rows = [x.values() for x in dataset]
    print(tabulate.tabulate(rows, header))

# TODO: Change so you see the leaderboard only once either with your score or just to see current scores


def check_if_leader(player_name, deck_id, current_score):
    deck_name = E_decks.Deck(deck_id).name

    with open("leaderboard_data.csv", "r") as leaderboard_csv:
        leader_data = csv.DictReader(leaderboard_csv)

        # Sort scores in the descending order
        sorted_leaderboard = sorted(leader_data, key=lambda item: int(item["Score"]), reverse=True)

        helpers.clear()
        print("\nHere is the current leaderboard:")
        table_print(sorted_leaderboard)
        time.sleep(5)

        # Grab last (lowest) leader entry from the sorted list
        lowest_score = int(sorted_leaderboard[-1]["Score"])

        # Check if new score makes it to the leaderboard and if yes amend the leaderboard
        if current_score > lowest_score:
            print(f"\nCongrats {player_name}. You made it to the leaderboard with your total score of {current_score} "
                  f"points!")
            del sorted_leaderboard[-1]

            new_leader_entry = {"Name": player_name,
                                "Deck": deck_name,
                                "Score": current_score}

            sorted_leaderboard.append(new_leader_entry)

            # TODO: Sort here before writing

            # Save new entries to the leaderboard
            keys = sorted_leaderboard[0].keys()
            with open("leaderboard_data.csv", "w", newline="") as updated_leaderboard_csv:
                dict_writer = csv.DictWriter(updated_leaderboard_csv, keys)
                dict_writer.writeheader()
                dict_writer.writerows(sorted_leaderboard)

            time.sleep(2)
            helpers.clear()

            # Open new updated csv with the new leader scores
            with open("leaderboard_data.csv", "r") as updated_leaderboard_csv:
                updated_data = csv.DictReader(updated_leaderboard_csv)

                # Sort scores in the descending order
                updated_leaderboard = sorted(updated_data, key=lambda item: int(item["Score"]), reverse=True)

                print("\nHere is the new leaderboard with your score:")
                table_print(updated_leaderboard)
        else:
            print(f"Sorry {player_name}, with total score of {current_score} you did not make it to the leaderboard.")


# Code to test when running just this file
if __name__ == "__main__":
    check_if_leader("Player1", 1, 2)
    check_if_leader("Player2", 2, 1)
    check_if_leader("Player3", 3, -6)

