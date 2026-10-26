print(f'Cálculo de sueldo mas ventas')

Sueldo = float(input(f'Introduce tu sueldo base = '))
venta1= float(input(f'Introduce la primera venta = '))
venta2= float(input(f'Introduce la segunda venta = '))
venta3= float(input(f'Introduce la tercera venta = '))

Ventas = venta1 + venta2 + venta3
Comision = Ventas * 0.10
SueldoTotal = Sueldo + Comision

print(f'Tu sueldo incluyendo comisiones seria de {SueldoTotal}€ ')

