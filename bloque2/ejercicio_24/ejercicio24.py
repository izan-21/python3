cantidad = int(input(f'¿Cuántos números deseas introducir?'))

mayores = 0
menores = 0
iguales = 0

i = 0
while i < cantidad:
    numero = float(input(f'Introduce el número {i + 1}: '))
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1
        
    i += 1
print(f'Números mayores que 0: {mayores}')
print(f'Números menores que 0: {menores}')
print(f'Números iguales a 0: {iguales}')
