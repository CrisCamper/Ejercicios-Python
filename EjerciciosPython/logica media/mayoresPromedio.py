# Preguntar al usuario cuántos datos ingresará
num_datos = int(input("Ingrese la cantidad de datos: "))

# Inicializar una lista para almacenar los datos
datos = []

# Pedir al usuario que ingrese los datos uno por uno
for i in range(num_datos):
    dato = float(input("Ingrese el dato {}: ".format(i + 1)))
    datos.append(dato)

# Calcular el promedio de los datos
promedio = sum(datos) / num_datos

# Contar cuántos datos son mayores que el promedio
mayores_que_promedio = sum(1 for dato in datos if dato > promedio)

# Mostrar el resultado
print("\nEl promedio de los datos ingresados es: {:.2f}".format(promedio))
print("Cantidad de datos mayores que el promedio: {}".format(mayores_que_promedio))