import random
import inicio


def generar_evento() -> int:
    return random.randint(1, 6)


def aplicar_evento(numero: int, difficulty: str):
    if difficulty == "easy":
        aplicar_evento_easy(numero)
    elif difficulty == "normal":
        aplicar_evento_normal(numero)
    else:
        aplicar_evento_hard(numero)


def aplicar_evento_easy(numero: int):
    if numero == 1:
        print("¡Se acerca una tormenta de nieve!")
        print("¡Pierdes 10 de leña!")
        inicio.firewood -= 10
    elif numero == 2:
        print("¡Se expande una plaga que acaba con el trigo!")
        print("¡Pierdes 12 de trigo!")
        inicio.wheat -= 12
    elif numero == 3:
        print("¡Bandidos atacan el pueblo!")
        print("¡Pierdes 10 de oro y sube el precio del trigo!")
        inicio.gold -= 10
        inicio.wheat_price += 2
    elif numero == 4:
        print("¡El río del pueblo se congela por completo!")
        print("¡Pierdes 12 de trigo!")
        inicio.wheat -= 12
    elif numero == 5:
        print("¡Una ventisca brutal destruye varias chozas del pueblo!")
        print("¡Pierdes 15 de leña!")
        inicio.firewood -= 15
    elif numero == 6:
        print("¡Una epidemia de fiebre invernal se expande por la aldea!")
        print("¡Pierdes 10 de trigo y sube el precio del trigo!")
        inicio.wheat -= 10
        inicio.wheat_price += 2

def aplicar_evento_normal(numero: int):
    if numero == 1:
        print("¡Una tormenta de nieve intensa azota el pueblo!")
        print("¡Pierdes 12 de leña!")
        inicio.firewood -= 12
    elif numero == 2:
        print("¡Una plaga devastadora arrasa con los cultivos de trigo!")
        print("¡Pierdes 15 de trigo!")
        inicio.wheat -= 15
    elif numero == 3:
        print("¡Bandidos saquean el pueblo!")
        print("¡Pierdes 12 de oro y sube el precio del trigo!")
        inicio.gold -= 12
        inicio.wheat_price += 4
    elif numero == 4:
        print("¡El río del pueblo se congela completamente durante semanas!")
        print("¡Pierdes 15 de trigo!")
        inicio.wheat -= 15
    elif numero == 5:
        print("¡Una ventisca brutal destruye la mayoría de las chozas!")
        print("¡Pierdes 15 de leña!")
        inicio.firewood -= 15
    elif numero == 6:
        print("¡Una epidemia de fiebre invernal se propaga por la aldea!")
        print("¡Pierdes 12 de trigo y sube el precio del trigo!")
        inicio.wheat -= 12
        inicio.wheat_price += 4

def aplicar_evento_hard(numero: int):
    if numero == 1:
        print("¡Una tormenta de nieve catastrófica azota el pueblo!")
        print("¡Pierdes 8 de leña!")
        inicio.firewood -= 8
    elif numero == 2:
        print("¡Una plaga mortal arrasa con los cultivos de trigo!")
        print("¡Pierdes 9 de trigo!")
        inicio.wheat -= 9
    elif numero == 3:
        print("¡Bandidos despiadados saquean el pueblo!")
        print("¡Pierdes 8 de oro y sube el precio del trigo!")
        inicio.gold -= 8
        inicio.wheat_price += 6
    elif numero == 4:
        print("¡El río del pueblo se congela completamente durante meses!")
        print("¡Pierdes 9 de trigo!")
        inicio.wheat -= 9
    elif numero == 5:
        print("¡Una ventisca brutal destruye todas las chozas del pueblo!")
        print("¡Pierdes 10 de leña!")
        inicio.firewood -= 10
    elif numero == 6:
        print("¡Una epidemia mortal de fiebre invernal se propaga por la aldea!")
        print("¡Pierdes 8 de trigo y sube el precio del trigo!")
        inicio.wheat -= 8
        inicio.wheat_price += 6