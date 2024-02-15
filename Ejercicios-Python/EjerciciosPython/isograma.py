# Example Convertions

# With strings
    #text = input('Input string text: ')
    #print(list(text))

# With numbers
    #n = int(input('Input quantity of values: '))
    #print(list(range(n)))

# OPERATIONS WITH LISTS
# obtain a element

    #shopping = ['huevos', 'pan', 'aceite']
    #print(shopping[0])
    #print(shopping[-1]) # acceso con indice negativo

# trocear a list

    #shopping = ['Agua', 'Aceite', 'Huevos', 'Sal', 'Limón']
    #print(shopping[0:3])
    #print(shopping[:3])
    #print(shopping[2:4])
    #print(shopping[-1:-4:-1])
    #print(shopping[::-1]) # Equivale a invertir una lista

# Add at end of list
# with the function .append()

    #shopping = ['Agua', 'Aceite', 'Huevos', 'Sal', 'Limón']
    #print(shopping) # List no modified
    #shopping.append('Atún')
    #print(shopping) # List modified

# Creating from empty
# Make a list with the numbers from 0 to 20

    #even_numbers = []
    #
    #for i in range(20):
    #    if i % 2 == 0:
    #        even_numbers.append(i)
    #print(even_numbers)

# Add at whatever position of a list
# with function .insert()

    #shopping = ['Agua', 'Aceite', 'Huevos', 'Sal', 'Limón']
    #print(shopping) # List no modified
    #shopping.insert(1, 'Jamón')
    #print(shopping) # List modified

# Repeat elements 
# With the operator *

    #shopping = ['Huevos', 'Pan', 'Aceite']
    #print(shopping*3) # Imprime la lista 3 veces!

    # Something I would add is the ability to iterate the list with arithmetic functions.
    # Example

    #print(shopping*((3+5)//2)) # en total, imprimirá cuatro veces la lista. Algo inutil pero interesante

# Combinate lists
# Conservating original list
# With operator + or +=

    #shopping = ['Huevos', 'Pan', 'Aceite']
    #fruitshop = ['Piña', 'Naranja', 'Manzana']
    #print(shopping + fruitshop) # Combinara las dos listas conservando la original

# Modificating the original list
# With function .extend()

    #shopping = ['Huevos', 'Pan', 'Aceite']
    #fruitshop = ['Piña', 'Naranja', 'Manzana']
    #shopping.extend(fruitshop) # Modifica la lista shopping agregando elementos de la otra lista
    #print(shopping)

# Modify list
    
    #shopping = ['Huevos', 'Pan', 'Aceite']
    #shopping[0] = 'Nueces'
    #print(shopping)
    
# Modify list with troceado

    #shopping = ['Huevos', 'Pan', 'Aceite']
    #shopping[1:2] = ['Pastel', 'Vino']
    #print(shopping)

# Search element
# With Function .index()

    #shopping = ['Huevos', 'Pan', 'Aceite']
    #print(shopping.index('Huevos')) # Me imprimirá el indice del elemento

# Exercise, Determine if a string is an isogram (no letters are repeated)

    #isogram = list(input('Input a word: '))
    #
    #for letter in isogram:
    #    if isogram.count(letter) > 1:
    #        print("Isn't an isogram")
    #        break
    #else:
    #    print('Is an isogram')