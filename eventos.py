# Eventos.py
# Author: Saul Uribe Hernandez
# Description: This module defines the random events that can occur in the game based on the chosen difficulty level. Each event has a certain probability of occurring and can affect the player's resources in different ways.

import random
import colorama
from colorama import Fore, Style

# This function calculates the probability limits for each event based on difficulty
# The harder the difficulty, the more likely a bad event will occur
def calculate_event(difficulty: str) -> int:
    """"
    Function to calculate the probability limits for each random event based on the chosen difficulty level.
    Args:
        difficulty (str): The chosen difficulty level as a string ("1", "2", or "3").
    Returns:
        list[float]: A list of cumulative probability limits for each event.
    """

    # I assign the maximum range based on the chosen difficulty
    if difficulty == "1":
        R = 10
    elif difficulty == "2":
        R = 24
    else:
        R = 40
    
    # I divide the range into 8 equal parts, one for each possible event
    width = R / 8

    # I return a list with the 8 cumulative limits
    return [width * i for i in range(1, 9)]

# This function applies a random event to the game depending on the difficulty
# It's called every turn to see what happens to the village
def apply_event(difficulty: str, resources: dict[str, int | float]) -> None:
    """
    function to apply a random event to the game based on the chosen difficulty level and current resources.
    Args:
        difficulty (str): The chosen difficulty level as a string ("1", "2", or "3").
        resources (dict[str, int | float]): A dictionary containing the quantities of each resource.
    Returns:
        None
    """
    # I generate a random number from 1 to 100
    r2 = random.randint(1, 100)
    
    # I get the limits to determine which event triggers
    limits = calculate_event(difficulty)

    # I compare r2 against each limit to determine the event
    # If it falls within the first range, snowstorm
    if r2 <= limits[0]:
        print("A snowstorm is approaching!")
        loss = 10 if difficulty == "1" else 12 if difficulty == "2" else 15
        print(f"{Fore.RED}You lose {loss} firewood!{Style.RESET_ALL}")
        resources['firewood'] -= loss
    # Plague that destroys wheat
    elif r2 <= limits[1]:
        print("A plague is spreading and destroying the wheat!")
        loss = 12 if difficulty == "1" else 15 if difficulty == "2" else 20
        print(f"{Fore.RED}You lose {loss} wheat!{Style.RESET_ALL}")
        resources['wheat'] -= loss
    # Bandit attack: you lose gold and wheat price goes up
    elif r2 <= limits[2]:
        print("Bandits are attacking the village!")
        gold_loss = 10 if difficulty == "1" else 12 if difficulty == "2" else 23
        wheat_rise = 2 if difficulty == "1" else 4 if difficulty == "2" else 6
        print(f"{Fore.RED}You lose {gold_loss} gold and wheat price rises!{Style.RESET_ALL}")
        resources['gold'] -= gold_loss
        resources['wheat_price'] += wheat_rise
    # The river freezes, wheat is lost
    elif r2 <= limits[3]:
        print("The village river has completely frozen over!")
        loss = 12 if difficulty == "1" else 15 if difficulty == "2" else 19
        print(f"{Fore.RED}You lose {loss} wheat!{Style.RESET_ALL}")
        resources['wheat'] -= loss
    # Blizzard destroys huts, firewood is lost
    elif r2 <= limits[4]:
        print("A brutal blizzard has destroyed several huts in the village!")
        loss = 15 if difficulty == "1" else 15 if difficulty == "2" else 20
        print(f"{Fore.RED}You lose {loss} firewood!{Style.RESET_ALL}")
        resources['firewood'] -= loss
    # Epidemic: you lose wheat and its price goes up
    elif r2 <= limits[5]:
        print("A winter fever epidemic is spreading through the village!")
        loss = 10 if difficulty == "1" else 12 if difficulty == "2" else 15
        wheat_rise = 2 if difficulty == "1" else 4 if difficulty == "2" else 6
        print(f"{Fore.RED}You lose {loss} wheat and wheat price rises!{Style.RESET_ALL}")
        resources['wheat'] -= loss
        resources['wheat_price'] += wheat_rise
    # Freezing cold wave hits, you burn extra firewood to survive
    elif r2 <= limits[6]:
        print("A freezing cold wave hits the village!")
        loss = 5 if difficulty == "1" else 8 if difficulty == "2" else 12
        print(f"{Fore.RED}You burn extra firewood to survive (-{loss}).{Style.RESET_ALL}")
        resources["firewood"] -= loss
    # Food storage freezes, wheat is lost
    elif r2 <= limits[7]:
        print("Your food storage froze overnight!")
        loss = 8 if difficulty == "1" else 12 if difficulty == "2" else 16
        print(f"{Fore.RED}You lose {loss} wheat.{Style.RESET_ALL}")
        resources["wheat"] -= loss
    # If r2 falls outside all ranges, nothing happens this turn
    else:
        print(f"{Fore.GREEN}Nothing happened today!{Style.RESET_ALL}")