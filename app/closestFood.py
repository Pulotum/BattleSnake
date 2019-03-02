'''

head    - array[ x,y ] cords of our snake head
food    - array[ array[x,y] ] of all food items

return  - array[ x,y ] of closest food item

'''
from operator import itemgetter


def closestFood(head, food):
    # store distances from head to food
    distances = []

    # loop through food items, find manhattan distance to head
    i = 0
    for foodLocation in food:
        Xdistance = abs(foodLocation[0] - head[0])
        Ydistance = abs(foodLocation[1] - head[1])
        # keep count of distance and corresponding food array location
        distances[i] = [[Xdistance + Ydistance], [i]]
        i += 1

    # sort distancs by manhattan distance
    distances = sorted(distances, key=itemgetter(0))

    # return  - array[ x,y ] of closest food item
    return food[distances[0][1]]
