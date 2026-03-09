#==========================================================================
#interfaz.py
#authors: ELIANIS CERVANTES 
#descripcion: Interfaz juego "WELCOME TO THE GAWE SERVIVAL TO EXTREMA"  

#===========================================================================
from colorama import init, Fore, Style

# Separator for formatting the output
separator: str = "=" * 50

def color_off_resource(quantity: int) -> str:
    """
    Determine the color for a resource based on its quantity.

    Args:
        cuantity (int): The quantity of the resource.

    Returns:
        str: The color code for the resource.
    """
    if quantity < 60:
        return Fore.RED

    elif quantity > 60 and quantity < 80:
        return Fore.YELLOW

    else: 
        return Fore.GREEN


def show_resources_list(player_name:str, current_day:int, current_day_text:str, resources:dict[str, int | float]) -> None:
    """
    Display the current resources and day information in a formatted manner.

    Args:
        player_name (str): The name of the player.
        current_day (int): The current day number.
        current_day_text (str): The text representation of the current day.
        resources (dict[str, int | float]): A dictionary containing the quantities of each resource.
    Returns:
        None
    """
    print(separator)
    print(f"| Days: {current_day} | Day_week: {current_day_text} | Player: {player_name.capitalize()}")
    print(separator)
    print(f"  ⚔️  Medieval village resources  ⚔️")
    print()
    print(f"  🌲 Firewood: {color_off_resource(resources['firewood'])}{resources['firewood']}{Style.RESET_ALL}")
    print(f"  🌾 Wheat: {color_off_resource(resources['wheat'])}{resources['wheat']}{Style.RESET_ALL}")
    print(f"  💰 Gold: {color_off_resource(resources['gold'])}{resources['gold']}{Style.RESET_ALL}")
    print(f"  👥 Population: {resources['population']}")
    print(separator)