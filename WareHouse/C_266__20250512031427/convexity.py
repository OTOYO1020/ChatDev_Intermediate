'''
Module to determine if a quadrilateral is convex based on its vertices.
'''
def is_convex_quadrilateral(A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y):
    def cross_product(v1, v2):
        return v1[0] * v2[1] - v1[1] * v2[0]
    # Vectors AB, BC, CD, DA
    AB = (B_x - A_x, B_y - A_y)
    BC = (C_x - B_x, C_y - B_y)
    CD = (D_x - C_x, D_y - C_y)
    DA = (A_x - D_x, A_y - D_y)
    # Cross products
    cross1 = cross_product(AB, BC)
    cross2 = cross_product(BC, CD)
    cross3 = cross_product(CD, DA)
    cross4 = cross_product(DA, AB)
    # Check if all cross products have the same sign
    return (cross1 > 0 and cross2 > 0 and cross3 > 0 and cross4 > 0) or \
           (cross1 < 0 and cross2 < 0 and cross3 < 0 and cross4 < 0)
def is_collinear(x1, y1, x2, y2, x3, y3):
    # Check if the area of the triangle formed by the points is zero
    # Calculate the area of the triangle formed by the points
    area = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    return area == 0  # True if collinear, False otherwise