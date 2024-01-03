# Definir una funcion para verificar un dato númerico
def verifyInt (a):
    while True:
        try:
            int(a)
            print('Perfecto')
            break
        except:
            print('Incorrecto')
            break

def verifyStr (a):
    while True:
        try:
            int(a)
            print('Incorrecto')
            break
        except:
            print('Perfecto')
            break

def verifyIntPos (a):
    while True:
        try:
            a = int(a)
            if a < 0:
                print('Incorrecto')
                break
            else:
                print('Perfecto')
                break
        except:
            break