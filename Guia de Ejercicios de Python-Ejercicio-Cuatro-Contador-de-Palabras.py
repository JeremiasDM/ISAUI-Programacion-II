def contar_palabras(frase: str) -> int:
    palabras = frase.split()
    return len(palabras)

Frase = input("Ingrese una frase: ")
NumeroDePalabras = contar_palabras(Frase)
print("La Frase: ", Frase, "Contiene", NumeroDePalabras, "Palabras")

