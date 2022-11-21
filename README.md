# Top-Trumps
 Team Everest Project

## MUST

- [x] Decide on the group name
- [x] Input/hello message - introduction, instruction, num of rounds
- [ ] Get user name (also for leader board)
- [x] Generate a random number between 1 and 151 to use as the Pokemon ID number
- [x] Using the Pokemon API get a Pokemon based on its ID number (1st stage)
- [x] Create a dictionary that contains the returned Pokemon's name, id, height and weight and other playing stat we decide on (?https://pokeapi.co/ )
- [x] Get a random Pokemon for the player and another for their opponent
- [x] Ask the user which stat they want to use (height, weight, xp)
- [x] Compare the player's and opponent's Pokemon on the chosen stat to decide who wins


## SHOULD
- [x] Switch ID to base_experience as a fighting stat
- [x] Get 2 random Pokemon and let the player decide which one that they want to use
- [x] Play multiple rounds and record the outcome of each round. The player with most number of rounds won, wins the game


## COULD
- [x] Allow the opponent (computer) to choose a stat that they would like to compare
- [ ] Record high scores for players and store them in a file - leader board - record 5 top players (names) & their scores
- [x] Allow the opponent (computer) to get 2 random Pokemon and let it decide which one to use


## WON'T
- [ ] Switch to a different API (@Marta: I would like to add this as an option to choose a deck. What do you think?)
- [ ] Add (types -> type -> name) as a fighting stat (more complex)
