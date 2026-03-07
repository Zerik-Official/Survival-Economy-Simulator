# ================================================================

# motor.py
# author: Melissa Garrido
# description: This module contains the Motor class, which represents the days traveled in the game.

# ================================================================

# --- Import files -----------------------------------------------
# We import the necessary files for the game to function, such as the interface, events, consumption, and state.

# Libraries
import random

# Internal modules
from estado import verify_state
from eventos import apply_event
from interfaz import show_resources_list
from consumo import consume, market_logic
from inicio import entry_difficulty, choose_difficulty, name

# --- Day cycle -----------------------------------------------
# We start the day cycle, iterating through the information of each day.

day_of_weeks: list[str] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def init_engine() -> tuple[str, dict[str, int | float], str]:
    """
    init_engine initializes the game engine by prompting the player to choose a difficulty level and setting up the initial resources based on that choice.
    It returns the chosen difficulty and the initial resources for the game.
    Args:
        None
    Returns:
        difficulty (str): The chosen difficulty level as a string ("1", "2", or "3").
        resources (dict[str, int | float]): A dictionary containing the initial resources for the game.
    """
    difficulty = entry_difficulty()

    resources = choose_difficulty(difficulty)



    return difficulty, resources

# Main game loop. Iterates through each day (1 to 10) while the game remains active.
# On each day, it waits for player input, updates the day, and reloads all game modules.

def day_cycle():

    # Game state variables
    current_day: int = 1
    game_active: bool = True

    random_entry_day: int = random.randint(0, len(day_of_weeks) - 1)
    

    difficulty, resources = init_engine()
    

    while current_day <= 10 and game_active:
        
        current_day_text: str = day_of_weeks[random_entry_day % len(day_of_weeks)]


        # Show resources
        show_resources_list(name, current_day, current_day_text, resources)


        print("\n--- EVENT ---")
        apply_event(difficulty, resources)

        print("\n--- CONSUMPTION ---")
        consume(resources, current_day_text)

        print("\n--- MARKET ---")
        market_logic(resources)

        print("\n--- STATE CHECK ---")
        game_active = verify_state(resources)

        if not game_active:
            break

        input("\nPress ENTER to pass the day...")
        
        current_day += 1
        random_entry_day += 1

    if game_active:
        print("\nYou survived 10 days! You win!")
    else:
        print("\nYour village did not survive.")


# --- Execute function in main -----------------------------------------------
# Entry point: only runs if this file is executed directly, not when imported.
if __name__ == "__main__":
    day_cycle()