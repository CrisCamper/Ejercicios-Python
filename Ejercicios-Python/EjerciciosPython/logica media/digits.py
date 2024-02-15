# Program for read numbers:
def calcularDigitos (a): #function for calculating numbers
    a = str(a)
    resultado = f'Cantidad de digitos de {a}: {len(a)}'

    return resultado


while True: # cicle for prevenir if the user send a invalid syntax
    try:
        n = int(input('Ingrese el número entero: '))
        break
    except ValueError:
        print('Error: Por favor ingrese un valor valido.')

print(calcularDigitos(n)) # Print the digit's number of a number