#===============================================
#consumo.py
#Autor:Angela Manjarres
#descripcion: Resta recursos según poblacion dia a dia.
# control de recursos.
#se ejecuta luego de eventos y antes de estado.
#=================================================

import inicio


# verificacion de cantidad de leña.
if inicio.firewood >= inicio.population:
    inicio.firewood = inicio.firewood - inicio.population * 1 
else:
    inicio.firewood >= 0

#verificar condiciones normales para identificar si es necesario entrar o no a razonamiento.
#por unidades actuales existentes de trigo.
#condicional muere uno por razonamiento.
 
if inicio.wheat >= inicio.population:
    inicio.wheat >= inicio.wheat - inicio.population * 2 
    print("Toda la poblacion se alimento")

    

if inicio.wheat < 10:
    print("se activo, razonamiento hay menos de 10 en trigo")
    inicio.wheat = inicio.wheat - inicio.population * 1

else:
    inicio.wheat = 0

if inicio.wheat > 0:
    inicio.wheat = inicio.wheat - inicio.population - 1
    