# Este archivo nos servirá para suplir necesidades del programador y para que otros modulos funcionen
import os
import json

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


