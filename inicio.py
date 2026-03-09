# ================================================================
# inicio.py
# Authors: Deyanis Martelo, Laimen Mejia
# Description: The game requests the player's name and sets up
#              global variables based on the difficulty level.
# ================================================================
import random
from colorama import Fore, Style, init 
init(autoreset=True)


# ======================== WELCOME MESSAGE ========================
print("============ WELCOME TO THE GAME SURVIVAL TO THE EXTREME ===========")


def get_player_name() -> str:
    """
    Prompt the user to enter a valid name.

    Validation rules:
    - Must not be empty or only spaces
    - Minimum length: 4 characters
    - Maximum length: 13 characters
    - Must contain only letters

    Returns:
        name (str): A validated name in lowercase.
    """

    valid:bool = False
    name = ""

    while not valid:
        name: str = input("Please enter your name: ").strip().lower()

        if not name:
            print("Name cannot be empty.")
        elif len(name) < 4:
            print("Name must be at least 4 characters.")
        elif len(name) > 13:
            print("Name must be at most 13 characters.")
        elif not name.isalpha():
            print("Name must contain only letters.")
        else:
            valid = True

    return name

def entry_difficulty() -> str:
    """ 
    Function to prompt the player to choose a difficulty level and validate the input. 
    
    Args: 
        None 
    Returns: 
        difficulty (str): The chosen difficulty level as a string ("1", "2", or "3").

    """
    difficulty = None
    difficulty_map:list[str] = ["1", "2", "3"]

    while difficulty not in difficulty_map:
        print("Choose your difficulty:")
        print(f"1){Fore.GREEN} Easy")
        print(f"2){Fore.YELLOW} Normal")
        print(f"3){Fore.RED} Hard")

        difficulty:str = input("Choose difficulty (1-3): ").strip()

        if difficulty not in difficulty_map:
            print("Please enter a valid option.")

    return difficulty

def choose_difficulty(difficulty:str) -> dict[str, int | float]:
    """
    Function to set up the game resources based on the chosen difficulty level.

    Args:
        difficulty (str): The chosen difficulty level as a string ("1", "2", or "3").
    Returns:
        resources (dict[str, int | float]): A dictionary containing the initial resources for the game.
    """

    
    # Randomly generate the population between 1 and 6
    population:int = random.randint(1, 6)

    # Easy respurces
    if difficulty == "1":
        resources = {
            "firewood": 100,
            "wheat": 100,
            "gold": 100,
            "population": population,
            "wheat_price": 10
        }

    # Normal resources
    elif difficulty == "2":
        resources = {
            "firewood": 50,
            "wheat": 50,
            "gold": 50,
            "population": population,
            "wheat_price": 10
        }

    # Hard resources
    elif difficulty == "3":
        resources = {
            "firewood": 20,
            "wheat": 20,
            "gold": 20,
            "population": population,
            "wheat_price": 10
        }

    return resources