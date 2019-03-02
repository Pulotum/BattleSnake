def returnMap(data):

    width = data['board']['width']
    height = data['board']['height']

    map = [[0 for x in range(width)] for y in range(height)] 

    #add all other snakes
    for enemy_snake in data['board']['snakes']:
        for enemy_pos in enemy_snake['body']:
            map[ enemy_pos['y'] ][ enemy_pos['x'] ] = 'x'

    #add yourself
    for you in data['you']['body']:
        map[ you['y'] ][ you['x'] ] = 'x'

    #add food
    for food in data['board']['food']:
        map[ food['y'] ][ food['x'] ] = '1'

    return map