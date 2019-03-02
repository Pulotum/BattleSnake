def returnMap(data):

    width = data['board']['width']
    height = data['board']['height']

    map = [[0 for x in range(width)] for y in range(height)] 

    #add all other snakes
    for enemy_snake in data['board']['snakes']:
        for enemy_pos in enemy_snake['body']:
            map[ enemy_pos['y'] ][ enemy_pos['x'] ] = 'E'

    #add yourself
    for you in data['you']['body']:
        map[ you['y'] ][ you['x'] ] = 'S'

    #add food
    for food in data['board']['food']:
        map[ food['y'] ][ food['x'] ] = 'F'

    #flip map
    '''
    i = 0
    for x in map:
        map[i] = x[::-1]
        i += 1
        
    map = map[::-1]
    '''

    return map