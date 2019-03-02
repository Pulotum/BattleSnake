def basicGoTo(data, food):

    me = data['you']['body'][0]
    
    if food['x'] < me['x']:
        movement = 'left'
    elif food['x'] > me['x']:
        movement = 'right'
    elif food['y'] > me['y']:
        movement = 'down'
    elif food['y'] < me['y']:
        movement = 'up'

    return movement