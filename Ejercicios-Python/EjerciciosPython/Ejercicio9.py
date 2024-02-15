# Programa para calcular la palabra más larga
# Entrada: Dos palabras
# Salida: palabra más larga

# Funcion para calcular la palabra mayor
def palabraMayor(word1, word2):
    if len(word1) > len(word2):
        resultado = f'{word1} es mayor que {word2} por {len(word1) - len(word2)} letras'
    elif len(word2) > len(word1):
        resultado = f'{word2} es mayor que {word1} por {len(word2) - len(word1)} letras'
    else:
        resultado = 'Ambas palabras tienen la misma longitud'
    return resultado

# Entrada de la palabra
word1 = input('Ingresa la palabra 1: ')
word2 = input('Ingresa la palabra 2: ')

# Calcular y mostrar el resultado
print(palabraMayor(word1, word2))

