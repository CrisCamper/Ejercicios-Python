def inicializar_palabra(palabra):
    return ["_" if letra.isalpha() else letra for letra in palabra]

def imprimir_palabra(palabra_actual):
    print('"' + ' '.join(palabra_actual) + '"')

def jugar_ahorcado(palabra_a_adivinar, intentos_maximos):
    palabra_actual = inicializar_palabra(palabra_a_adivinar)
    intentos_realizados = 0
    partes_del_cuerpo = ["pierna derecha", "pierna izquierda", "brazo derecho", "brazo izquierdo", "tronco", "cabeza"]

    print("Comienza el juego!")
    imprimir_palabra(palabra_actual)

    while "_" in palabra_actual and intentos_realizados < intentos_maximos:
        letra = input("Ingrese letra: ").lower()

        if letra.isalpha() and len(letra) == 1:
            if letra in palabra_a_adivinar:
                for i in range(len(palabra_a_adivinar)):
                    if palabra_a_adivinar[i] == letra:
                        palabra_actual[i] = letra
            else:
                print(f"Pierde \"{partes_del_cuerpo[intentos_realizados]}\"")
                intentos_realizados += 1
        else:
            print("Ingrese una letra válida.")

        imprimir_palabra(palabra_actual)

    if "_" not in palabra_actual:
        print("¡Haz ganado!")
    else:
        print("¡Haz perdido el juego!")

# Ejemplo de uso
palabra_a_adivinar = input("Ingrese la palabra: ").lower()
intentos_maximos = 6  # Número máximo de intentos antes de perder

jugar_ahorcado(palabra_a_adivinar, intentos_maximos)
