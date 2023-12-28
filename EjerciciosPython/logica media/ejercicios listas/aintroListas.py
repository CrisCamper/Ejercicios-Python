#LISTAS

# Crear una lista con las 5 ciudades que más le gusten

    #cities = ['Bucaramanga', 'Cucuta', 'Medellín', 'Bogotá', 'Santa Marta']

    #for city in cities:
        #print(city)

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

# Ocurrency number
# for check how many times appear a valor
# with function .count(value)

    #sheldon_greeting = ['Penny', 'Penny', 'Penny', 'Penny']
    #print(sheldon_greeting.count('Penny')) # Penny appears 4 times 

# convert list to string
# with function .join(list)

    #shopping = ['Huevos', 'Aceite', 'Pan']
    #print(', '.join(shopping)) # Print the list like string separated with a space or whatever

# Organize a list
# Conservating the original list
# With the function sorted(list)

    #shopping = ['Huevos', 'Aceite', 'Pan']
    #print(sorted(shopping)) # Return a new list ordened

# Modificating original list
# With Function .sort()

    #shopping = ['Huevos', 'Aceite', 'Pan']
    #shopping.sort()
    #print(shopping)

# Iterar using enumeration
# for know the index inside him
# with function enumerate(list)

    #shopping = ['Huevos', 'Aceite', 'Pan']
    
    #for i, product in enumerate(shopping):
    #    print(i, product)

# Iterate in multiples lists
# With function zip()

    #shopping = ['Huevos', 'Aceite', 'Pan']
    #details = ['A3', 'de oliva extra virgen', 'Francés']
    
    #for product, detail in zip(shopping, details):
    #    print(product, detail)

# Exercise: dados dos vectores(listas) de la misma dimensión, utilizar la funcion zip() para calcular su producto escalar

    #v1 = [4, 3, 8, 1]
    #v2 = [9, 2, 7, 3]
    
    #product_escalar = 0
    
    #for i1, j1 in zip(v1, v2):
    #    mult = i1 * j1
    #    product_escalar = product_escalar + mult
    
    #print(product_escalar)

# Comparate lists
# Example: [1, 2, 3] < [1, 2, 4] = True
# Python compares element to element

# Careful with the copies
# A simple change in the list, changes completaly the copy list and the original list

    #original_list = [1, 2, 3, 4]
    #copy_list = original_list
    #original_list[0] = 15
    #print(original_list)
    #print(copy_list)

# Multiply veracity
# if all conditions are met all()
# If any conditions are met any()