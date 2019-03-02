def returnHazards(map):

    hazards = []

    for x in map:
        for y in map:
            if y == 'x':
                hazards.append({"x":x,"y":y})
    
    return hazards