import random
print(f'¡Binvenido al juego de adivinar el número!')
print(f'Tienes 10 intentos para divinar el número que he pensado')

numero_secreto = random.randint(1, 100)
intentos_totales = 10

for intento_actual in range(1, intentos_totales + 1):
    intentos_restantes = intentos_totales - intento_actual + 1
    print(f'Intentos restantes, {intentos_restantes}')

    intento = int(input(f'Introduce un número: '))

    if intento == numero_secreto:
        print(f'¡Felicidades, lo has conseguido!') 
        break

    elif intento > numero_secreto:
        print(f'Tu número es Mayor')

    else: 
        print(f'Tu número es Menor')

if intentos_totales == 0:
    print(f'Se acabó el juego, has alcanzado el número máximo de intentos /n El número era {numero_secreto}'>
