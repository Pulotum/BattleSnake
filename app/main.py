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
    
    color = "#4E3629"

    return start_response(color)


@bottle.post('/move')
def move():
    data = bottle.request.json

    direction = ''

    # print(json.dumps(data))

    game_id = data['game']['id']
    game_turn = data['turn']

    head = data['you']['body'][0]
    tail = data['you']['body'][-1]
    health = data['you']['health']
    map = returnMap.returnMap(data)
    
    print json.dumps({
        'map': json.dumps(returnMap.returnMap(data,'display'))
    })

    path_tail = breathFirst.breathFirst(data, map, (head['x'], head['y']), 'T')
    path_food = breathFirst.breathFirst(data, map, (head['x'], head['y']), 'f')

    # if game turn is less than 2, always go for food
    if game_turn < 2:
        goal = 'food'
    else:
        # if hungry, make food top priority
        if health <= 50:
            if path_food is not None:
                goal = 'food'
            elif path_tail is not None:
                goal = 'tail'
            else:
                goal = 'space'
        else:
            if path_food is not None and path_tail is not None:
                if len(path_food) <= len(path_tail):
                    goal = 'food'
                else:
                    goal = 'tail'
            elif path_tail is not None:
                goal = 'tail'
            elif path_food is not None:
                goal = 'food'
            else:
                goal = 'space'

    safe = False
    tried = set()

    while not safe:
        # get path from priority
        if goal=='tail':
            path = path_tail
        elif goal=='food':
            path = path_food
        else:
            path = breathFirst.breathFirst(data, map, (head['x'], head['y']), ' ')

        # check if path is safe
        next = path[1]
        next_path = breathFirst.breathFirst(data, map, (next[0], next[1]), 'T')
        if next_path is not None:
            safe = True
        else:
            safe = False
            tried.add(goal)
            if 'tail' not in tried:
                goal = 'tail'
            elif 'food' not in tried:
                goal = 'food'
            else:
                safe = True
                path = breathFirst.breathFirst(data, map, (head['x'], head['y']), ' ')
                next = path[1]


    # get direction to go
    direction = basicGoTo.basicGoTo(data, next)

    ##########################################
    ##########################################
    print json.dumps({
        'id': game_id,
        'turn': game_turn,
        'goal': goal,
        'dir': direction,
        'map': json.dumps(returnMap.returnMap(data,'display'))
    })
    ##########################################
    ##########################################

    # return desired direction
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
