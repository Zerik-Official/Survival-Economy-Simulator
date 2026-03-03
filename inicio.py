#authors: Deyanis Martelo, Laimen Mejia
#description: The game requests the player's name and sets up global variables based on difficulty

#welcome message
print("============ WELCOME TO THE GAME SURVIVAL TO THE EXTREME ===========")

#player name is requested
name:str = input("Please enter your name: ").strip().lower()

#game variables
game_active:bool = True
victory:bool = False
day:int = 1

#player chooses the difficulty they will play on
print("Choose your difficulty")

print("- Easy")
print("- Normal")
print("- Hard")
#resource configuration based on difficulty
difficulty:str = input("Difficulty:   ").strip().lower()

#easy resources
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
else:
    firewood:int = 20
    wheat:int = 20
    gold:int = 20
    population:int = 10
    wheat_price:float = 10
    print("your chosen difficulty is hard")