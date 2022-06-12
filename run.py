import random
import time

print("Welcome to the Number Guessing Game!\n")
time.sleep(1)

def get_name():
    player_name = input("Ready to play?  Please enter your name: \n")
    print("Hello", player_name)
    time.sleep(1)


def play_game():
    level = input('Choose level - E for easy, M for medium or H for hard: \n')
    time.sleep(0.5)

    if level.lower() == "e":
        max_number = 10
        tries = 5
    elif level.lower() == "m":
        max_number = 100
        tries = 8
    elif level.lower()== "h":
        max_number = 500
        tries = 10
    else:
        print("Sorry!  Invalid input, please try again!")
        print(" ")
        play_game()  # stops game from crashing

    number = random.randint(1, max_number)
    print('I am thinking of a number between 1 and ' + str(max_number) + "\n")
    time.sleep(1)

    number_of_guesses = 1
    while number_of_guesses <= tries:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Your guess is too low!")
            time.sleep(1)
            number_of_guesses += 1
        if guess > number:
            print("Your guess is too high!")
            time.sleep(1)
            number_of_guesses += 1
        elif guess == number:
            print('You got it in ' + str(number_of_guesses) + ' tries!')
            return
    else:
        print('You have run out of guesses! The number was', number)
        


def main():
    get_name()
    again = 'y'
    while again.lower() == "y":
        play_game()
        again = input("Would you like to play again?  (y/n): ")
        if again.lower() == "n":
            print("Bye")

if __name__ == "__main__":
    main()








