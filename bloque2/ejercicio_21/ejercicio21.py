print(f'Calcular un factorial')

num = int(input(f'Introduzca un número: '))
fac = 1
numero = 1
while numero <= num:
     fac = fac * numero
     numero += 1

print(f'El número factorial es {fac}')

