import random 

print('Welcome to the Number Guessing Game!')

number = random.randint(1, 10) #random number generated between 1 and 10

player_name = input("Ready to play?  Please enter your name: \n")
guess = None #players current guess
number_of_guesses = 0 #keeps track of players current guess
guessed = False #keeps track of whether or not the player has guessed the number

print(''+ player_name+ ', I am thinking of a number between 1 and 10, can you guess what it is?')


while(not guessed):
    guess = input()
    number_of_guesses += 1 #increments the number of guesses    
    if number_of_guesses == 5: #number of guesses limited to 5  
        print('You have run out of guesses!') #executes if player reaches 5 guesses

    if guess.isdigit(): #checks player input is a number
        guess = int(guess) #converting guess into integer value
        

    
        if guess < number:
            print('Your guess is too low!') #hints to player that the number is higher
        elif guess > number:
            print('Your guess is too high!') #hints to player that the number is lower 
        else:
            guessed = True #player has guessed correct number
    
    else:
        print('Must enter a number!  Try again.') #executes when player entry is invalid ie not a number

print('Yay, you got it!  You guessed it in '+ str(number_of_guesses) + ' tries!') #executes when player guesses correct number


