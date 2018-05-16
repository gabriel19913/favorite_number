import json
def save_number():
    number = int(input('\nType your favorite number and a will save it for you: '))
    with open('favorite_number.json', 'w') as file_object:
        json.dump(number, file_object)
    return number

def read_number():
    try:
        with open('favorite_number.json') as file_object:
            number = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return number

def show_number():
    number = read_number()
    if number:
        print('\n------------------------------------------------------------')
        print('I know what is your favorite number. It is: {}!'.format(number))
        print('------------------------------------------------------------')
    else:
        print('\n------------------------------------------------------------')
        print('Your favorite number is not saved.')
        number = save_number()
        print('The number {} was saved as your favorite number.'.format(number))
        print('------------------------------------------------------------')

show_number()