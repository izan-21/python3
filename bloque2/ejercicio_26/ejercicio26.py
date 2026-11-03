inicio = int(input(f'Introduce el número inicial: '))
fin = int(input(f'Introduce el número final: '))

if inicio > fin:
  inicio, fin = fin, inicio
print(f'\nNúmeros pares entre {inicio} y {fin}:')
actual = inicio
while actual <= fin:
  if (actual // 2) * 2 == actual:
    print(actual)
  actual += 1
