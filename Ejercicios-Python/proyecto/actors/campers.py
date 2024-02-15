# Este archivo tendrá todas las funciones que utilizaremos para registrar campers, etc.

from tools.utilidades import validar_opcion, guardar_en_json, cargar_datos_json, tecla_continuar, limpiar_pantalla, buscador_de_valor

def registrar_camper(): #Funcion para registrar un camper
    while True:
        try:

            #! Cargamos los datos existentes de los campers (si los hay, recordemos que todo lo sobrescribiremos)
            #! En caso de que no haya nada en json (Retorna None), se creará una lista en donde podamos guardar los datos

            datos_campers = cargar_datos_json("campers.json") or []

            #! Aqui escribiremos los datos del camper

            while True:
                identificacion = int(input("Ingrese el número de identificación: "))
                usuario_existente = buscador_de_valor("identificacion", identificacion, datos_campers)
                if not usuario_existente:
                    break
                else:
                    print("Usuario existente, intente de nuevo con otra ID")

            nombre = input("Ingrese el nombre del camper: ")
            apellido = input("Ingrese el apellido del camper: ")
            direccion = input("Ingrese la dirección del camper: ")
            acudiente = input("Acudiente del camper: ")
            celular = int(input("Ingrese el número de telefono del camper: "))
            numero_fijo = int(input("Ingrese el número fijo del camper: "))

            #? Para los estados primero decidi dar una lista de estados disponibles            
            print("Estados disponibles: ")
            print("1. Inscrito ")
            print("2. Aprobado ")

            # Luego validamos la opcion del usuario    
            estado = validar_opcion(1,2)

            if estado == 1: #? Si la opcion es 1, entonces el estado será "Inscrito"
                estado = "inscrito"
            elif estado == 2: #? Si la opcion es 2, entonces el estado será "Aprobado"
                estado = "aprobado"

            ruta = "none"

            #! Guardamos los anteriores datos en el siguiente diccionario

            nuevo_camper = {
                "identificacion": identificacion,
                "nombre": nombre,
                "apellidos": apellido,
                "direccion": direccion,
                "acudiente": acudiente,
                "celular": celular,
                "fijo": numero_fijo,
                "estado": estado,
                "ruta": ruta
            }

            #! Guardammos la informacion del nuevo camper al final del diccionario de "datos_campers". Cuando todo este combinado (la informacion existente con la nueva), lo guardaremos en campers.json

            datos_campers.append(nuevo_camper)
            guardar_en_json(datos_campers, "campers.json")

            print("El nuevo camper Fue agregado con éxito.")
            tecla_continuar()
            limpiar_pantalla()
            return None

        except ValueError:
            print("Por favor ingrese un dato válido.")
            tecla_continuar()
            limpiar_pantalla()

def listar_campers(): # Funcion para listar los campers
    limpiar_pantalla()
    #! Cargamos los datos de los campers, si no los hay, retornaremos "none" para salir de la función.
    lista_de_campers = cargar_datos_json("campers.json")
    if lista_de_campers is None:
        print("No hay campers almacenados aún.")
        tecla_continuar()
        limpiar_pantalla()
        return None

    #! Imprimimos la lsita de campers
    print('LISTA DE CAMPERS')
    for camper in lista_de_campers:
        for datos in camper:
            print(datos,':',camper[datos])
        print('---------------------------')
    tecla_continuar()
    limpiar_pantalla()

def pruebas_camper(): # Funcion para evaluar el rendimiento del camper
    while True:
        try:
            #! CARGAMOS LOS DATOS DE LOS CAMPERS QUE SE ENCUENTRAN EN CAMPERS.JSON

            datos_campers = cargar_datos_json("campers.json")
            if datos_campers is None: #! SI NO HAY NINGÚN CAMPERS EN EL JSON, IMPRIMIRÁ EL MENSAJE A CONTINUACIÓN Y SALDRÁ DE LA FUNCION
                print("ERROR: La base de datos que ud solicita está vacía.")
                tecla_continuar()
                limpiar_pantalla()
                break

            #! LE PEDIMOS AL USUAIO QUE INGRESE EL ID DEL USUAIO QUE DESEA EVALUA

            id_camper = int(input("Ingrese el id del camper que desea evaluar: "))
            camper_encontrado = buscador_de_valor("identificación",id_camper)
        except ValueError:
            print("Asegurese de ingresar datos validos")