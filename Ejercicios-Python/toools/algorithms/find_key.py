# This function could help you to find a specific key of a dict

def find_key(name_key, dictionary): # Function for nested dicts
    found_key = None
    for player_key, player_data in dictionary.get('players', {}).items():
        if name_key in player_data:
            found_key = player_data.get(name_key)
            break
    return found_key

#! Example usage

'''
data = {
    'players': {
        'P1': {
            'Name': 'Carlos',
            'Age': 24,
            'Sons': False
        }
    }
}

def find_key(name_key, dictionary):
    found_key = None
    for player_key, player_data in dictionary.get('players', {}).items():
        if name_key in player_data:
            found_key = player_data.get(name_key)
            break
    return found_key

key = find_key('Name', data)
print(key) # print carlos
''' 