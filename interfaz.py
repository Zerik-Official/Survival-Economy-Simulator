#==========================================================================
#interfaz.py
#authors: ELIANIS CERVANTES 
#descripcion: Interfaz juego "WELCOME TO THE GAWE SERVIVAL TO EXTREMA"  

#===========================================================================
from colorama import init, Fore, Style

def color_off_resource(cuantity: int) -> str:
    """
    Determine the color for a resource based on its quantity.

    Args:
        cuantity (int): The quantity of the resource.

    Returns:
        str: The color code for the resource.
    """
    if cuantity < 20:
        return Fore.RED

    elif cuantity > 60 and cuantity < 80:
        return Fore.YELLOW

    else: 
        return Fore.GREEN


def show_resources_list(player_name:str, current_day:int, current_day_text:str, resources:dict[str, int | float]) -> None:
    """
    Display the current resources and day information in a formatted manner.

    Args:
        current_day (int): The current day number.
        current_day_text (str): The text representation of the current day.
        resources (dict[str, int | float]): A dictionary containing the quantities of each resource.
    Returns:
        None
    """

    print("firewood", resources["firewood"])
    print("wheat", resources["wheat"])
    print("gold", resources["gold"])
    print("poblacion", resources["population"])