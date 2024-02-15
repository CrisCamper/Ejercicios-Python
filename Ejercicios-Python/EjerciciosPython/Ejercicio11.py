#Programa para calcular la cantidad de vocales

word = input('input a word: ')
cont_vocales = 0

vowels = set('aeiou')  # conjunto

for letter in word:
    if letter in vowels:
        cont_vocales += 1

print('quantity of vocales:', cont_vocales)
