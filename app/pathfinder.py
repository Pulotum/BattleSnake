import returnMap
import mapCoordinates


def find_path(data, start, goal):
    width = data['board']['width']
    height = data['board']['height']

    map = returnMap.returnMap(data)

    # dist and visited arrays for visited and unvisited vertices
    dist = [10000 for x in range(width*height)]
    vertices = [i for i in range(width*height)]
    visited = [-1 for x in range(width*height)]
    # remove unreachable vertices
    # hazards = returnMap.returnHazards(map)
    # for hazard in hazards:
    #     if goal == hazard:
    #         return False
    #     val = mapToVertex(hazard, width)
    #     vertices.remove(val)

    # set initial distance to 0 (need conversion method)
    start_index = mapCoordinates.mapToVertex(start)
    dist[start_index] = 0

    while len(vertices) > 0:
        # set u as vertex with min distance
        u = min_index(vertices)

        # check for end condition
        coord = mapCoordinates.VertexToMap(u)
        if coord['x'] == goal['x'] and coord['y'] == goal['y']:
            path = []
            if (visited[u] or (coord['x'] == start['x'] and coord['y'] == start['y'])):
                while u is not -1:
                    [u] + path
                    u = visited[u]
            return path

        # remove u from vertices
        vertices.remove(u)

        neighbours = mapCoordinates.neighbours(u)
        for neighbour in neighbours:
            alt = dist[u] + 1
            if alt < dist[neighbour]:
                dist[neighbour] = alt
                visited[neighbour] = u

    return dist


def distance(start, goal):
    dist_x = abs(start['x'] - goal['x'])
    dist_y = abs(start['y'] - goal['y'])
    return dist_x + dist_y


def min_index(num_list):
    return num_list.index(min(num_list))
