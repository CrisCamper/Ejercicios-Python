# TUPLES

#Making tuples

    #empty_tuple = ()
    #tenerife_geoloc = (26.8976, -16.3456)
    #three_wise_men = ('Melchor', 'Gaspar', 'Baltasar')
    #print(empty_tuple, '/',tenerife_geoloc, '/',three_wise_men) # Imprime as variadas tuplas que hemos creado

#Tuples of a only element
# We can make a tuple of only element of the next form:

    #only_element = ('Only Element', ) # We add a comma to end
    #print(type(only_element)) # class tuple

# something has cases that we can find tuples without parentheses

    #tuple_without = 'Machine', 'Strong', 'Discipline'
    #print(type(tuple_without)) # class tuple

# Convertions
# The convertion is only availiable for items iterables, numbers are not acepted

    #shopping = ['Agua', 'Aceite', 'Pan']
    #print(tuple(shopping)) # List convert to tuple

# the use of function tuple() withouth arguments, is the same to create a empty tuple
# Unboxing of tuples, is the same like lists

    #foods = ('Pastel', 'Pasta', 'Arroz')
    #food1, food2, food3 = foods
    #print(food1, food2, food3) # pastel, pasta, arroz  

# Summary: Tuples are almost the same as lists, the only difference is that tuples cannot be modified, tuples are immutable