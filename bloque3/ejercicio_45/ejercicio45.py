nombre = input(f'Introduce tu nombre:')
iniciales = ""
coger = True

for i in range(len(nombre)):
    if nombre[i] != " " and coger:
        iniciales = iniciales + nombre[i]
        coger = False
    elif nombre[i] == " ":
        coger = True
print(iniciales)
