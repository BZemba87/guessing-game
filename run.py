import random 
number = random.randint(1, 100)

player_name = input("Ready to play?  Please enter your name: \n")
number_of_guesses = 0
print(''+ player_name+ ', I am thinking of a number between 1 and 100, can you guess what it is?')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low!')
    if guess > number:
        print('Your guess is too high!')
    if guess == number:
        break