# Programa para calcular la parte decimal de un número ingresado
# Entrada: número 
# Salida: parte decimal

def parteDecimal (num): # Calcula parte decimal
    parte_entera = int(num)
    decimal = num - parte_entera
    return decimal

num = float(input('ingrese un número: '))

while num != 0: # Repetir hasta que el resultado sea 0.0
    print(parteDecimal(num))
    num = float(input('ingrese un número: '))
