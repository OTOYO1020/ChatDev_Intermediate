'''
Main application file for determining if a quadrilateral is convex using standard input and output.
'''
from convexity import is_convex_quadrilateral, is_collinear
def get_coordinates():
    # Input handling for coordinates with range validation
    A_x, A_y = map(int, input("Enter coordinates for A (A_x A_y): ").split())
    B_x, B_y = map(int, input("Enter coordinates for B (B_x B_y): ").split())
    C_x, C_y = map(int, input("Enter coordinates for C (C_x C_y): ").split())
    D_x, D_y = map(int, input("Enter coordinates for D (D_x D_y): ").split())
    # Check for integer range
    for x, y in [(A_x, A_y), (B_x, B_y), (C_x, C_y), (D_x, D_y)]:
        if not (-10**6 <= x <= 10**6 and -10**6 <= y <= 10**6):
            raise ValueError("Coordinates must be integers within the range of -10^6 to 10^6.")
    # Check for unique vertices
    if len({(A_x, A_y), (B_x, B_y), (C_x, C_y), (D_x, D_y)}) < 4:
        raise ValueError("Vertices must be unique.")
    return A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y
def main():
    try:
        A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y = get_coordinates()
        # Check for collinearity among all combinations of three points
        if is_collinear(A_x, A_y, B_x, B_y, C_x, C_y) or \
           is_collinear(A_x, A_y, B_x, B_y, D_x, D_y) or \
           is_collinear(A_x, A_y, C_x, C_y, D_x, D_y) or \
           is_collinear(B_x, B_y, C_x, C_y, D_x, D_y):
            raise ValueError("No three vertices can be collinear to form a valid quadrilateral.")
        # Check for convexity
        if is_convex_quadrilateral(A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y):
            print("Yes, the quadrilateral is convex.")
        else:
            print("No, the quadrilateral is not convex.")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
if __name__ == "__main__":
    main()