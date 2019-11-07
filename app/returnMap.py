def returnMap(data, method='display'):

    width = data['board']['width']
    height = data['board']['height']

    our_id = data['you']['id']

    #icons
    if method=='display':
        icon_potential = 'p'
        icon_enemy = 'x'
        icon_snake = 's'
        icon_edible_snake = 'e'
        icon_food = 'f'
        icon_head = 'h'
        icon_tail = 'T'
    else:
        icon_potential = 'x'
        icon_enemy = 'x'
        icon_snake = 'x'
        icon_edible_snake = 'f'
        icon_food = 'f'
        icon_head = 'x'
        icon_tail = 'T'

    our_length = len(data['you']['body'])

    map = [[' ' for x in range(width)] for y in range(height)] 
    
    #add food
    for food in data['board']['food']:
        map[ food['y'] ][ food['x'] ] = icon_food   

        
    #define out head and tail seperate from snake
    for snake in data['board']['snakes']:

        if snake['id'] == our_id:
            #our snake
            for you_pos in snake['body']:
                map[ you_pos['y'] ][ you_pos['x'] ] = icon_snake
                
    our_snake = data['you']['body']
    map[ our_snake[0]['y'] ][ our_snake[0]['x'] ] = icon_head
    map[ our_snake[-1]['y'] ][ our_snake[-1]['x'] ] = icon_tail

    
    #add all other snakes
    for snake in data['board']['snakes']:

        if snake['id'] != our_id:
            #enemy snake
            count = 0
            for enemy_pos in snake['body']:
                enemy_length = len(snake['body'])
                #if enemy head
                if count == 0:

                    map[ enemy_pos['y'] ][ enemy_pos['x'] ] = icon_enemy
                    
                    # if we are smaller
                    if our_length <= enemy_length:
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
                   
                    # if we are larger
                    else:
                        map[ enemy_pos['y'] ][ enemy_pos['x'] ] = icon_edible_snake
               
                # rest of body
                else:
                    map[ enemy_pos['y'] ][ enemy_pos['x'] ] = icon_enemy

                count += 1

        else:
            #our snake
            for you_pos in snake['body']:
                map[ you_pos['y'] ][ you_pos['x'] ] = icon_snake



    return map