# Here we need to write to a csv file the name and score of the winner if it's within the top 5 scores
# Create following functions:
#   1) Check if the score is eligible to show in the leaderboard
#   2) Write current name, score and deck (either Pokémon or NBA) to a leaderboard (sort by score) - comment update

# Make sure you can import pandas package
import pandas as pd
import csv


def sort_leaderboard(leaderboard):
    # Sort data (In pandas axis = 0 refers to horizontal axis (rows), inplace=True makes changes to the original
    # dataframe
    leaderboard.sort_values(["Score"],
                            axis=0,
                            ascending=[False],
                            inplace=True)


def check_if_leader(player_name, deck_name, current_score):
    # Assigning dataset
    leaderboard_csv_data = pd.read_csv("leaderboard_data.csv")

    # Sort before printing
    sort_leaderboard(leaderboard_csv_data)

    print(f"Here is the current leaderboard:\n{leaderboard_csv_data.to_string(index=False)}")

    # Check the lowest score (last column, last row) to check if the player makes it to the leaderboard
    lowest_score = leaderboard_csv_data.iloc[-1, -1]

    if current_score > lowest_score:
        print(f"Congrats {player_name}. You made it to the leaderboard with your total score of {current_score} points!")
        leaderboard_csv_data.iloc[-1, leaderboard_csv_data.columns.get_loc("Name")] = player_name
        leaderboard_csv_data.iloc[-1, leaderboard_csv_data.columns.get_loc("Deck")] = deck_name
        leaderboard_csv_data.iloc[-1, leaderboard_csv_data.columns.get_loc("Score")] = current_score

        # Sort before printing
        sort_leaderboard(leaderboard_csv_data)
        leaderboard_csv_data.to_csv("leaderboard_data.csv", index=False)
        print(leaderboard_csv_data.to_string(index=False))

    else:
        print(f"Sorry {player_name}, with total score of {current_score} you did not make it to the leaderboard.")


if __name__ == "__main__":
    player = "Julia"
    deck = "Pokemon"
    score = 2

    check_if_leader(player, deck, score)
