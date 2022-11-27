# Here we need to write to a csv file the name and score of the winner if it's within the top 5 scores
# Create following functions:
#   1) Check if the score is eligible to show in the leaderboard
#   2) Write current name, score and deck (either Pokémon or NBA) to a leaderboard (sort by score) - comment update

# Make sure you can import pandas package
import pandas as pandasForSortingCSV
import csv


if __name__ == "__main__":
    player_name = "Julia"
    score = 2
    deck = "Pokemon"


def check_if_leader():
    # Assigning dataset
    leaderboard_csv_data = pandasForSortingCSV.read_csv("leaderboard_data.csv")

    # Sort data (In pandas axis = 0 refers to horizontal axis (rows), inplace=True makes changes to the original df
    leaderboard_csv_data.sort_values(["Score"],
                                     axis=0,
                                     ascending=[False],
                                     inplace=True)

    print(leaderboard_csv_data)
    # with open("leaderboard_data.csv", "r") as leaderboard_csv:


check_if_leader()
