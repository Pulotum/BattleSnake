''''
    receives vertex coordinate as int and returns neighbor locations
'''
import mapCoordinates


def findNeighbours(vertex, width, height):
    # convert to 2D for ease of use
    arrayCoordinate = mapCoordinates.VertexToMap(vertex, width)

    neighbors = []

    # left of
    arrayCoordinate['x'] -= 1
    if(checkRange(arrayCoordinate, width, height) == True):
        neighbors.append(mapCoordinates.mapToVertex(arrayCoordinate, width))

    # right of
    arrayCoordinate['x'] += 2
    if(checkRange(arrayCoordinate, width, height) == True):
        neighbors.append(mapCoordinates.mapToVertex(arrayCoordinate, width))

    # up of
    arrayCoordinate['x'] -= 1
    arrayCoordinate['y'] += 1
    if(checkRange(arrayCoordinate, width, height) == True):
        neighbors.append(mapCoordinates.mapToVertex(arrayCoordinate, width))

    # down of
    arrayCoordinate['y'] -= 2
    if(checkRange(arrayCoordinate, width, height) == True):
        neighbors.append(mapCoordinates.mapToVertex(arrayCoordinate, width))

    return neighbors


def checkRange(coordinate, width, height):
    if (coordinate['x'] < 0 or coordinate['x'] > width-1 or coordinate['y'] < 0 or coordinate['y'] > height-1):
        print("if")
        print(coordinate['x'])
        print(coordinate['y'])
        return False
    else:
        print("else")
        print(coordinate['x'])
        print(coordinate['y'])
        return True

# tests


def main():
    result = findNeighbours(0, 3, 2)
    print(result)


if __name__ == "__main__":
    main()
