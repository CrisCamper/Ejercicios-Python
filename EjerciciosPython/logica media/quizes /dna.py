# Información inicial del programa (nombres y cromosomas)
nombres = ["Pedro", "Juan", "Diego"]
cromosomas = ["00000101010101010101", "00101010101101110111", "00100010010000001001"]

# Obtener la muestra del usuario
muestra_usuario = input("Ingrese la muestra de la escena del crimen (20 caracteres 0/1): ")

# Inicializar variables para la búsqueda
mejor_coincidencia = 0
nombre_sospechoso = ""

# Búsqueda del cromosoma más parecido
for i in range(len(nombres)):
    cromosoma_actual = cromosomas[i]
    coincidencias = 0
    
    # Comparar caracteres uno por uno
    for j in range(20):
        if muestra_usuario[j] == cromosoma_actual[j]:
            coincidencias += 1
    
    if coincidencias > mejor_coincidencia:
        mejor_coincidencia = coincidencias
        nombre_sospechoso = nombres[i]

# Calcular porcentaje de parentesco
porcentaje_parentesco = (mejor_coincidencia / 20) * 100

# Mostrar resultados
print(f"\nEl sospechoso es {nombre_sospechoso} con un {porcentaje_parentesco:.2f}% de parentesco.")

