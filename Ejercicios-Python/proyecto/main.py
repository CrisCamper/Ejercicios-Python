from tools.menus import * # Importamos todas las funciones que se encuentran en la carpeta tools, archivo menus (importamos absolutamente todos los menus)
from tools.utilidades import limpiar_pantalla # Importamos la función de limpiar pantalla que se encuentra en la carpeta tools archivo utilidades (Importamos solo la funcion especificada)
from actors.campers import registrar_camper,listar_campers # Importamos las funciones registrar campers y listar campers que se encuentran en la carpeta actors, archivo campers
from actors.trainers import registrar_trainer, listar_trainers

# funciones comprimidas
def camper(): #Funcion camper (Abarca absolutamente todo lo que tiene que ver con campers)
    opcion = menu_campers()
    if opcion == 1: # Si la opcion es registar camper, ejecutaremos la funcion de registrarlo
        registrar_camper()
    elif opcion == 2: # Si la opcion es listar camper, ejecutaremos la función de listarlos
        listar_campers()
    elif opcion == 3: # Si la opcion es salir del menu de campers, retornaremos "nada" para entrar al menu principal
        limpiar_pantalla()
        return None

def trainer(): #Funcion trainer (Abarca absolutamente todo lo que tiene que ver con trainers)
    opcion = menu_trainers()
    if opcion == 1: # Si la opcion es registar trainer, ejecutaremos la funcion de registrarlo
        registrar_trainer()
    elif opcion == 2: # Si la opcion es listar trainer, ejecutaremos la función de listarlos
        listar_trainers()
    elif opcion == 3: # Si la opcion es salir del menu de trainers, retornaremos "nada" para entrar al menu principal
        limpiar_pantalla()
        return None


# Inicio del programa
while True:
    opcion = menu_principal()
    if opcion == 1: # Si la opcion es igual a 1, ejecutará la función camper
        # Limpiamos pantalla para simular el cambio de ventana
        limpiar_pantalla()
        camper()
    elif opcion == 2: # Si la opcion es 2, Ejecutaremos la función trainer
        # Limpiamos pantalla para simular el cambio de ventana
        limpiar_pantalla()
        trainer()
    elif opcion == 3: # Si la opcion es 3, finalizaremos el programa
        # Limpiamos pantalla para simular el cambio de ventana
        limpiar_pantalla()
        print("Ten un lindo día")
        break 