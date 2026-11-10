cadena = input(f'Introduce la cadena principal: ')
subcadena = input(f'Introduce la subcadena: ')

if cadena.startswith(subcadena):
    print(f'La cadena empieza por la subcadena')
else:
    print(f'La cadena no empieza por la subcadena')
