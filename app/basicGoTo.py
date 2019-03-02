import random

def basicGoTo(data, cords):

    me = data['you']['body'][0]
    movement = random.choice(['up', 'right', 'down', 'left'])
    
    if cords[0] < me['x']:
        movement = 'left'
    elif cords[0] > me['x']:
        movement = 'right'
    elif cords[1] > me['y']:
        movement = 'down'
    elif cords[1] < me['y']:
        movement = 'up'

    return movement