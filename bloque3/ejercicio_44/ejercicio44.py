frase = input("Introduce una frase: ")
palabras = 0
palabra = False

for caracter in frase:
    if caracter != " " and not palabra:
        palabras += 1
        palabra = True
    elif caracter == " ":
        palabra = False
print(palabras)
