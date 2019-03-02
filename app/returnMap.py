def returnMap(data):

    width = data['board']['width']
    height = data['board']['height']

<<<<<<< HEAD
    map = [[0 for x in range(width)] for y in range(height)] 

    #add all other snakes
    for enemy_snake in data['board']['snakes']:
        for enemy_pos in enemy_snake['body']:
            map[ enemy_pos['x'] ][ enemy_pos['y'] ] = 'E'
=======
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

>>>>>>> b429599d233063108705947c73ced43d93c35035

    #add yourself
    for you in data['you']['body']:
        map[ you['x'] ][ you['y'] ] = 'S'

    #add food
    for food in data['board']['food']:
<<<<<<< HEAD
        map[ food['x'] ][ food['y'] ] = 'F'

    #flip map
    for x in map:
        map[x] = map[x][::-1]
    map = map[::-1]
=======
        map[ food['y'] ][ food['x'] ] = icon_food
>>>>>>> b429599d233063108705947c73ced43d93c35035

    return map