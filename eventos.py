# Eventos.py
# Author: Saul Uribe Hernandez
# Description: This module defines the random events that can occur in the game based on the chosen difficulty level. Each event has a certain probability of occurring and can affect the player's resources in different ways.

import random
import inicio

# This function calculates the probability limits for each event based on difficulty
# The harder the difficulty, the more likely a bad event will occur
def calculate_event(difficulty: str) -> int:
    # I assign the maximum range based on the chosen difficulty
    if difficulty == "easy":
        R = 10
    elif difficulty == "normal":
        R = 24
    else:
        R = 40
    
    # I divide the range into 8 equal parts, one for each possible event
    width = R / 8

    # I return a list with the 8 cumulative limits
    return [width * i for i in range(1, 9)]

# This function applies a random event to the game depending on the difficulty
# It's called every turn to see what happens to the village
def apply_event(difficulty: str):
    # I generate a random number from 1 to 100
    r2 = random.randint(1, 100)
    
    # I get the limits to determine which event triggers
    limits = calculate_event(difficulty)

    # I compare r2 against each limit to determine the event
    # If it falls within the first range, snowstorm
    if r2 <= limits[0]:
        print("A snowstorm is approaching!")
        loss = 10 if difficulty == "easy" else 12 if difficulty == "normal" else 15
        print(f"You lose {loss} firewood!")
        inicio.firewood -= loss

    # Plague that destroys wheat
    elif r2 <= limits[1]:
        print("A plague is spreading and destroying the wheat!")
        loss = 12 if difficulty == "easy" else 15 if difficulty == "normal" else 20
        print(f"You lose {loss} wheat!")
        inicio.wheat -= loss

    # Bandit attack: you lose gold and wheat price goes up
    elif r2 <= limits[2]:
        print("Bandits are attacking the village!")
        gold_loss = 10 if difficulty == "easy" else 12 if difficulty == "normal" else 23
        wheat_rise = 2 if difficulty == "easy" else 4 if difficulty == "normal" else 6
        print(f"You lose {gold_loss} gold and wheat price rises!")
        inicio.gold -= gold_loss
        inicio.wheat_price += wheat_rise

    # The river freezes, wheat is lost
    elif r2 <= limits[3]:
        print("The village river has completely frozen over!")
        loss = 12 if difficulty == "easy" else 15 if difficulty == "normal" else 19
        print(f"You lose {loss} wheat!")
        inicio.wheat -= loss

    # Blizzard destroys huts, firewood is lost
    elif r2 <= limits[4]:
        print("A brutal blizzard has destroyed several huts in the village!")
        loss = 15 if difficulty == "easy" else 15 if difficulty == "normal" else 20
        print(f"You lose {loss} firewood!")
        inicio.firewood -= loss

    # Epidemic: you lose wheat and its price goes up
    elif r2 <= limits[5]:
        print("A winter fever epidemic is spreading through the village!")
        loss = 10 if difficulty == "easy" else 12 if difficulty == "normal" else 15
        wheat_rise = 2 if difficulty == "easy" else 4 if difficulty == "normal" else 6
        print(f"You lose {loss} wheat and wheat price rises!")
        inicio.wheat -= loss
        inicio.wheat_price += wheat_rise

    # Acid rain, water is lost
    elif r2 <= limits[6]:
        print("Acid rain!")
        loss = 10 if difficulty == "easy" else 12 if difficulty == "normal" else 15
        print(f"You lose {loss} water!")
        inicio.water -= loss

    # If r2 falls outside all ranges, nothing happens this turn
    else:
        print("Nothing happened today!")