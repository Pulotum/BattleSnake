import math

# maps 2D array location to a 1D array position
# location is [x,y] coordiniate
# width of game board


def mapToVertex(location2D, width):
    return width * location2D['x'] + location2D['y']

# maps 1D array position to 2D array position
# returns dictionary


def VertexToMap(locationVertice, width):
    col = math.floor(locationVertice / width)
    row = locationVertice % width
    location2D = {'x': row, 'y': col}

    return location2D


def main():
    test = {'x': 1, 'y': 2}
    result = mapToVertex(test, 3)
    print(result)

    result = VertexToMap(0, 3)
    print(result)


if __name__ == "__main__":
    main()
