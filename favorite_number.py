import json
def save_number():
    '''Save the user favorite number into a json file.'''
    number = int(input('Type your favorite number and a will save it for you: '))
    with open('favorite_number.json', 'w') as file_object:
        json.dump(number, file_object)
    return number

def read_number():
    '''Read the json file that contain the user favorite numver'''
    try:
        with open('favorite_number.json') as file_object:
            number = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return number

def show_number():
    '''If the user already informed a number it will show to him/her. Otherwise the function save_number will be called to ask the user his/her favorite number'''
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
