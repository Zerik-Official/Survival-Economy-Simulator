# Estado.py
# Author: Juan Jose Varela
# Description: Verifies resource limits and determines defeat conditions.

def verify_state (resources:list):

    firewood = resources[0]
    wheat = resources[1]
    population = resources[2]

# I normalize negatives as 0

    if firewood < 0:  
        firewood = 0

    if wheat < 0:
        wheat = 0

    if population < 0:
        population = 0

# I update the list

    resources[0] = firewood
    resources[1] = wheat
    resources[2] = population

#Defeat conditions

    if wheat == 0:
        print("GAME OVER: You are out of wheat")
        return False
    elif population == 0:
        print("GAME OVER: Your population is gone")
        return False
    elif firewood == 0:  
        print("WARNING: No firewood, Population  will decrease due to cold")
        return False