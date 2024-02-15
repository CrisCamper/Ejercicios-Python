# Este archivo nos servirá para suplir necesidades del programador y para que otros modulos funcionen
import os, json

# FUNCIONES GENEREALES

def validar_opcion(min,max): # (Modulos) Funcion para valdiar opciones del menú
    while True:
        try:
            opcion = int(input("Escoja una opcion: "))
            if (opcion >= min) and (opcion <= max):
                return opcion
            else:
                print("El número ingresado está fuera de rango")
        except ValueError:
            print("Por Favor ingrese un dato válido")

def limpiar_pantalla(): # (Sistema) Función para limpiar pantalla, lo usamos para simular una nueva ventana
    os.system('cls' if os.name == 'nt' else 'clear')

def tecla_continuar(): # (Modulos) Función que servirá para presionar una tecla para continuar
    input("[Presiona Cualquier tecla para continuar]")

def buscador_de_valor(clave, valor, archivo_json): # Funcion para buscar valores en específico

    # 
    if archivo_json is None:
        print("Base de datos vacía, es posible que no haya ningún actor agregado aún")
    else:
        try:

            #! POR CADA PERSONA ENCONTRADA QUE CONTENGA LA INFORMACIÓN SOLICITADA; SERÁ AGREGADA A LA LISTA DE PERSONAS ENCONTRADAS

            personas_encontradas = [persona for persona in archivo_json if persona[f"{clave}"] == valor]
            return personas_encontradas
        
        except Exception as e:
            print(f"Error: {e}")

# FUNCIONES ACERCA DE JSON
def guardar_en_json(datos, nombre_json): #Funcion para guardar datos en json
    # Crea el directorio database si no existe
    if not os.path.exists("database"):
        os.makedirs("database")

    # Guardar los datos en json
    with open(f"database/{nombre_json}", "w") as archivo:
        archivo.write(json.dumps(datos, indent=4))
        archivo.write('\n')  # agrega una nueva linea

def cargar_datos_json(nombre_json): #Funcion para extraer los datos de un archivo json en forma de lista
    try:

        # Cargar los datos almacenados en json 
        with open(f"database/{nombre_json}", "r") as archivo:

            datos_existentes = json.load(archivo) #los convertimos en una lista para mejor uso
            return datos_existentes
        
    except Exception as e:
        pass