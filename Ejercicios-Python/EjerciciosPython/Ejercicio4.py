#Programa de conversion de unidades de longitud
#entrada: cms
#Salida: pulgadas

#pedir al usuario que ingrese la longitud
unidad = float(input('Ingrese longitud: '))

#conversión
pulgada = (unidad * 1)/2.54

#mostrar en pantalla el resultado
print(f'{unidad} cm = {pulgada} in')