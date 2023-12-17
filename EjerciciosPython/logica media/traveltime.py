# program to calculate the time of a journey
# ask the leg of the travel
# the program stops asking when the user gives a zero
# send like a result the time in hours 

def calcularHora (h): # Function for calculating number
    resultado = round((1*h)/60)
    module = (h%60)

    if module < 10: # Condicion para add 0 en caso de que el modulo de menor a 10
        rta = (f'{resultado}:0{module}')
    else:
        rta = (f'{resultado}:{module}')
   
    return rta


suma_tramo = 0 # starting variable
tramo = 1 # Starting varible for enter into the cicle

while tramo != 0:
    tramo = int(input('Ingrese tramo: '))
    suma_tramo = tramo + suma_tramo
    h = suma_tramo

print(calcularHora(h)) # print the variable h