# ================================================================
# inicio.py
# Authors: Deyanis Martelo, Laimen Mejia
# Description: The game requests the player's name and sets up
#              global variables based on the difficulty level.
# Runs after: N/A (entry point of the game)
# ================================================================

# ======================== WELCOME MESSAGE ========================
print("============ WELCOME TO THE GAME SURVIVAL TO THE EXTREME ===========")


name:str = input("Please enter your name: ").strip().lower()

#game variables
game_active:bool = True
victory:bool = False
current_day:int = 1
show_table:bool = False
difficulty = None

#player chooses the difficulty they will play on

print("Choose your difficulty")

print("- Easy")
print("- Normal")
print("- Hard")

def entry_difficulty(): 
    try:
        not_error:bool = False

        valids_difficultys:list[str] = ["easy", "normal", "hard"]

        while (not not_error):
            #resource configuration based on difficulty

            difficulty = input("Difficulty:   ").strip().lower()


            if difficulty not in valids_difficultys:
                print("chamo, pon una dificultad real")
                continue
            
            return difficulty
    except ValueError: 
        print("Please choose a valid difficulty")

#easy resources
def choose_difficulty(difficulty): 
    if difficulty == "easy":
        firewood:int = 100
        wheat:int = 100
        gold:int = 100
        population:int = 10
        wheat_price:float = 10
        print("your chosen difficulty is easy")

    #intermediate resources
    elif difficulty == "normal":
        firewood:int = 50
        wheat:int = 50
        gold:int = 50
        population:int = 10
        wheat_price:float = 10
        print("your chosen difficulty is normal")

    #hard resources
    elif difficulty == "hard":
        firewood:int = 20
        wheat:int = 20
        gold:int = 20
        population:int = 10
        wheat_price:float = 10
        print("your chosen difficulty is hard")
    else:
        print("Please choose a valid difficulty (easy, normal, hard)")
        return None

    return firewood, wheat, gold, population, wheat_price