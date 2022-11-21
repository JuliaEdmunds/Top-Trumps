# This is our main file and should include as little code as possible (to avoid merge conflicts when working
# together on the project)

# Functions needed:
#   1) Input/hello message & get player's name
#   2) Play multiple rounds using play_round file
#   3) Decide who wins the game (the player with the highest number of rounds won, wins the game)

# I have created files that we can utilize to work on different features of the project (see below example)

import E_scores
import play_round
import time
from os import system, name
import test

test.test_hello_function()


# Starting the "real" code here, for now I have selected these parameters, but we can discuss and change

# Define clear function for windows
def clear():
    # for windows the name is "nt"
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


num_of_rounds = 5
win_points = E_scores.Score.win.value
draw_points = E_scores.Score.draw.value
lost_points = E_scores.Score.lost.value
print(f"""Welcome to Top Trumps. It is a game in which players decide (in alternating order) which stats they want to compare. 
Player with higher stats wins a round. You will play total of {num_of_rounds} rounds. 
Each round you earn points: for win {win_points} points, for draw {draw_points} points and for a lost round {lost_points} point""")
time.sleep(2)

player_score = 0
player_wins = 0
computer_wins = 0

for round_num in range(num_of_rounds):
    current_round = round_num + 1
    current_round_result = play_round.play_round(current_round)
    if current_round_result == E_scores.Score.win:
        player_wins += 1
    elif current_round_result == E_scores.Score.lost:
        computer_wins += 1

    to_print = current_round_result.name
    player_score += current_round_result.value

    print(f"You {to_print}. Current results after {current_round} round/s:"
          f"\nPlayer wins: {player_wins}, points: {player_score}"
          f"\nOpponent wins: {computer_wins}")
    time.sleep(5)
    # Clear the screen for the next round
    clear()

if player_wins > computer_wins:
    print(f"Congrats. You won the game!")
elif player_wins < computer_wins:
    print("Sorry this time you lost the game...")
else:
    print("It's a draw.")
