# Estado.py
# Author: Juan Jose Varela
# Description: Verifies resource limits and determines defeat conditions.
from colorama import init
import colorama

init()

def verify_state(resources:dict[str, int | float]) -> bool:
    """
    Function to verify the current state of the game by checking resource limits and determining defeat conditions.
    
    Args:
        resources (dict[str, int | float]): A dictionary containing the current quantities of each resource.
    Returns:
        bool: True if the game continues, False if a defeat condition is met.
    """

    firewood = resources['firewood']
    wheat = resources['wheat']
    population = resources['population']

    # I normalize negatives as 0

    if firewood < 0:  
        firewood = 0

    if wheat < 0:
        wheat = 0

    if population < 0:
        population = 0

    # I update the list

    resources['firewood'] = firewood
    resources['wheat'] = wheat
    resources['population'] = population

    #Defeat conditions

    if wheat == 0:
        print(colorama.Fore.RED + "GAME OVER: You are out of wheat")
        return False
    elif population == 0:
        print(colorama.Fore.RED + "GAME OVER: Your population is gone")
        return False
    elif firewood == 0:  
        print(colorama.Fore.RED + "GAME OVER: You ran out of firewood")
        return False

    return True