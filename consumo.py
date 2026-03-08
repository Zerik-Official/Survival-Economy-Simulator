#===============================================
# consumo.py
# Author: Angela Manjarres
# Description: Subtracts daily resources according 
# to population and applies market logic.
# It runs after eventos and before estado.
#================================================
import random
from colorama import Fore, Style


def daily_modifier(current_day_text: str, base_amount: float, resource: str, random_resource: str) -> float:
    """
    Function to apply a daily modifier to the resource consumption based on the current day of the week and a randomly selected resource.

    Args:
        current_day_text (str): The current day of the week as a string (e.g., "Monday", "Tuesday", etc.).
        base_amount (float): The base amount of the resource to be consumed before applying the modifier
        resource (str): The type of resource being consumed ("firewood" or "wheat").
        random_resource (str): The randomly selected resource that will be affected by the daily modifier ("firewood" or "wheat").
    Returns:
        modified_amount (float): The modified amount of the resource to be consumed after applying the daily modifier.
    """


    if resource == random_resource:

        if current_day_text == "Monday" or current_day_text == "Tuesday":
            return base_amount * 0.8

        elif current_day_text == "Wednesday" or current_day_text == "Thursday" or current_day_text == "Friday":
            return base_amount

        elif current_day_text == "Saturday" or current_day_text == "Sunday":
            return base_amount * 1.2

    return base_amount

def consume(resources: dict[str, int | float], current_day_text:str) -> None:
    """
    Function to consume daily resources based on the population and apply market logic. It updates the resources dictionary in place.

    Args:
        resources (dict[str, int | float]): A dictionary containing the current quantities of each resource.
    Returns:
        None
    """
    # Firewood consumption (1 per person)

    # Randomly select a resource to be affected by the daily modifier (20% more or less consumption).
    random_resource = random.choice(["firewood", "wheat"])

    firewood_consume = resources['population']
    firewood_consume = daily_modifier(current_day_text, firewood_consume, "firewood", random_resource)

    if resources['firewood'] >= firewood_consume:
        resources['firewood'] = resources['firewood'] - firewood_consume
    else:
        resources['firewood'] = 0

    # Check normal conditions to determine if rationing is required.
    # Based on the current available wheat units.
    # One citizen dies due to rationing.

    wheat_consume = resources['population'] * 2
    wheat_consume = daily_modifier(current_day_text, wheat_consume, "wheat", random_resource)

    # Normal condition (2 per person)
    if resources['wheat'] >= wheat_consume:
        resources['wheat'] = resources['wheat'] - wheat_consume
        print(f"{Fore.GREEN}[FEEDING]{Style.RESET_ALL} The whole population was fed")
    # Not enough wheat
    else:
        print(f"{Fore.RED}[FEEDING]{Style.RESET_ALL} Not enough wheat to feed the population")
        resources['wheat'] = 0

def market_logic(resources: dict[str, int | float]) -> None:
    """
    Function to apply market logic based on the current wheat price. It updates the resources dictionary in place.
    
    Args:
        resources (dict[str, int | float]): A dictionary containing the current quantities of each resource.
    Returns:
        None
    """

    quantity_sold = 2

    purchase_quantity = 2

    # for high price
    if resources['wheat_price'] >= 12:

        if resources['wheat'] >= quantity_sold:
            resources['wheat'] = resources['wheat'] - quantity_sold
            resources['gold'] = resources['gold'] + quantity_sold * resources['wheat_price']
            print(f"{Fore.YELLOW}[MARKET]{Style.RESET_ALL} 2 units of wheat were sold")
        else:
            print(f"{Fore.RED}[MARKET]{Style.RESET_ALL} There is not enough wheat to sell")

    # for low price
    elif resources['wheat_price'] <= 10:

        if resources['gold'] >= purchase_quantity * resources['wheat_price']:
            resources['wheat'] = resources['wheat'] + purchase_quantity
            resources['gold'] = resources['gold'] - purchase_quantity * resources['wheat_price']
            print(f"{Fore.GREEN}[MARKET]{Style.RESET_ALL} Low wheat price, 5 units were bought")
        else:
            print(f"{Fore.RED}[MARKET]{Style.RESET_ALL} There is not enough gold")

    # standard price
    else:
        print(f"{Fore.CYAN}[MARKET]{Style.RESET_ALL} Standard price, no buying or selling actions are performed")


    # Protection to avoid negative values

    if resources['firewood'] < 0:
        resources['firewood'] = 0

    if resources['wheat'] < 0:
        resources['wheat'] = 0

    if resources['gold'] < 0:
        resources['gold'] = 0

    if resources['population'] < 0:
        resources['population'] = 0
    