import random
import time
import os


def clear_screen():
    """
    clears screen after every input and output
    """
    os.system('cls' if os.name == 'nt' else 'clear')


print("Welcome to the Number Guessing Game!\n")
time.sleep(1)
clear_screen()


def get_name():
    """
    Asks player if they are ready to play and tells player to enter name.
    Name must be letters not numbers.
    """
    player_name = input("Ready to play?  Please enter your name: \n")
    clear_screen()
    if (not player_name.isalpha()):
        print("Sorry, I need a name!")
        get_name()
        return
    print("Hello", player_name)
    time.sleep(2)


def play_game():
    """
    Player selects difficulty level and game runs
    """
    level = input('Choose level - E for easy, M for medium or H for hard: \n')
    time.sleep(0.5)
    clear_screen()

    if level.lower() == "e" or level.lower() == "easy":
        max_number = 10
        tries = 5
    elif level.lower() == "m" or level.lower() == "medium":
        max_number = 100
        tries = 8
    elif level.lower() == "h" or level.lower() == "hard":
        max_number = 500
        tries = 10
    else:
        print("Sorry!  Please select e, m or h!")
        print(" ")
        time.sleep(1)
        play_game()  # stops game from crashing

    number = random.randint(1, max_number)
    print('I am thinking of a number between 1 and ' + str(max_number) + "\n")
    time.sleep(2)
    clear_screen()

    number_of_guesses = 1
    while number_of_guesses <= tries:
        try:
            guess = int(input("Your guess: "))
            clear_screen()
        except ValueError:
            print("Must be a number!  Try again.")
            time.sleep(1)
            play_game()  # stops game from crashing

        if guess < number:
            print("Oops too low!\n")
            time.sleep(1)
            clear_screen()
            number_of_guesses += 1
        if guess > number:
            print("Oops too high!\n")
            time.sleep(1)
            clear_screen()
            number_of_guesses += 1
        elif guess == number:
            print('You got it in ' + str(number_of_guesses) + ' tries!')
            time.sleep(1)
            clear_screen()
            return
    else:
        print('You have run out of guesses! The number was', number)
        clear_screen()


def main():
    get_name()
    again = 'y'
    while again.lower() == "y":
        play_game()
        again = input("Would you like to play again?  (y/n): ")
        clear_screen()
        if again.lower() == "n":
            print("Ok, thanks for playing!  See ya!")
           


if __name__ == "__main__":
    main()
