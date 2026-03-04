# ================================================================
# inicio.py
# Authors: Deyanis Martelo, Laimen Mejia
# Description: The game requests the player's name and sets up
#              global variables based on the difficulty level.
# Runs after: N/A (entry point of the game)
# ================================================================

# ======================== WELCOME MESSAGE ========================
print("============ WELCOME TO THE GAME SURVIVAL TO THE EXTREME ===========")


# Player name
name:str = input("Please enter your name: ").strip().lower()

# Game State Variables
game_active:bool = True
victory:bool = False
current_day:int = 1
show_table:bool = False

# player chooses the difficulty they will play on

print("Choose your difficulty")

print("- Easy")
print("- Normal")
print("- Hard")

def entry_difficulty() -> str: 

    difficulty:str = None

    difficulty_map:list[str] = ["easy", "normal", "hard"]

    while difficulty not in difficulty_map:
        print("Please choose: easy, normal, or hard")
        difficulty:str = input("Choose Difficulty: ").strip().lower()
    
    return difficulty


#easy resources
def choose_difficulty(difficulty:str) -> list[int]: 
    if difficulty == "easy":
        firewood:int = 100
        wheat:int = 100
        gold:int = 100
        population:int = 10
        wheat_price:int = 10
        print("your chosen difficulty is easy")

    #intermediate resources
    elif difficulty == "normal":
        firewood:int = 50
        wheat:int = 50
        gold:int = 50
        population:int = 10
        wheat_price:int = 10
        print("your chosen difficulty is normal")

    #hard resources
    elif difficulty == "hard":
        firewood:int = 20
        wheat:int = 20
        gold:int = 20
        population:int = 10
        wheat_price:int = 10
        print("your chosen difficulty is hard")

    return firewood, wheat, gold, population, wheat_price