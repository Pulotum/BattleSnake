def returnMap(data):

    width = data['board']['width']
    height = data['board']['height']

    map = [[0 for x in range(width)] for y in range(height)] 

    #add all other snakes
    for enemy_snake in data['board']['snakes']:
        i = 0
        for enemy_pos in enemy_snake['body']:
            #snake head
            if i == 0:
                #add up
                map[ enemy_pos['y'] - 1 ][ enemy_pos['x'] ] = 1
                #add right
                map[ enemy_pos['y'] ][ enemy_pos['x'] + 1 ] = 1
                #add down
                map[ enemy_pos['y'] + 1 ][ enemy_pos['x'] ] = 1
                #add left
                map[ enemy_pos['y'] ][ enemy_pos['x'] - 1 ] = 1

            map[ enemy_pos['y'] ][ enemy_pos['x'] ] = 1
            i += 0

    #add yourself
    for you in data['you']['body']:
        map[ you['y'] ][ you['x'] ] = 2

    #add food
    #for now ignore food locations
    for food in data['board']['food']:
        map[ food['y'] ][ food['x'] ] = 3

    return map