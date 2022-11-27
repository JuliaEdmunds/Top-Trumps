# CFG Top-Trumps Project
 by Team Everest

## Project brief 

### For smooth experience make sure to:
- Check if the requests and pandas modules are installed and if not please install it. 
If using pycharm, check in the "Python Packages" (in the bottom taskbar) if "requests" and "pandas" are installed. If not then go to the "Terminal" tab (also bottom taskbar), paste "py -m pip install requests" and press enter. Repeat for pandas.
In you have any issues please try to Google a solution that will work for you
- Enable "Emulate terminal in output console" for the main.py file. You can find this under edit configuration of the main file, then it's under Execution option
- Always run the project from main.py 

### Version control info
- We have decided to use GitHub for version control and collaboration to enable smooth code-sharing and track changes in the code across versions
- To enable smooth collaboration we have decided to split the project into multiple files for better readability and to avoid merge conflicts

### Used APIs
- We have decided to use multiple APIs in our project to be able to play with different decks of cards
- The first API is the one we have used during the course (https://pokeapi.co/). 
It was quite straightforward to work with as we had enough numerical data to choose for the stats
- We have struggled to find other suitable APIs that have not been disabled and included the numerical data we have been searching for
- We have decided to use https://www.balldontlie.io/ which provided us with 2 additional APIs:
  1. NBA_Games is quite an unusual one but all ids contained valid data we could use
  2. FOr NBA_Player we had to write a small standalone program to extract valid ids we can use for the Top Trumps game

## MUST

- [x] Decide on the group name
- [x] Input/hello message - introduction, instruction, num of rounds
- [x] Get username (also for leader board)
- [x] Generate a random number between 1 and 151 to use as the Pokémon ID number
- [x] Using the Pokémon API get a Pokémon based on its ID number (1st stage)
- [x] Create a dictionary that contains the returned Pokémon's name, id, height and weight and other playing stat we decide on (https://pokeapi.co/)
- [x] Get a random Pokémon for the player and another for their opponent
- [x] Ask the user which stat they want to use (height, weight, xp)
- [x] Compare the player's and opponent's Pokémon on the chosen stat to decide who wins


## SHOULD
- [x] Switch ID to base_experience as a fighting stat for Pokémon
- [x] Get 2 random cards and let the player decide which one that they want to use
- [x] Play multiple rounds and record the outcome of each round. The player with the highest number of rounds won, wins the game
- [x] Add an option for player to decide if they want to play again or not


## COULD
- [x] Allow the opponent (computer) to choose a stat that they would like to compare
- [x] Record high scores for players and store them in a file - leaderboard - record 5 top players (names), their scores and the deck they have played with
- [x] Allow the opponent (computer) to get 2 random cards and let it decide which one to use
- [x] Add more APIs so the player can choose the deck they want to play with 


## WON'T
❌ Add Pokémon types as fighting stat (would require assignment which Pokémon type wins/loses against which, like in rock paper scissors)
