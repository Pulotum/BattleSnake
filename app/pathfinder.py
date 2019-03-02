def find_path(data, map, goal, start):
    width = data['board']['width']
    height = data['board']['height']

    # dist and prev arrays for visited and unvisited vertices
    dist = [[10000 for x in range(width)] for y in range(height)] 
    prev = [[0 for x in range(width)] for y in range(height)] 
    vertices = [["N" for x in range(width)] for y in range(height)] 

    dist[goal['x']][goal['y']] = 0

    curr_min = 10000
    for x_index, x in enumerate(vertices):
        for y_index, y in enumerate(x):
            if dist[x][y] < curr_min:
            curr_min = dist[x_index][y_index]

    print "we did it"
    return 420
    

def distance(start, goal):
    dist_x = abs(start['x'] - goal['x'])
    dist_y = abs(start['y'] - goal['y'])
    return dist_x + dist_y