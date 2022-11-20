# This is our main file and should include as little code as possible (so we do not have merge conflicts when working
# together on the project)

# Functions needed:
#   1) Input/hello message & get player's name
#   2) Play multiple rounds using play_round file
#   3) Decide who wins the game (the player with most number of rounds won, wins the game)

# I have created files that we can utilize to work on different features of the project (see below example)

import E_scores
import test

test.test_hello_function()

# Starting the "real" code here, for now I have selected these parameters, but we can discuss and change
num_of_rounds = 5
win_points = E_scores.Score.win.value
draw_points = E_scores.Score.draw.value
lost_points = E_scores.Score.lost.value
print(f"""Welcome to Top Trumps. It is a game in which players decide which stats they want to compare. 
Player with higher stats wins a round. You will play total of {num_of_rounds} rounds. 
Each round you earn points: for win {win_points} points, for draw {draw_points} points 
and for a lost round {lost_points} point""")
