#Programa para calcular el área de un circulo
#Entrada: radio
#Salida: Área y Perimetro

def areaCirculo(radio):#función para calcular el área de un circulo
    area = float(3.14 * (radio)**2)
    print(f'El area del circulo es: {area}')

def perimetroCircle(radio):#función para calcular el área de un círculo
    perimetro = float((2*3.14)*(radio))
    print(f'El perimetro del circulo es: {perimetro}')


#Le pedimos al usuario el radio y el perímetro del círculo

radio = int(input('Ingrese el radio del circulo: '))
areaCirculo(radio)
perimetroCircle(radio)
