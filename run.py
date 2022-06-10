import random

print('Welcome to the Number Guessing Game!')

number = random.randint(1, 10)  # random number generated between 1 and 10

player_name = input("Ready to play?  Please enter your name: \n")
guess = None  # players current guess
number_of_guesses = 0  # keeps track of players current guess
guessed = False  # tracks whether or not the player has guessed right

print('' + player_name + ', guess a number between 1 and 10!')

while(not guessed):
    guess = input()
    number_of_guesses += 1  # increments the number of guesses
    
    if guess.isdigit():  # checks player input is valid (integer)
        guess = int(guess)  # converting guess into integer value

        if number_of_guesses == 5:  # limits number of player guesses to 5
            print('You have run out of guesses!')
            break  # stops printing hints when guesses run out
        
        if guess < number:
            print('Your guess is too low!')  # hints to player to guess higher
        elif guess > number:
            print('Your guess is too high!')  # hints to player to guess lower
        else:
            guessed = True  # player has guessed correct number
    else:
        print('Must enter a number!  Try again.')  # tells player input invalid
else:
    print('YAY!  You guessed it in ' + str(number_of_guesses) + ' tries!')