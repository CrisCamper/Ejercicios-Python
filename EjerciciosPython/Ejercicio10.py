#Programa que encuentre todos los multiplos de 5 menores que un valor dado
#Entrada: 36
#Salida: 5,10,15...,35

num_limite = int(input('Input a number: '))
result = 0 #Inicializamos la variable controladora

while result < num_limite:
    if result % 5 == 0:
        print(result)
    result += 1 #Por cada iteracion, aumentamos en uno la variable result
print('Come back soon!')