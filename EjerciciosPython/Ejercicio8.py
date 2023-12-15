# Programa para calcular la nota que necesito
# Entrada: certamen1, certamen2, nota_lab
# Salida: nota certamen 3

def calcular_certamen3(cert_1, cert_2, nota_lab): 
    Nc = 60 * 0.7 + nota_lab * 0.3
    cert_3 = (cert_1 + cert_2 - Nc) / 3
    return cert_3

# Entrada de datos
cert_1 = float(input('Ingrese la nota del certamen 1: '))
cert_2 = float(input('Ingrese la nota del certamen 2: '))
nota_lab = float(input('Ingrese la nota del laboratorio: '))

# Calcular y mostrar el resultado
resultado = calcular_certamen3(cert_1, cert_2, nota_lab)
print(f'Necesitas {resultado:.2f} en el certamen 3 para alcanzar la nota deseada.')
