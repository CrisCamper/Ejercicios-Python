# Programa que pida numero de columnas y filas para mostrar una matriz
number_files = int(input('Ingrese un becerro numero de filas: ')) # (rows = filas) dato de numero de filas
number_columnes = int(input('Ingrese el berraco numero de columnas 🦴: ')) # Dato de número de columnas

print(' _'* number_columnes) # Imprimimos los '_' al inicio

for file in range (number_files): # Por cada fila, agregamos la correspondiente columna
    print('|_'*number_columnes+'|')
    