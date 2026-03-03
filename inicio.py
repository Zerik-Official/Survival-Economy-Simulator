
#autores:Deyanis Martelo , Laimen Mejia 
#descripcion: variables globales, dificultad y nombre del jugador
print("============ BIENVENIDO AL JUEGO SUPERVIVENCIA AL EXTREMO===========")
nombre:str = input("Por favor introduce tu nombre: ").strip().lower() 
print("Elija la dificultad")

print("- Facil")
print("- Normal")
print("- Dificil")

dificultad:str = input("Dificultad:   ").strip().lower()


if dificultad == "facil" : 
    leña:int = 100
    trigo:int = 100
    oro:int = 100
    poblacion:int = 10
    precio_trigo:float = 10
    juego_activo:bool = True
    victoria:bool = False
    print("tu dificultad eligida es facil")

elif dificultad == "normal" :
    leña:int = 50
    trigo:int = 50
    oro:int = 50
    poblacion:int = 10
    precio_trigo:float = 10
    juego_activo:bool = True
    victoria:bool = False
    print("tu dificultad eligida es normal")

else:
    leña:int = 20
    trigo:int = 20
    oro:int = 20
    poblacion:int = 10
    precio_trigo:float = 10
    juego_activo:bool = True
    victoria:bool = False

    print("tu dificultad eligida es dificil")
