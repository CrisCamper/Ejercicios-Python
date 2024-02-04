# Este archivo tendrá todas las funciones que utilizaremos para registrar campers, etc.

from tools.utilidades import validar_opcion, guardar_en_json

def registrar_camper(): #Funcion para registrar un camper
    while True:
        try:

            #! Aqui escribiremos los datos del camper

            while True: # bucle para prevenir que el usuario ingrese un dato erroneo
                try:
                    identificacion = int(input("Ingrese el número de identificación: "))
                    break
                except ValueError:
                    print("Por favor Ingrese un dato válido.")
            
            nombre = input("Ingrese el nombre del camper: ")
            apellido = input("Ingrese el apellido del camper: ")
            direccion = input("Ingrese la dirección del camper: ")
            acudiente = input("Acudiente del camper: ")
            
            while True: # bucle para prevenir que el usuario ingrese un dato erroneo
                try:
                    celular = int(input("Ingrese el número de telefono del camper: "))
                    numero_fijo = int(input("Ingrese el número fijo del camper: "))
                    break
                except ValueError:
                    print("Por Favor ingrese un dato valido.")
            
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

            camper = {
                "identificacion": identificacion,
                "nombre": nombre,
                "apellidos": apellido,
                "direccion": direccion,
                "acudiente": acudiente,
                "celular": celular,
                "fijo": numero_fijo
            }

            guardar_en_json(camper, 'campers')

        except ValueError:
            print("Por favor ingrese un dato válido.")