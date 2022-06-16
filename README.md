<h1 align="center">NUMBER GUESSING GAME</h1>

Number Guessing Game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Players can try to guess a number that the computer randomly generates.  There are 3 difficulty levels the player can choose to play - easy, medium or hard.  

The live site can be found [here](https://guessing-game-pp3.herokuapp.com/)

<h2 align ="center"><img src = "assets/docs/am-i-responsive-gg.jpg"></h2>


# How to play

The game is between the computer and 1 player.  The player must enter a name and then select the difficulty level (easy, medium or hard).  The computer will then think of a random number within a known range and the user has to guess the correct number within a limited amount of tries.  Whether they lose or win, they will be asked if they would like to play again.  

# Design

## Flowchart

<h2 align ="center"><img src = "assets/docs/flowchart.jpg"></h2>


# User Experience

## User Goals
- As a user, I want to play a fun guessing game
- As a user, I want to choose how challenging I want the game to be 

## User Stories 
- As a user, I want to play a game that is straightforward and immediately easy to understand
- As a user, I want to be able to select the difficulty level of the game
- As a user, I want feedback and hints on my progression
- As a user, I want feedback on whether I have won or lost
- As a user, I want the option to play again 

# Features

## Existing Features

### Welcome Message
- The player is greeted with a welcome message and the name of the game.

<h2 align ="center"><img src = "assets/docs/welcome.jpg"></h2>

### Ready to Play
- The player is taken to the next page which asks if they are ready to play and they are then prompted to enter a name.
- If the user enters a number or a blank space, an error message will alert them that a name is required to play.

### Select Difficulty Level
- The player is greeted and then asked to select level - easy, medium or hard.
- If user enters anything other than e, easy, m, medium, h, hard, an error message will alert them to correctly select the level.





