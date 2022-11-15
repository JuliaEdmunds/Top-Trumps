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