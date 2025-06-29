'''
Module for checking visibility of coordinates.
'''
class VisibilityChecker:
    def __init__(self, coordinates):
        self.coordinates = coordinates  # Store the coordinates for visibility checks
    def is_visible(self, origin, coord):
        # Check if the coordinate is visible from the origin
        quadrilateral = self.calculate_quadrilateral(origin, coord)
        # Check if the quadrilateral is valid (not degenerate)
        if self.is_degenerate(quadrilateral):
            return False  # Not visible if the quadrilateral is degenerate
        # Check if the origin is inside the quadrilateral
        if self.point_in_polygon(origin, quadrilateral):
            return False  # Not visible if the origin is inside the quadrilateral
        # Check for intersections with all other coordinates
        for other_coord in self.coordinates:
            if other_coord != coord:  # Don't check against itself
                other_quadrilateral = self.calculate_quadrilateral(origin, other_coord)
                # Check if the quadrilateral intersects with the other quadrilateral
                if self.check_quadrilateral_intersection(quadrilateral, other_quadrilateral):
                    return False  # Not visible if there's an intersection
        return True  # The coordinate is visible if no intersections were found
    def calculate_quadrilateral(self, origin, coord):
        x, y = coord
        return [
            origin,
            (x - 1, y),
            (x, y),
            (x, y - 1)
        ]
    def check_quadrilateral_intersection(self, quad1, quad2):
        # Check if two quadrilaterals intersect
        for i in range(len(quad1)):
            p1 = quad1[i]
            p2 = quad1[(i + 1) % len(quad1)]
            for j in range(len(quad2)):
                p3 = quad2[j]
                p4 = quad2[(j + 1) % len(quad2)]
                if self.segments_intersect(p1, p2, p3, p4):
                    return True
        return False
    def segments_intersect(self, p1, p2, p3, p4):
        # Check if line segments p1p2 and p3p4 intersect
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0  # collinear
            return 1 if val > 0 else 2  # clock or counterclockwise
        def on_segment(p, q, r):
            return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
                    min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))
        o1 = orientation(p1, p2, p3)
        o2 = orientation(p1, p2, p4)
        o3 = orientation(p3, p4, p1)
        o4 = orientation(p3, p4, p2)
        # General case
        if o1 != o2 and o3 != o4:
            return True
        # Special Cases
        if o1 == 0 and on_segment(p1, p3, p2):
            return True
        if o2 == 0 and on_segment(p1, p4, p2):
            return True
        if o3 == 0 and on_segment(p3, p1, p4):
            return True
        if o4 == 0 and on_segment(p3, p2, p4):
            return True
        return False  # Doesn't intersect
    def point_in_polygon(self, point, polygon):
        # Ray-casting algorithm to determine if the point is in the polygon
        x, y = point
        n = len(polygon)
        inside = False
        p1x, p1y = polygon[0]
        for i in range(n + 1):
            p2x, p2y = polygon[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside
    def is_degenerate(self, quadrilateral):
        # Check if the quadrilateral is degenerate (all points are collinear)
        def area(p1, p2, p3):
            return abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2.0
        return area(quadrilateral[0], quadrilateral[1], quadrilateral[2]) == 0 or \
               area(quadrilateral[0], quadrilateral[2], quadrilateral[3]) == 0
    def are_adjacent(self, coord1, coord2):
        # Check if two coordinates are adjacent (horizontally or vertically)
        x1, y1 = coord1
        x2, y2 = coord2
        return (abs(x1 - x2) == 1 and y1 == y2) or (abs(y1 - y2) == 1 and x1 == x2)