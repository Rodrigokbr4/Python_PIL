import random


def jugar():
    usario = input('Elige una opcion: "pi" para piedra, "pa" para papel y "ti" para tijera. \n').lower()
    
    computadora = random.choice(["pi", "pa", "ti"])
    
    if usario == computadora:
        print('Eleccion de la computadora: ', computadora)
        return '¡Empate!'
    
    if gano_el_jugador(usario, computadora):
        print('Eleccion de la computadora: ', computadora)
        return '¡Ganaste!'
    
    print('Eleccion de la computadora: ', computadora)
    return '¡Perdiste!'
    
    
def gano_el_jugador(jugador, oponente):
    #Retornar True si gana el jugador.
    #Piedra gana a Tijera (pi > ti).
    #Tijera gana a Papel (ti > pa).
    #Papel gana a Piedra (pa > pi).
    if (( jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())
    
    
    
    