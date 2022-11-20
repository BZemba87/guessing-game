
import random
import time
import os
import termcolor


def clear_screen():
    """
    clears screen after some messages to keep it tidy
    """
    os.system('cls' if os.name == 'nt' else 'clear')


termcolor.cprint("Welcome to the Number Guessing Game!", "green")
time.sleep(2)
termcolor.cprint("You have 5, 8 or 10 chances to guess", "green")
time.sleep(1)
termcolor.cprint("the correct number.", 'green')
time.sleep(2)
termcolor.cprint("Good luck!", "green")
time.sleep(4)
clear_screen()


def get_name():
    """
    Asks player if they are ready to play and tells player to enter name.
    Name must be letters not numbers or blank space.
    """
    player_name = input("Ready to play?  Please enter your name: \n")
    clear_screen()
    if not player_name.isalpha():
        termcolor.cprint("Sorry, I need a name!", "red")
        get_name()
        return
    print("Hello", player_name)
    time.sleep(2)


def generate_number(max_number):
    number = random.randint(1, max_number)
    print('I am thinking of a number between 1 and ' + str(max_number) + "\n")
    time.sleep(2)
    return number


def gets_guess_number():
    """
    Gives player option to quit or try again
    """
    guess = None
    dont_quit = True
    input_question = "What's the number?"
    while dont_quit:
        try:
            guess = input(input_question)
            if guess == "q" or guess == "quit":
                dont_quit = False
            else:
                guess = int(guess)
                dont_quit = False
        except ValueError:
            termcolor.cprint("Must be a number!  Try again.", "red")
            time.sleep(1)
            clear_screen()
            input_question = """You can type q to quit.
                \nTry again?  What's the number?"""
    return guess


def play_game():
    """
    Player selects difficulty level and game runs
    """
    tries = 0
    max_number = 0
    level = input('Choose level - E for easy, M for medium or H for hard: \n')
    time.sleep(0.5)
    clear_screen()
    generated_number = 0
    if level.lower() == "e" or level.lower() == "easy":
        max_number = 10
        tries = 5
        generated_number = generate_number(max_number)
    elif level.lower() == "m" or level.lower() == "medium":
        max_number = 100
        tries = 8
        generated_number = generate_number(max_number)
    elif level.lower() == "h" or level.lower() == "hard":
        max_number = 500
        tries = 10
        generated_number = generate_number(max_number)
    else:
        termcolor.cprint("Sorry!  Please select e, m or h!", "red")
        print(" ")
        time.sleep(1)
        play_game()  # stops game from crashing

    number_of_guesses = 1
    while number_of_guesses <= tries:
        guess = gets_guess_number()
        if guess == "q" or guess == "quit":
            termcolor.cprint("Thanks for playing!  Bye!", "green")
            break

        if guess < generated_number:
            termcolor.cprint("Oops, too low!", "red")
            time.sleep(1)
            clear_screen()
            number_of_guesses += 1
        if guess > generated_number:
            termcolor.cprint("Oops too high!", "red")
            time.sleep(1)
            clear_screen()
            number_of_guesses += 1
        elif guess == generated_number:
            print('You got it in ' + str(number_of_guesses) + ' tries!')
            time.sleep(1)
            break       # stops both messages appearing at end of play
    else:
        print('You have run out of guesses! The number was', generated_number)
        time.sleep(2)


def main():
    get_name()
    again = 'y'
    while True:
        play_game()
        again = input("Would you like to play again?  (y/n): ")
        clear_screen()
        while again.lower() not in ("y", "n"):
            again = input("Would you like to play again?  (y/n): ")
        if again == "n":
            termcolor.cprint("Thanks for playing!  Bye!", "green")
            break


if __name__ == "__main__":
    main()
