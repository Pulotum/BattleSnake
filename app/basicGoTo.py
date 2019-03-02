import random

def basicGoTo(data, food):

    food['x'] = food[0]
    food['y'] = food[1]

    me = data['you']['body'][0]
    movement = random.choice(['up', 'right', 'down', 'left'])
    
    if food['x'] < me['x']:
        movement = 'left'
    elif food['x'] > me['x']:
        movement = 'right'
    elif food['y'] > me['y']:
        movement = 'down'
    elif food['y'] < me['y']:
        movement = 'up'

    return movement