#Programa para calcular promedio de 4 notas
#Entrada: notas
#Salida: promedio

def promedio(sumaNotas, cantidad):#función para calcular el promedio
    media = 0
    media = float(sumaNotas / cantidad)
    return media

def sumaNotas(listaNotas):
    suma = 0
    for i in listaNotas:
        suma = suma + i

    return suma


note1 = float(input('nota 1: '))
note2 = float(input('nota 2: '))
note3 = float(input('nota 3: '))
note4 = float(input('nota 4: '))

list = [note1,note2,note3,note4]
suma = sumaNotas(list)
print('El promedio es: ', promedio(suma, 4))