# CFG Top-Trumps Project
 by Team Everest

## Project goal
Final project for the Code Fist Girls Introduction to Python & Apps. 

## Project description
Top Trumps is a game in which players draw cards and decide (in alternating order) which stats they want to compare. Both the Player and simple AI get 2 random cards and need to decide which one they want to use in the battle. The player with higher stats wins a round.

## For smooth experience make sure to implement these steps:
### 1. Packages
Check if the following modules are installed:
1. requests 
2. tabulate 

If using pycharm, check in the "Python Packages" (in the bottom taskbar). If they are not installed then go to the "Terminal" tab (also bottom taskbar), paste "pip install requests" and press enter. Repeat for other modules.
If you have any issues please try to Google a solution that will work for you

### 2. Emulate terminal
Enable "Emulate terminal in output console" for the main.py file:
  1. Right-click main.py
  2. Select "Modify Run Configuration" 
  3. Then it's under Execution option

### 3. Run configurations
Always run the project from main.py 

## Version control info
- We have decided to use GitHub for version control and collaboration to enable smooth code-sharing and tracking changes in the code across versions
- To mitigate merge conflicts and to enhance readability we have decided to split the project into multiple files

## Used APIs
We have decided to use multiple APIs in our project to be able to play with different decks of cards. Aside from Pokémon, we have struggled to find other suitable APIs that have not been disabled and included the numerical data we have been searching for
### Pokémon
The first API is the one we have used during the course (https://pokeapi.co/). It was quite straightforward to work with as we had enough numerical data to choose for the stats
### NBA_Games
We used https://www.balldontlie.io/ for NBA_Games. It is quite an unusual one but all ids contained valid data we could use
### NBA_Players
We used https://www.balldontlie.io/ also for NBA_Players. We had to write a small standalone program to extract valid ids we can use for the Top Trumps game. 
Also, we have switched height and weight from imperial to metric units 

## Tasks
We decided to break the project into smaller tasks using the MSCW system

### MUST

- [x] Decide on the group name
- [x] Input/hello message - introduction, instruction, num of rounds
- [x] Get username (also for leader board)
- [x] Generate a random number between 1 and 151 to use as the Pokémon ID number
- [x] Using the Pokémon API get a Pokémon based on its ID number (1st stage)
- [x] Create a dictionary that contains the returned Pokémon's name, id, height and weight and other playing stat we decide on (https://pokeapi.co/)
- [x] Get a random Pokémon for the player and another for their opponent
- [x] Ask the user which stat they want to use (height, weight, xp)
- [x] Compare the player's and opponent's Pokémon on the chosen stat to decide who wins


### SHOULD
- [x] Switch ID to base_experience as a fighting stat for Pokémon
- [x] Get 2 random cards and let the player decide which one that they want to use
- [x] Play multiple rounds and record the outcome of each round. The player with the highest number of rounds won, wins the game
- [x] Add an option for player to decide if they want to play again or not


### COULD
- [x] Allow the opponent (computer) to choose a stat that they would like to compare
- [x] Record high scores for players and store them in a file - leaderboard - record 5 top players (names), their scores and the deck they have played with
- [x] Allow the opponent (computer) to get 2 random cards and let it decide which one to use
- [x] Add more APIs so the player can choose the deck they want to play with 


### WON'T
❌ Add Pokémon types as fighting stat (would require assignment which Pokémon type wins/loses against which, like in rock paper scissors)

## Future work
Given more time we would have included the following things:
- Add additional APIs
- Add a GUI
- For now computer chooses the card based on the max value (usually weight for Pokémon, height for NBA_Players and season for NBA_Games). 
Given more time, we would have computer recognize the min and max values of each trait, so it would choose highest normalized value.
