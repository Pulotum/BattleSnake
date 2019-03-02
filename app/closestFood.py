from operator import itemgetter


def closestFood(data):
    board = data['board']
    food = board['food']

    snake = data['you']
    head = snake['body'][0]

    # store distances from head to food
    distances = []

    # loop through food items, find manhattan distance to head
    i = 0
    for foodLocation in food:
        Xdistance = abs(foodLocation['x'] - head['x'])
        Ydistance = abs(foodLocation['y'] - head['y'])
        # keep count of distance and corresponding food array location
        distances.append([(Xdistance + Ydistance), i])
        i += 1

    # sort distancs by manhattan distance
    distances = sorted(distances, key=itemgetter(0))

    # return  - array[ x,y ] of closest food item
    return food[distances[0][1]]
