#diagonal principal : X
#parte inferior : D
#parte superior : U
#obtener tamaño

size = int(input('Input the size: '))

for i in range(1, (size+1)):
    print('D '*(i-1)+'X '+'U '*(size-i))