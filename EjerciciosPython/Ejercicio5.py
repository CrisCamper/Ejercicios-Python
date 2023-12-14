# Aplicar pitagoras
# Entrada: catetoA y catetoB
# Salida: Hipotenusa c

import math # Importamos la libreria math

def calculoCateto(a , b): # funcion calcular la hipotenusa
    c = 0
    c = math.sqrt(a**2 + b**2)
    return c

# Entrada de datos
a = 0 # Inicializar variable
b = 0 # Inicializar variable
a = int(input('ingrese cateto a: '))# leemos cateto a
b = int(input('ingrese cateto b: '))# leemos cateto b

# Salida por pantalla
print('El valor de la hipotenusa es: ', calculoCateto(a,b))