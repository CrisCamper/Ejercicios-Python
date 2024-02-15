def brute_force_decryption(encrypted_message):
    alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    decrypted_messages = []

    for key in range(len(alphabet)):
        decryption = ''
        
        for letter in encrypted_message:
            if letter.upper() in alphabet:
                original_index = alphabet.find(letter.upper())
                decryption_index = (original_index - key) % len(alphabet)
                decryption_letter = alphabet[decryption_index]

                if letter.islower():
                    decryption_letter = decryption_letter.lower()

                decryption += decryption_letter
            else:
                decryption += letter

        decrypted_messages.append(decryption)

    for i, message in enumerate(decrypted_messages):
        print(f'Key {i}: {message}')


while True:
    try:
        # Presentation
        print('************************************')
        print('*|WELCOME TO THE CESAR DECIFRATION|*')
        print('************************************')

        # Requirements
        crypt = input('Type a message to decifrate: ')

        #Decifration
        decifrate_message = brute_force_decryption(crypt)
        print('***************************')
        print('*  |...DECIPHERING...|    *')
        print('***************************')
        print('* |LOADING POSSIBLES MSG| *')
        print('***************************')
        
        print('\n Made by Chulo...')

        break
    except ValueError:
        print('Please type a valid data')