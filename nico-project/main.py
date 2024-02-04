from tools.menus import *
from tools.utilidades import limpiar_pantalla
from actors.campers import registrar_camper


# funciones comprimidas
def camper(): #Funcion camper (Abarca todo lo que tiene que ver con campers)
    opcion = menu_campers()
    if opcion == 1: # Si la opcion es registar camper, ejecutaremos la funcion de registrarlo
        registrar_camper()
    elif opcion == 2: # Si la opcion es salir del menu de campers, retornaremos "nada" para entrar al menu principals
        limpiar_pantalla()
        return None

# Inicio del programa
while True:
    opcion = menu_principal()
    if opcion == 1: # Si la opcion es igual a 1, ejecutará la función camper
        # Limpiamos pantalla para simular el cambio de ventana
        limpiar_pantalla()
        camper()
    elif opcion == 3: # Si la opcion es 3, finalizaremos el programa
        # Limpiamos pantalla para simular el cambio de ventana
        limpiar_pantalla()
        print("Ten un lindo día")
        break