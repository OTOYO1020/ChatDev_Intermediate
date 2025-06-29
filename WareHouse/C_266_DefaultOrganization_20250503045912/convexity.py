'''
Module containing the function to check if a quadrilateral is convex.
'''
def is_convex(vertices):
    '''
    Determines if the quadrilateral formed by the given vertices is convex.
    Parameters:
    vertices (list): A list of tuples representing the vertices of the quadrilateral.
    Returns:
    str: 'YES' if the quadrilateral is convex, 'NO' otherwise.
    '''
    A, B, C, D = vertices
    AB = (B[0] - A[0], B[1] - A[1])
    BC = (C[0] - B[0], C[1] - B[1])
    CD = (D[0] - C[0], D[1] - C[1])
    DA = (A[0] - D[0], A[1] - D[1])
    cross1 = AB[0] * BC[1] - AB[1] * BC[0]
    cross2 = BC[0] * CD[1] - BC[1] * CD[0]
    cross3 = CD[0] * DA[1] - CD[1] * DA[0]
    cross4 = DA[0] * AB[1] - DA[1] * AB[0]
    # Check if all cross products are positive or all are negative
    if (cross1 > 0 and cross2 > 0 and cross3 > 0 and cross4 > 0) or \
       (cross1 < 0 and cross2 < 0 and cross3 < 0 and cross4 < 0):
        return 'YES'
    else:
        return 'NO'