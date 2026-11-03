caracter = input(f'Introduce un carácter (introduce un espacio para terminar):')

while caracter != " ":
  if caracter in "aeiouAEIOU":
    print("Vocal")
  else:
    print("No vocal")
  caracter = input("Introduce un carácter (introduce un espacio para terminar): ")

print("Programa finalizado.")

