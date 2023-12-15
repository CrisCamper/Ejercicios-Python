# Programa para mostrar la hora futura
# Entrada: hora actual (t), número entero de horas (h)
# Salida: Hora dentro de h horas

def contadorHoras(t,h): # Contamos las horas desde t hasta h
    nueva_hora = (t+h)%12
    print(nueva_hora) # retornamos la variable nueva_hora

#entrada de datos
t = int(input('Ingrese la hora actual: '))
h = int(input('Cantidad de horas: '))


contadorHoras(3,5)