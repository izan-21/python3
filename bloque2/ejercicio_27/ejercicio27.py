numero = int(input(f'Introduce un número para mostra su tabla de multiplicar: '))
print(f'Tabla de multiplicar del {numero}')
for tabla in range(1,11):
   print(f'{numero} x {tabla} = {numero*tabla}')
