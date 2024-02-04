# Este archivo guarda todos los menús que serán utilizados dentro del programa
from tools.utilidades import validar_opcion

def menu_principal(): #Menu de menus
    print("***************[MENU PRINCIPAL]***************")
    print("* 1.---------------------------------Campers *")
    print("* 2.--------------------------------Trainers *")
    print("* 3.-----------------------------------Salir *")
    print("**********************************************")
    opcion = validar_opcion(1,3)
    return opcion

def menu_campers(): #Menu de campers
    print("***************[CAMPERS]***************")
    print("* 1.--------------------------Campers *")
    print("* 2.----------------------------Salir *")
    print("***************************************")
    opcion = validar_opcion(1,2)
    return opcion