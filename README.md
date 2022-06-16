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
- As a user, I want the game to be user-friendly

## User Stories 
- As a user, I want to play a game that is straightforward and immediately easy to understand
- As a user, I want to be able to select the difficulty level of the game
- As a user, I want to be alerted to an invalid input and given the chance to re-enter data 
- As a user, I want feedback and hints on my progression
- As a user, I want feedback on whether I have won or lost
- As a user, I want the option to play again 

# Features

## Welcome Message
- The player is greeted with a welcome message, name of the game and a short message explaining the aim of the game.

<h2 align ="center"><img src = "assets/docs/welcome.jpg"></h2>

## Ready to Play
- The player is taken to the next page which asks if they are ready to play and they are then prompted to enter a name.

<h2 align ="center"><img src = "assets/docs/ready.jpg"></h2>

- If the player enters a blank space or non letter character, an error message will alert them that a name is required to play.

<h2 align ="center"><img src = "assets/docs/ready-error.jpg"></h2>


## Select Difficulty Level
- The player is greeted and then asked to select level - easy, medium or hard.

<h2 align ="center"><img src = "assets/docs/level.jpg"></h2>

- If user enters anything other than e, easy, m, medium, h, hard, an error message will alert them to correctly select the level.

<h2 align ="center"><img src = "assets/docs/level-error.jpg"></h2>

## Game Play
- The computer tells the player it is thinking of a number between 1 and 10, 1 and 100 or 1 and 500 depending on the difficulty level selected by the player.  

<h2 align ="center"><img src = "assets/docs/play.jpg"></h2>

- The player will receive hints if their guess needs to be higher or lower

<h2 align ="center"><img src = "assets/docs/hint.jpg"></h2>

- The player will be alerted if they have entered an invalid guess (such as a letter, blank space or character) and they will be prompted to try again.

<h2 align ="center"><img src = "assets/docs/play-error.jpg"></h2>

- If the player runs out of guesses, they lose the game and the correct number is advised.  The computer will also ask if they would like to play again.  

<h2 align ="center"><img src = "assets/docs/lose.jpg"></h2>

- If the player wins the game, a message will appear telling them they got it and however many tries they had.  The computer will also ask if they would like to play again.  

<h2 align ="center"><img src = "assets/docs/win.jpg"></h2>

- If the player selects n for no, the computer will thank the player for playing and say bye.  If they select y for yes, the game will start again from the choose level page.

<h2 align ="center"><img src = "assets/docs/bye.jpg"></h2>








