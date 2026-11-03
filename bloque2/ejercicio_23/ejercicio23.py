suma = 0
contador = 0

numero = float(input("Introduce un número (0 para acabar): "))

while numero != 0:
  suma += numero
  contador += 1
  numero = float(input("Introduce un número (0 para acabar): "))

if contador > 0:
  media = suma / contador
  print(f'\nSuma total: {suma}')
  print(f'Media de los números: {media}')
else:
  print('\nNo se ha introducido ningún número.')
