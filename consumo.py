#===============================================
# consumo.py
# Author: Angela Manjarres
# Description: Subtracts daily resources according 
# to population and applies market logic.
# It runs after eventos and before estado.
#================================================

import inicio

def consumo():
    # Firewood consumption (1 per person)
    if inicio.firewood >= inicio.population:
        inicio.firewood = inicio.firewood - inicio.population
    else:
        inicio.firewood = 0

    # Check normal conditions to determine if rationing is required.
    # Based on the current available wheat units.
    # One citizen dies due to rationing.

    # Normal condition (2 per person)
    if inicio.wheat >= inicio.population * 2:
        inicio.wheat = inicio.wheat - inicio.population * 2
        print("The whole population was fed")

    # Rationing
    elif inicio.wheat < 10:
        print("Rationing activated: less than 10 wheat available")

        if inicio.wheat >= inicio.population:
            inicio.wheat = inicio.wheat - inicio.population
        else:
            inicio.wheat = 0

        # One citizen dies due to rationing (never below 0)
        if inicio.population > 0:
            inicio.population = inicio.population - 1
            print("One citizen died due to rationing")

    # No wheat available
    else:
        inicio.wheat = 0


# Market logic
def market_logic():
    print("==== Market ====")

    venta = 2
    compra = 5

    # for high price
    if inicio.wheat_price >= 12:

        if inicio.wheat >= venta:
            inicio.wheat = inicio.wheat - venta
            inicio.gold = inicio.gold + venta * inicio.wheat_price
            print("2 units of wheat were sold")
        else:
            print("There is not enough wheat to sell")

    # for low price
    elif inicio.wheat_price <= 8:

        if inicio.gold >= compra * inicio.wheat_price:
            inicio.wheat = inicio.wheat + compra
            inicio.gold = inicio.gold - compra * inicio.wheat_price
            print("Low wheat price, 5 units were bought")
        else:
            print("There is not enough gold")

    # standard price
    else:
        print("Standard price, no buying or selling actions are performed")


    # Protection to avoid negative values

    if inicio.firewood < 0:
        inicio.firewood = 0

    if inicio.wheat < 0:
        inicio.wheat = 0

    if inicio.gold < 0:
        inicio.gold = 0

    if inicio.population < 0:
        inicio.population = 0
    