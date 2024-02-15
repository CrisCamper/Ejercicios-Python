#This function could help you generate infinite codes with a unique sequence.

def code_generator(prefix, start, end):
    for id in range(start, end):
        yield f'{prefix}{id}'  # I'm use yield to generate values one by one


#* You can use start and end or you can generate infinite codes with the examples 
#* A example of usages:

#! generation consecutive

'''
count = 0

while True:
    op = input("Do you want to generate a code? [y/n] ")
    
    if op.lower() == 'y': #? Lower convert uppercase letters to lowercase
        count += 1
        generated_id = next(code_generator('A', count, count + 1)) #? I use next to generate the next code generate
        print(generated_id)
    elif op.lower() == 'n':
        break

'''

#! generation standard

'''
while True:
    op = input("Do you want to generate a code? [y/n] ")
    
    if op.lower() == 'y':
        generated_id = next(code_generator('A', 1, 10)) # Just 10 entries
        print(generated_id)
    elif op.lower() == 'n':
        break
'''