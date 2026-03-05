import random
import inicio

def calculate_event(difficulty: str) -> int:
    if difficulty == "easy":
        R = 10
    elif difficulty == "normal":
        R = 24
    else:
        R = 40
    
    width = R / 8

    return [width * i for i in range(1, 9)]

print(calculate_event("easy"))

def apply_event(difficulty: str):
    r2 = random.randint(1, 100)
    
    limits = calculate_event(difficulty)

    if r2 <= limits[0]:
        print("A snowstorm is approaching!")
        loss = 10 if difficulty == "easy" else 12 if difficulty == "normal" else 15
        print(f"You lose {loss} firewood!")
        inicio.firewood -= loss

    elif r2 <= limits[1]:
        print("A plague is spreading and destroying the wheat!")
        loss = 12 if difficulty == "easy" else 15 if difficulty == "normal" else 20
        print(f"You lose {loss} wheat!")
        inicio.wheat -= loss

    elif r2 <= limits[2]:
        print("Bandits are attacking the village!")
        gold_loss = 10 if difficulty == "easy" else 12 if difficulty == "normal" else 23
        wheat_rise = 2 if difficulty == "easy" else 4 if difficulty == "normal" else 6
        print(f"You lose {gold_loss} gold and wheat price rises!")
        inicio.gold -= gold_loss
        inicio.wheat_price += wheat_rise

    elif r2 <= limits[3]:
        print("The village river has completely frozen over!")
        loss = 12 if difficulty == "easy" else 15 if difficulty == "normal" else 19
        print(f"You lose {loss} wheat!")
        inicio.wheat -= loss

    elif r2 <= limits[4]:
        print("A brutal blizzard has destroyed several huts in the village!")
        loss = 15 if difficulty == "easy" else 15 if difficulty == "normal" else 20
        print(f"You lose {loss} firewood!")
        inicio.firewood -= loss

    elif r2 <= limits[5]:
        print("A winter fever epidemic is spreading through the village!")
        loss = 10 if difficulty == "easy" else 12 if difficulty == "normal" else 15
        wheat_rise = 2 if difficulty == "easy" else 4 if difficulty == "normal" else 6
        print(f"You lose {loss} wheat and wheat price rises!")
        inicio.wheat -= loss
        inicio.wheat_price += wheat_rise

    elif r2 <= limits[6]:
        print("Acid rain!")
        loss = 10 if difficulty == "easy" else 12 if difficulty == "normal" else 15
        print(f"You lose {loss} water!")
        inicio.water -= loss

    else:
        print("Nothing happened today!")