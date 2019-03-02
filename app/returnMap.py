def returnMap(data):

    width = data['board']['width']
    height = data['board']['height']

    name = data['you']['id']

    #icons
    icon_potential = 'x'
    icon_enemy = 'x'
    icon_snake = 'x'
    icon_food = 'f'

    map = [[' ' for x in range(width)] for y in range(height)] 

    #add all other snakes
    for snake in data['board']['snakes']:

        if snake['id'] != id:
            #enemy snake
            count = 0
            for enemy_pos in snake['body']:
                if count == 0:
                    #add potential to up
                    if (enemy_pos['y'] - 1) >= 0:
                        map[ enemy_pos['y'] - 1 ][ enemy_pos['x'] ] = icon_potential

                    #add potential to down
                    if (enemy_pos['y'] + 1) < height:
                        map[ enemy_pos['y'] + 1 ][ enemy_pos['x'] ] = icon_potential

                    #add potential to right
                    if (enemy_pos['x'] + 1) < width:
                        map[ enemy_pos['y'] ][ enemy_pos['x'] + 1 ] = icon_potential

                    #add potential to left
                    if (enemy_pos['x'] - 1) >= 0:
                        map[ enemy_pos['y'] ][ enemy_pos['x'] - 1 ] = icon_potential

                map[ enemy_pos['y'] ][ enemy_pos['x'] ] = icon_enemy
                count += 1

        else:
            #our snake
            for you_pos in snake['body']:
                map[ you_pos['y'] ][ you_pos['x'] ] = icon_snake



    #add food
    #for now ignore food locations
    for food in data['board']['food']:
        map[ food['y'] ][ food['x'] ] = icon_food

    return map