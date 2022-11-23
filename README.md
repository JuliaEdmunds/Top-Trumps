# CFG Top-Trumps Project
 by Team Everest

## Project brief 

### For smooth experience make sure to:
- Check if the Requests module is installed and if not please install it. 
If using pycharm, check in the "Python Packages" (in the bottom taskbar) if "requests" is installed. If not go to the "Terminal" tab (also bottom taskbar), paste "py -m pip install requests" and press enter
- Enable "Emulate terminal in output console" for the main.py file. You can find this under edit configuration of the main file, then it's under Execution option
- Always run the project from main.py 

### Short description
- We have decided to use GitHub as the version control
- Split into files for better readability and avoiding merge conflicts
- ??

## MUST

- [x] Decide on the group name
- [x] Input/hello message - introduction, instruction, num of rounds
- [ ] Get username (also for leader board)
- [x] Generate a random number between 1 and 151 to use as the Pokémon ID number
- [x] Using the Pokémon API get a Pokémon based on its ID number (1st stage)
- [x] Create a dictionary that contains the returned Pokémon's name, id, height and weight and other playing stat we decide on (?https://pokeapi.co/ )
- [x] Get a random Pokémon for the player and another for their opponent
- [x] Ask the user which stat they want to use (height, weight, xp)
- [x] Compare the player's and opponent's Pokémon on the chosen stat to decide who wins


## SHOULD
- [x] Switch ID to base_experience as a fighting stat
- [x] Get 2 random Pokémon and let the player decide which one that they want to use
- [x] Play multiple rounds and record the outcome of each round. The player with the highest number of rounds won, wins the game


## COULD
- [x] Allow the opponent (computer) to choose a stat that they would like to compare
- [ ] Record high scores for players and store them in a file - leaderboard - record 5 top players (names), their scores and the deck they have played with
- [x] Allow the opponent (computer) to get 2 random Pokémon (cards) and let it decide which one to use
- [x] Add another API so the player can choose the deck they want to play with 


## WON'T
❌ Add Pokémon types as fighting stat (would require assignment which Pokémon type wins/loses against which, like in rock paper scissors)
