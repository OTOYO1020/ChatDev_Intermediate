'''
Module containing logic for checking lattice points.
'''
def is_lattice_point(x, y):
    '''
    Checks if the point (x, y) is a lattice point (both coordinates are integers).
    '''
    return isinstance(x, int) and isinstance(y, int) or (isinstance(x, float) and x.is_integer() and isinstance(y, float) and y.is_integer())
def is_distance_sqrt5(x1, y1, x2, y2):
    '''
    Checks if the distance between points (x1, y1) and (x2, y2) is sqrt(5).
    '''
    return (x2 - x1) ** 2 + (y2 - y1) ** 2 == 5
def find_lattice_points(x1, y1, x2, y2):
    '''
    Finds lattice points that are sqrt(5) units away from (x1, y1) and (x2, y2).
    '''
    candidates = [
        (x1 + 2, y1 + 1), (x1 + 2, y1 - 1), (x1 - 2, y1 + 1), (x1 - 2, y1 - 1),
        (x1 + 1, y1 + 2), (x1 + 1, y1 - 2), (x1 - 1, y1 + 2), (x1 - 1, y1 - 2)
    ]
    for (x, y) in candidates:
        # Check if the candidate point is a lattice point and satisfies the distance condition
        if is_lattice_point(x, y) and is_distance_sqrt5(x, y, x2, y2):
            return True
    return False