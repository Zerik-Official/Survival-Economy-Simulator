#===============================================
# consumo.py
# Author: Angela Manjarres
# Description: Subtracts daily resources according 
# to population and applies market logic.
# It runs after eventos and before estado.
#================================================


def consume(resources: dict[str, int | float]) -> None:
    """
    Function to consume daily resources based on the population and apply market logic. It updates the resources dictionary in place.

    Args:
        resources (dict[str, int | float]): A dictionary containing the current quantities of each resource.
    Returns:
        None
    """
    # Firewood consumption (1 per person)



    if resources['firewood'] >= resources['population']:
        resources['firewood'] = resources['firewood'] - resources['population']
    else:
        resources['firewood'] = 0

    # Check normal conditions to determine if rationing is required.
    # Based on the current available wheat units.
    # One citizen dies due to rationing.

    # Normal condition (2 per person)
    if resources['wheat'] >= resources['population'] * 2:
        resources['wheat'] = resources['wheat'] - resources['population'] * 2
        print("The whole population was fed")

    # Rationing
    elif resources['wheat'] < 10:
        print("Rationing activated: less than 10 wheat available")

        if resources['wheat'] >= resources['population']:
            resources['wheat'] = resources['wheat'] - resources['population']
        else:
            resources['wheat'] = 0

        # One citizen dies due to rationing (never below 0)
        if resources['population'] > 0:
            resources['population'] = resources['population'] - 1
            print("One citizen died due to rationing")

    # No wheat available
    else:
        resources['wheat'] = 0


def market_logic(resources: dict[str, int | float]) -> None:
    """
    Function to apply market logic based on the current wheat price. It updates the resources dictionary in place.
    Args:
        resources (dict[str, int | float]): A dictionary containing the current quantities of each resource.
    Returns:
        None
    """

    venta = 2
    compra = 5

    # for high price
    if resources['wheat_price'] >= 12:

        if resources['wheat'] >= venta:
            resources['wheat'] = resources['wheat'] - venta
            resources['gold'] = resources['gold'] + venta * resources['wheat_price']
            print("2 units of wheat were sold")
        else:
            print("There is not enough wheat to sell")

    # for low price
    elif resources['wheat_price'] <= 8:

        if resources['gold'] >= compra * resources['wheat_price']:
            resources['wheat'] = resources['wheat'] + compra
            resources['gold'] = resources['gold'] - compra * resources['wheat_price']
            print("Low wheat price, 5 units were bought")
        else:
            print("There is not enough gold")

    # standard price
    else:
        print("Standard price, no buying or selling actions are performed")


    # Protection to avoid negative values

    if resources['firewood'] < 0:
        resources['firewood'] = 0

    if resources['wheat'] < 0:
        resources['wheat'] = 0

    if resources['gold'] < 0:
        resources['gold'] = 0

    if resources['population'] < 0:
        resources['population'] = 0
    