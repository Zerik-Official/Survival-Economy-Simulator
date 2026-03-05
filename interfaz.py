#==========================================================================
#interfaz.py
#authors: ELIANIS CERVANTES 
#descripcion: Interfaz juego "WELCOME TO THE GAWE SERVIVAL TO EXTREMA"  

#===========================================================================

import inicio

from colorama import init, Fore, Style
#INICIO DE COLORAMA

print(Fore.BLUE + "WELCOME TO THE GAME SERVIVAL TO EXTREMA" + Style.RESET_ALL)

#TABLA DE RECURSO 

print(Fore.RED + "firewood" + Style.RESET_ALL)
print(Fore.RED + "wheat" + Style.RESET_ALL)
print(Fore.RED + "gold" + Style.RESET_ALL)


print(Fore.GREEN + "firewood" + Style.RESET_ALL)
print(Fore.GREEN + "wheat" + Style.RESET_ALL)
print(Fore.GREEN + "gold" + Style.RESET_ALL)

#FUNCIONES PARA DEFINIR COLOR 

def color_recurso(valor: int) -> str:
    if valor < 20:
        return Fore.RED + str(valor)

    elif valor > 60:
        return Fore.YELLOW + str(valor)

    else: 
        return Fore.GREEN + str(valor)

# funciones para mostrar recursos 
def lista_recursos(resources:list[int, float]):

    print("firewoo", resources[0])
    print("wheat", resources[1])
    print("gold", resources[2])