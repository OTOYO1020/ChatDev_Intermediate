'''
Main application file for the Line Counter.
'''
from line_counter import count_lines
def main():
    points_str = input("Enter points (x1,y1 x2,y2 ...): ")
    k_str = input("Enter minimum points (K): ")
    try:
        points = [tuple(map(int, point.split(','))) for point in points_str.split()]
        k = int(k_str)
        if k > len(points):
            raise ValueError("K cannot be greater than the number of points.")
        result = count_lines(len(points), k, points)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()