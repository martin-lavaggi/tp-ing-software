import random
import time

print('\n')
time.sleep(0.5)
print('------------------------------------------')
time.sleep(0.5)
print('----- JUEGO DE PIEDRA, PAPEL, TIJERA -----')
time.sleep(0.5)
print('------------------------------------------')
time.sleep(0.5)
print('\n')

# MODALIDAD DE LA PARTIDA (JUEGO O SIMULACIÓN)
modo = input('Para simular una partida, introduzca [S]. Para jugar contra el ordenador, introduzca [J] -> ').lower()
print('\n')
# control de datos incorrectos
if modo not in ['s', 'j']:
    print('ERROR: Los datos introducidos no son correctos.')
    quit()

# CONTADOR SI O NO. MUESTRA INICIAL
contador = input('¿Desea usar un contador de puntos? Responda [Si] o [No] -> ').lower()
if contador == 'si':
    # Variables para implementar el contador
    contador_1 = 0
    contador_2 = 0
    print('\n')
    print('-------------------------')
    print('| Jugador 1 | Jugador 2 |')
    print('| ', contador_1, 'ptos   | ', contador_2, 'ptos   |')
    print('-------------------------')
elif contador != 'no':
    print('\n')
    print('ERROR: Los datos introducidos no son correctos.')
    quit()
# control de datos incorrectos
else:
    print('ERROR: Los datos introducidos no son correctos.')
    quit()

print('\n')
time.sleep(2)

# BUCLE PARA REPETIR EL JUEGO O SIMULACIÓN SI ASÍ SE QUIERE
repetir = 'r'
while repetir == 'r':

    # MODO JUEGO (FUNCIONA)
    if modo == 'j':

        print('--------- JUEGO CONTRA ORDENADOR ---------')
        print('\n')
        time.sleep(1)

        # Petición de elección al usuario
        usuario = input('Escoja su elección para la partida: [Piedra], [Papel] o [Tijera] - > ').lower()
        if usuario == 'piedra':  # piedra es 1
            usuario = 1
        elif usuario == 'papel':  # papel es 2
            usuario = 2
        elif usuario == 'tijera':  # tijera es 3
            usuario = 3
        else:  # control de datos incorrectos
            print('ERROR: Los datos introducidos no son correctos.')
            quit()

        print('\n')
        # print('------ USUARIO ES: ', usuario, ' -------')                                                       # TEST

        # asignación aleatoria del resultado del ordenador
        ordenador = random.randrange(1, 4)

        # Usuario gana con piedra
        if usuario == 1 and ordenador == 3:
            print('Usuario ha escogido piedra y el Ordenador ha escogido tijera.')
            time.sleep(1)
            print('Ha ganado el Usuario')
            time.sleep(1)
            ganador = 'user'
        # Usuario gana con tijera
        elif usuario == 3 and ordenador == 2:
            print('Usuario ha escogido tijera y Ordenador ha escogido papel.')
            time.sleep(1)
            print('Ha ganado Usuario')
            time.sleep(1)
            ganador = 'user'
        # Usuario gana con papel
        elif usuario == 2 and ordenador == 1:
            print('Usuario ha escogido papel y Ordenador ha escogido piedra.')
            time.sleep(1)
            print('Ha ganado Usuario')
            time.sleep(1)
            ganador = 'user'
        # Jugador 2 gana con piedra
        elif ordenador == 2 and usuario == 3:
            print('Usuario ha escogido tijera y Ordenador ha escogido piedra.')
            time.sleep(1)
            print('Ha ganado Ordenador')
            time.sleep(1)
            ganador = 'ord'
        # Jugador 2 gana con tijera
        elif ordenador == 3 and usuario == 2:
            print('Usuario ha escogido papel y Ordenador ha escogido tijera.')
            time.sleep(1)
            print('Ha ganado Ordenador')
            time.sleep(1)
            ganador = 'ord'
        # Jugador 2 gana con papel
        elif ordenador == 2 and usuario == 1:
            print('Usuario ha escogido piedra y Ordenador ha escogido papel.')
            time.sleep(1)
            print('Ha ganado Ordenador')
            time.sleep(1)
            ganador = 'ord'
        # HAY EMPATE
        else:
            print('Usuario y Ordenador han empatado.')
            time.sleep(1)
            ganador = 'empate'
        print('\n')

        # contador
        if contador == 'si':
            # asignación de puntos para el contador
            if ganador == 'user':
                contador_1 = contador_1 + 1
            elif ganador == 'ord':
                contador_2 = contador_2 + 1
            elif ganador == 'empate':
                contador_1 = contador_1 + 1
                contador_2 = contador_2 + 1

            # muestra contador
            if (len(str(contador_1)) == 1) and (len(str(contador_2)) == 1):
                print('-------------------------')
                print('|  Usuario  | Ordenador |')
                print('| ', contador_1, 'ptos   | ', contador_2, 'ptos   |')
                print('-------------------------')
                print('\n')
            elif (len(str(contador_1)) == 1) and (len(str(contador_2)) == 2):
                print('-------------------------')
                print('|  Usuario  | Ordenador |')
                print('| ', contador_1, 'ptos   | ', contador_2, 'ptos  |')
                print('-------------------------')
                print('\n')
            elif (len(str(contador_1)) == 2) and (len(str(contador_2)) == 1):
                print('-------------------------')
                print('|  Usuario  | Ordenador |')
                print('| ', contador_1, 'ptos  | ', contador_2, 'ptos   |')
                print('-------------------------')
                print('\n')
            elif (len(str(contador_1)) == 2) and (len(str(contador_2)) == 2):
                print('-------------------------')
                print('|  Usuario  | Ordenador |')
                print('| ', contador_1, 'ptos  | ', contador_2, 'ptos  |')
                print('-------------------------')
                print('\n')

        # Repetir juego
        repetir = input(
            '¿Desea repetir el juego/simulación? Si es así, introduzca [R]; si no, [ENTER] -> ').lower()
        print('\n')

    # MODO SIMULAR (FUNCIONA)
    elif modo == 's':

        print('--------- SIMULACIÓN DE PARTIDA ----------')
        print('\n')
        time.sleep(1)

        # asignación de valores para cada opción del juego
        piedra = 1
        papel = 2
        tijera = 3

        # se toman resultados aleatorios para cada jugador
        jugador_1 = random.randrange(1, 4)
        jugador_2 = random.randrange(1, 4)

        # Jugador 1 gana con piedra
        if jugador_1 == piedra and jugador_2 == tijera:
            print('Jugador 1 ha escogido piedra y el Jugador 2 ha escogido tijera.')
            time.sleep(1)
            print('Ha ganado el Jugador 1')
            time.sleep(1)
            ganador = 'jug1'
        # Jugador 2 gana con tijera
        elif jugador_1 == tijera and jugador_2 == papel:
            print('Jugador 1 ha escogido tijera y Jugador 2 ha escogido papel.')
            time.sleep(1)
            print('Ha ganado Jugador 1')
            time.sleep(1)
            ganador = 'jug1'
        # Jugador 1 gana con papel
        elif jugador_1 == papel and jugador_2 == piedra:
            print('Jugador 1 ha escogido papel y Jugador 2 ha escogido piedra.')
            time.sleep(1)
            print('Ha ganado Jugador 1')
            time.sleep(1)
            ganador = 'jug1'
        # Jugador 2 gana con piedra
        elif jugador_2 == piedra and jugador_1 == tijera:
            print('Jugador 1 ha escogido tijera y Jugador 2 ha escogido piedra.')
            time.sleep(1)
            print('Ha ganado Jugador 2')
            time.sleep(1)
            ganador = 'jug2'
        # Jugador 2 gana con tijera
        elif jugador_2 == tijera and jugador_1 == papel:
            print('Jugador 1 ha escogido papel y Jugador 2 ha escogido tijera.')
            time.sleep(1)
            print('Ha ganado Jugador 2')
            time.sleep(1)
            ganador = 'jug2'
        # Jugador 2 gana con papel
        elif jugador_2 == papel and jugador_1 == piedra:
            print('Jugador 1 ha escogido piedra y Jugador 2 ha escogido papel.')
            time.sleep(1)
            print('Ha ganado Jugador 2')
            time.sleep(1)
            ganador = 'jug2'
        # Hay empate
        else:
            print('Ambos jugadores han escogido lo mismo.')
            time.sleep(1)
            print('Jugador 1 y Jugador 2 han empatado.')
            time.sleep(1)
            ganador = 'empate'
        print('\n')

        # contador
        if contador == 'si':
            # asignación de puntos para el contador
            if ganador == 'jug1':
                contador_1 = contador_1 + 1
            elif ganador == 'jug2':
                contador_2 = contador_2 + 1
            elif ganador == 'empate':
                contador_1 = contador_1 + 1
                contador_2 = contador_2 + 1

            # muestra contador
            if (len(str(contador_1)) == 1) and (len(str(contador_2)) == 1):
                print('-------------------------')
                print('| Jugador 1 | Jugador 2 |')
                print('| ', contador_1, 'ptos   | ', contador_2, 'ptos   |')
                print('-------------------------')
                print('\n')
            elif (len(str(contador_1)) == 1) and (len(str(contador_2)) == 2):
                print('-------------------------')
                print('| Jugador 1 | Jugador 2 |')
                print('| ', contador_1, 'ptos   | ', contador_2, 'ptos  |')
                print('-------------------------')
                print('\n')
            elif (len(str(contador_1)) == 2) and (len(str(contador_2)) == 1):
                print('-------------------------')
                print('| Jugador 1 | Jugador 2 |')
                print('| ', contador_1, 'ptos  | ', contador_2, 'ptos   |')
                print('-------------------------')
                print('\n')
            elif (len(str(contador_1)) == 2) and (len(str(contador_2)) == 2):
                print('-------------------------')
                print('| Jugador 1 | Jugador 2 |')
                print('| ', contador_1, 'ptos  | ', contador_2, 'ptos  |')
                print('-------------------------')
                print('\n')

        # Repetir juego
        repetir = input('¿Desea repetir el juego/simulación? Si es así, introduzca [R]; si no, [ENTER] -> ').lower()
        print('\n')
