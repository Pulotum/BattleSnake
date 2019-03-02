def returnHazards(map):

    hazards = []

    for x_index, x in enumerate(map):
        for y_index, y in enumerate(x):
            if y == 'x':
                hazards.append({"x":x_index,"y":y_index})
    
    return hazards