def returnMap(data):

    width = data['board']['width']
    height = data['board']['height']

    name = data['you']['name']

    map = [[' ' for x in range(width)] for y in range(height)] 

    #add all other snakes
    for snake in data['board']['snakes']:

        if snake['name'] != name:
            #enemy snake
            for enemy_pos in snake['body']:
                map[ enemy_pos['y'] ][ enemy_pos['x'] ] = 'E'

        else:
            #our snake
            for you_pos in snake['body']:
                map[ you_pos['y'] ][ you_pos['x'] ] = 'S'



    #add food
    #for now ignore food locations
    for food in data['board']['food']:
        map[ food['y'] ][ food['x'] ] = 'F'

    return map