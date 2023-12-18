# Solicitamos el número
while True:
    try:
        n = int(input('Input the number: '))  # Pedimos el número original
        break
    except ValueError:
        print('Error: Input a valid date')  # Volver al ciclo en caso de error

# Convertimos el número a una lista de dígitos
digitos_lista = [int(digito) for digito in str(n)[::-1]]  # Invertimos la cadena antes de convertirla en lista

j = 2  # Declarando variable para el ciclo for
suma = 0  # Declarando variable para el ciclo for

# Multiplicamos el número por la secuencia de 2, 3, 4, 5, 6, 7
for i in digitos_lista:
    result = i * j
    suma = suma + result
    j = j + 1
    if j > 7:
        j = 2  # Reiniciamos j a 2 después de llegar a 7

# Tomamos el módulo 11 del resultado obtenido
modulo_resultado = suma % 11

# Restamos 11 al modulo_resultado
x = (11 - modulo_resultado)

# Restamos el módulo 11 al número original
verificador = (n - x)

print(f'The verification digit is: {verificador}')
