cadena = input(f'Introduce una cadena:')
caracter = input(f'Introduce un caracter:')
if  len(caracter) !=1 :
    print(f'Debe de ser un solo caracter')
else:
    print(cadena.count(caracter))
