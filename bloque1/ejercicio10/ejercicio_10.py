print(f'Nota final de la materia algoritmos')
p1 = float(input("Nota parcial 1: "))
p2 = float(input("Nota parcial 2: "))
p3 = float(input("Nota parcial 3: "))
examen = float(input("Nota examen final: "))
trabajo = float(input("Nota trabajo final: "))


promedio_parciales = (p1 + p2 + p3) / 3
calificacion_final = (promedio_parciales * 0.55) + (examen * 0.30) + (trabajo * 0.15)

print(f"Calificación final: {calificacion_final:.2f}")
