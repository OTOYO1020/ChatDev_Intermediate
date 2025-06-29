'''
Contains functions for calculating Manhattan distance and counting lattice points.
'''
from itertools import product
def manhattan_distance(point_a, point_b):
    '''Calculates the Manhattan distance between two points in N-dimensional space.'''
    return sum(abs(a - b) for a, b in zip(point_a, point_b))
def is_lattice_point(point):
    '''Checks if a given point is a lattice point (all components are integers).'''
    return all(isinstance(coord, int) for coord in point)
def count_lattice_points(p, q, D):
    '''Counts the number of lattice points r satisfying d(p, r) <= D and d(q, r) <= D.'''
    count = 0
    # Generate lattice points within the bounding box defined by Manhattan distances
    for r in generate_lattice_points(p, q, D):
        if manhattan_distance(p, r) <= D and manhattan_distance(q, r) <= D:
            count += 1
    return count % 998244353
def generate_lattice_points(p, q, D):
    '''Generates all possible lattice points within the bounding box defined by p and q.'''
    # Calculate the bounding box
    min_point = [min(p[i], q[i]) - D for i in range(len(p))]
    max_point = [max(p[i], q[i]) + D for i in range(len(p))]
    # Generate all possible lattice points within the bounding box
    lattice_points = []
    for coords in product(*(range(min_point[i], max_point[i] + 1) for i in range(len(p)))):
        if is_lattice_point(coords):
            lattice_points.append(coords)
    return lattice_points