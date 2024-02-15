import math

def desviacion_estandar(valores):
    # Calcular el promedio de los valores
    suma = sum(valores)
    promedio = suma / len(valores)

    # Restarle el promedio a cada valor y elevar al cuadrado
    resultado_cuadrado = sum((x - promedio) ** 2 for x in valores)

    # Dividir la suma por la cantidad de valores
    varianza = resultado_cuadrado / len(valores)

    # Sacar la raíz cuadrada del resultado para obtener la desviación estándar
    desviacion_estandar = math.sqrt(varianza)

    return desviacion_estandar

valores = [1.3, 1.3 , 1.3]
print('La desviacion estandar es:',desviacion_estandar(valores))
