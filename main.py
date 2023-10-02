from random import randint
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def guessing_game(retry, number_range):
    """
    Function to take input and check the number with the random number generated.
    Parameters: 
    
    retry: Number of retries in the guessing game
    number_range: Range of the guessing game
    """
    # Generating a random number to initiate the game
    try:
        random_number = randint(1, number_range)

        while retry > 0:
            retry -= 1
            guess = int(input(f"Guess a number between 1 and {number_range}: "))
            if guess == random_number:
                print("You guessed correctly!")
                return
            elif guess > number_range:
                print("Your guess is out of range.")
                print("You have %d tries left." % retry)
            else:
                print("You guessed incorrectly.")
                print("You have %d tries left." % retry)         
            

        print("Game Over!")
        print(f"Random Number Generated was {random_number}")
    except Exception as er:
        LOGGER.error("ERROR:=====>", er)

        return {"status_code": 500, "message": er}

# define levels
def easy_level():
    """
    Function to define the level of the game.
    """
    print("Guess the number between 1 and 10, you have 6 retries")
    guessing_game(6, 10)

def medium_level():
    """
    Function to define the level of the game.
    """
    print("Guess the number between 1 and 20, you have 4 retries")
    guessing_game(4, 20)

def hard_level():
    """
    Function to define the level of the game.
    """
    print("Guess the number between 1 and 50, you have 3 retries")
    guessing_game(3, 50)

# try again function
def try_again():
    """
    Function to check whether user wants to try again or not
    """
    response = input("Do you want to try again? (YES/NO): ")
    if response.upper() == "YES":
        print("Let's play again!")
        welcome_players()
    elif response.upper() == "NO":
        print("Thanks for playing!")
    else:
        print("Invalid response!")
        try_again()

# Function to welcome the players
def welcome_players():
    """
    Function to welcome the user in the game
    """
    print("Welcome to the Number Guessing Game!")
    game_mode()

def game_mode():
    """
    Function to take game difficulty mode input from the user.
    """
    print("Please select a difficulty level: ")
    response = input("EASY, MEDIUM, HARD: ")

    if response.upper() == "EASY":
        easy_level()
        try_again()
    elif response.upper() == "MEDIUM":
        medium_level()
        try_again()
    elif response.upper() == "HARD":
        hard_level()
        try_again()
    else:
        print("Invalid Response!")
        game_mode()





if __name__ == "__main__":
    welcome_players()