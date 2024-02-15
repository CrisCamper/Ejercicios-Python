#DICTIONARY#
# Example of Dictionary mix the real life with python

    #Play: -------> Password
    #Do something with joy in order to entertain yourself, have fun or develop certain abilities -------> value

#Making Dictionaries
# To create a dictionary we use keys {} around assignments password: value that are separated by commas

    #empty_dict = {}

    #rae = {
        #'bifronte': 'De dos frentes o dos caras',
        #'anarcoide': 'Que tiende al desorden',
        #'montuvio': 'Campesino de la costa'
    #}
    #population_can = {
        #2015: 2_234_546,
        #2016: 2_548_786,
        #2017: 2_890_234
    #}
    
    #print(f'{rae}\n{population_can}') # Print rae and population_can

#Exercise: make a dictionary with names and ages of 5 members of your family

    #family = {
        #'Kimberlyn': 30,
        #'Alvaro': 57,
        #'Nicolás': 8,
        #'Cristopher': 17,
        #'Lucas': 9
    #}

    #print(family)
 
#OPERATIONS WITH DICTIONARIES
#Obtain a element

    #rae = {
        #'bifronte': 'De dos frentes o dos caras',
        #'anarcoide': 'Que tiende al desorden',
        #'montuvio': 'Campesino de la costa'
        #}

    #print(rae['anarcoide']) # Que tiende al desorden


#Using get()
#If the key exist, it return us its value
#If the key does not exist, it returns 'None' or another value that we assign to it

    #rae = {
        #'bifronte': 'De dos frentes o dos caras',
        #'anarcoide': 'Que tiende al desorden',
        #'montuvio': 'Campesino de la costa'
    #}

    #print(rae.get('bifronte')) # De dos frentes o dos caras
    #print(rae.get('programación')) # None
    #print(rae.get('programación', 'No disponible')) # No disponible

#Add or Modify a element
# To add an element to the dictionary simply reference the key and add a value to it

    #rae = {
    #    'bifronte': 'De dos frentes o dos caras',
    #    'anarcoide': 'Que tiende al desorden',
    #    'montuvio': 'Campesino de la costa'
    #}
    
    #rae['jugar'] = 'Hacer algo divertido con el fin de entretenerse' # Add 'jugar' to diccionary
    #print(rae)
    #rae['Jugar'] = 'Realizar actividades divertidas para entretenerse' # Change the value of 'jugar' for another
    #print(rae)

#Creating from empty

    #VOWELS = 'aeiou'
    #enum_vowels = {}
    #
    #for i, vowel in enumerate(VOWELS, start=1):
    #    enum_vowels[vowel] = i
    #
    #print(enum_vowels)

