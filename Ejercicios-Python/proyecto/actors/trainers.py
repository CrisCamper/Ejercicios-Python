# Este archivo tendrá todas las funciones que utilizaremos para registrar trainers, etc.

from tools.utilidades import validar_opcion, guardar_en_json, cargar_datos_json, tecla_continuar, limpiar_pantalla

def registrar_trainer(): #Funcion para registrar un trainer
    while True:
        try:

            #! Cargamos los datos existentes de los trainers (si los hay, recordemos que todo lo sobrescribiremos)
            #! En caso de que no haya nada en json (Retorna None), se creará una lista en donde podamos guardar los datos

            datos_trainers = cargar_datos_json("trainers.json") or []

            #! Aqui escribiremos los datos del trainer


            identificacion = int(input("Ingrese el número de identificación: "))
            nombre = input("Ingrese el nombre del trainer: ")
            apellido = input("Ingrese el apellido del trainer: ")
            direccion = input("Ingrese la dirección del trainer: ")
            celular = int(input("Ingrese el número de telefono del trainer: "))
            numero_fijo = int(input("Ingrese el número fijo del trainer: "))

            #! Guardamos los anteriores datos en el siguiente diccionario

            nuevo_trainer = {
                "identificacion": identificacion,
                "nombre": nombre,
                "apellidos": apellido,
                "direccion": direccion,
                "celular": celular,
                "fijo": numero_fijo,
            }

            #! Guardammos la informacion del nuevo trainer al final del diccionario de "datos_trainers". Cuando todo este combinado (la informacion existente con la nueva), lo guardaremos en trainers.json

            datos_trainers.append(nuevo_trainer)
            guardar_en_json(datos_trainers, "trainers.json")

            print("El nuevo trainer Fue agregado con éxito.")
            tecla_continuar()
            limpiar_pantalla()
            return None

        except ValueError:
            print("Por favor ingrese un dato válido.")
            tecla_continuar()
            limpiar_pantalla()

def listar_trainers(): # Funcion para listar los trainers
    limpiar_pantalla()
    #! Cargamos los datos de los trainers, si no los hay, retornaremos "none" para salir de la función.
    lista_de_trainers = cargar_datos_json("trainers.json")
    if lista_de_trainers is None:
        print("No hay trainers almacenados aún.")
        tecla_continuar()
        limpiar_pantalla()
        return None

    #! Imprimimos la lsita de trainers
    print('LISTA DE TRAINERS')
    for trainer in lista_de_trainers:
        for datos in trainer:
            print(datos,':',trainer[datos])
        print('---------------------------')
    tecla_continuar()
    limpiar_pantalla()