# Ejercicio cuadrado
print('cuadrado/rectángulo')
h = int(input('Ingrese altura: '))
a = int(input('Ingrese ancho: '))

for i in range(h): # hacer cuadrado
    print('*'*a)

# Ejercicio triangulo
print('triángulo')
h = int(input('Ingrese altura: '))
for i in range (h+1): # Hacer triangulo
    temp = 0+i
    print('*'*temp)

# Ejercicio Hexagono
print('Hexagono')
lado = int(input('Ingrese lado: '))

# Hacer el hexagono
for i in range(lado): # Hacer parte superior
    espacios = '-'*(lado-i-1)
    i = i + i
    print(espacios+'*'*(lado+i))

for j in range(lado-1): # Hacer parte inferior
    espacios = '-'*(j+1)
    i = i - 2
    print(espacios+'*'*(lado+i))
    