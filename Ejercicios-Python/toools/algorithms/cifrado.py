# Function to encrypt a message

def encrypt_message(key,message):
    alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    key = key
    message = message
    encryption = ''

    for letter in message:
        if letter.upper() in alphabet:  # Convertir a mayúscula para manejar minúsculas
            original_index = alphabet.find(letter.upper())
            excryption_index = (original_index + key) % len(alphabet)
            encryption_letter = alphabet[excryption_index]

            encryption += encryption_letter
        else:
            encryption += letter

    return encryption

while True:
    try:
        # Presentation
        print('***********************************')
        print('*|WELCOME TO THE CESAR ENCRYPTION|*')
        print('***********************************')

        # Requirements
        message = input('Type a message to encrypt: ')
        key = int(input('Type a key to encrypt (1,2,3...): '))

        #Encryptation
        encryp_message = encrypt_message(key,message)
        print('*************************')
        print('*  |...ENCRYPTING...|   *')
        print('*************************')
        print('*|SUCCESFULLY ENCRYPTED|*')
        print('*************************')
        print('X'*len(encryp_message)+'XXXX')
        print('X',encryp_message,'X')
        print('X'*len(encryp_message)+'XXXX')
        print('\n Made by Chulo...')

        break
    except ValueError:
        print('Please type a valid data')
