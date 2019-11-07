import json
import os
import random
import bottle

from api import ping_response, start_response, move_response, end_response

import returnMap
import closestFood
import pathfinder
import basicGoTo
import breathFirst

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''


@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')


@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()


@bottle.post('/start')
def start():
    data = bottle.request.json

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    #print(json.dumps(data))

    color = "#4E3629"

    return start_response(color)


@bottle.post('/move')
def move():
    data = bottle.request.json

    direction = ''

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    # print(json.dumps(data))

    game_id = data['game']['id']
    game_turn = data['turn']

    head = data['you']['body'][0]
    tail = data['you']['body'][-1]
    health = data['you']['health']
    map = returnMap.returnMap(data)
    food = closestFood.closestFood(data)

    #nice = pathfinder.find_path(data, map, food, {1,1})
    #print nice

    #print food
    #print head

    #print map

    #go to food -> tail -> random space

    path_tail = breathFirst.breathFirst(data, map, (head['x'], head['y']), 'T')
    path_food = breathFirst.breathFirst(data, map, (head['x'], head['y']), 'f')

    if health <= 50:
        if path_food is not None:
            path = path_food
            goal = 'food'
        elif path_tail is not None:
            if game_turn > 2:
                path = path_tail
                goal = 'tail'
            else:
                path = breathFirst.breathFirst(data, map, (head['x'], head['y']), ' ')
                goal = 'space'
        else:
            path = breathFirst.breathFirst(data, map, (head['x'], head['y']), ' ')
            goal = 'space'
    else:
        if path_food is not None and path_tail is not None:
            if len(path_food) <= len(path_tail):
                path = path_food
                goal = 'food'
            else:
                if game_turn > 2:
                    path = path_tail
                    goal = 'tail'
                else:
                    path = breathFirst.breathFirst(data, map, (head['x'], head['y']), ' ')
                    goal = 'space'
        elif path_tail is not None:
            if game_turn > 2:
                path = path_tail
                goal = 'tail'
            else:
                path = breathFirst.breathFirst(data, map, (head['x'], head['y']), ' ')
                goal = 'space'
        elif path_food is not None:
            path = path_food
            goal = 'food'
        else:
            path = breathFirst.breathFirst(data, map, (head['x'], head['y']), ' ')
            goal = 'space'
        
    
    # if health <= 50:
    #     if food:
    #         path = breathFirst.breathFirst(data, map, (head['x'], head['y']), 'f')
    #         goal = 'food'
    #         if path is None:
    #             #check if for turn length
    #             if data['turn'] > 2:
    #                 #turn is greater than 2 go to tail
    #                 path = breathFirst.breathFirst(data, map, (head['x'], head['y']), 'T')
    #                 goal = 'tail'
    #                 if path is None:
    #                     path = breathFirst.breathFirst(data, map, (head['x'], head['y']), ' ')
    #                     goal = 'space'
    #             else:
    #                 #turn is short dont go to tail
    #                 path = breathFirst.breathFirst(data, map, (head['x'], head['y']), ' ')
    #                 goal = 'space'
    #     else:
    #         #check if turn length is shorter than 2
    #         if data['turn'] > 2:
    #             #turn is greater go to tail
    #             path = breathFirst.breathFirst(data, map, (head['x'], head['y']), 'T')
    #             goal = 'tail'
    #             if path is None:
    #                 path = breathFirst.breathFirst(data, map, (head['x'], head['y']), ' ')
    #                 goal = 'space'
    #         else:
    #             #goto empty
    #             path = breathFirst.breathFirst(data, map, (head['x'], head['y']), ' ')
    #             goal = 'space'
    
    # else:
    #     if data['turn'] > 2:
    #         #turn is greater than 2 go to tail
    #         path = breathFirst.breathFirst(data, map, (head['x'], head['y']), 'T')
    #         goal = 'tail'
    #         if path is None:
    #             path = breathFirst.breathFirst(data, map, (head['x'], head['y']), ' ')
    #             goal = 'space'
    #     else:
    #         #turn is short dont go to tail
    #         path = breathFirst.breathFirst(data, map, (head['x'], head['y']), ' ')
    #         goal = 'space'


    #print goal
    #print path
    next = path[1]
    direction = basicGoTo.basicGoTo(data, next)


    ##########################################
    ##########################################
    # print json.dumps( map )
    print json.dumps({
        'id': game_id,
        'turn': game_turn,
        'goal': goal,
        'dir': direction,
        'map': json.dumps(returnMap.returnMap(data,'display'))
    })
    ##########################################
    ##########################################


    #print next
    #print direction

    return move_response(direction)


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    # print("---------- ---------- END OF GAME ---------- ----------")
    # print(json.dumps(data))

    return end_response()


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
