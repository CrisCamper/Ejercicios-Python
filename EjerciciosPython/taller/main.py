# Pedir dato numérico al usuario
from utils import verifyInt, verifyStr, verifyIntPos

age = input('Ingrese su edad: ')
verifyInt(age)

name = input('Ingrese nombre: ')
verifyStr(name)

num_fav_positive = input('Ingrese su numero preferido positivo: ')
verifyIntPos(num_fav_positive)