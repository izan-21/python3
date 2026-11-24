cadena = input(f'Introduce una cadena:')
subcadena = input(f'Introduce una subcadena:')

if cadena[:len(subcadena)] == subcadena:
    print(f'La subcadena empeiza por la cadena')
else:
    print(f'La subcadena no comienza por la cadena')
