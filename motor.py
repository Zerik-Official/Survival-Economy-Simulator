# ================================================================

# motor.py
# author: Melissa Garrido
# description: This module contains the Motor class, which represents the days traveled in the game.

# ================================================================

# --- Import files -----------------------------------------------
# We import the necessary files for the game to function, such as the interface, events, consumption, and state.

import random
from inicio import entry_difficulty, choose_difficulty, name
from interfaz import color_off_resource, show_resources_list
from consumo import consume, market_logic
from estado import verify_state
from eventos import apply_event


# --- Day cycle -----------------------------------------------
# We start the day cycle, iterating through the information of each day.

day_of_weeks: list[str] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
current_day: int = 1
game_active: bool = True



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

    randon_entry_day: int = random.randint(1, len(day_of_weeks) - 1)
    current_day_text: str = day_of_weeks[randon_entry_day]

    return difficulty, resources, current_day_text

# Main game loop. Iterates through each day (1 to 10) while the game remains active.
# On each day, it waits for player input, updates the day, and reloads all game modules.

def day_cycle():

    global current_day
    global game_active

    difficulty, resources, current_day_text = init_engine()

    while current_day <= 10 and game_active:

        print("\n===================================")
        print(f"DAY {current_day} - {current_day_text}")
        print("===================================\n")

        # Show resources
        show_resources_list(name, current_day, current_day_text, resources)


        print("\n--- EVENT ---")
        apply_event(difficulty, resources)

        print("\n--- CONSUMPTION ---")
        consume(resources)

        print("\n--- MARKET ---")
        market_logic(resources)

        print("\n--- STATE CHECK ---")
        game_active = verify_state(resources)

        if not game_active:
            break

        input("\nPress ENTER to pass the day...")

        current_day += 1

    if game_active:
        print("\nYou survived 10 days! You win!")
    else:
        print("\nYour village did not survive.")


# --- Execute function in main -----------------------------------------------
# Entry point: only runs if this file is executed directly, not when imported.
if __name__ == "__main__":
    day_cycle()