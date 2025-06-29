'''
Module to provide coordinates for vertices of a regular pentagon based on character input.
'''
def get_coordinates(vertex):
    '''
    Returns the coordinates of the vertex based on the character input.
    Raises a ValueError if the vertex is not valid.
    '''
    coordinates = {
        'A': (1, 0),
        'B': (0.309, 0.951),
        'C': (-0.809, 0.588),
        'D': (-0.809, -0.588),
        'E': (0.309, -0.951)
    }
    if vertex not in coordinates:
        raise ValueError(f"Invalid vertex '{vertex}'. Must be one of {list(coordinates.keys())}.")
    return coordinates[vertex]