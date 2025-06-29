'''
Main application file for the point transformation checker.
'''
import sys
from transform import canTransform
def main():
    try:
        # Read input from standard input
        input_data = sys.stdin.read().strip().splitlines()
        s_points = parse_input(input_data[0])
        t_points = parse_input(input_data[1])
        result = canTransform(s_points, t_points)
        print("YES" if result else "NO")
    except Exception as e:
        print(f"Error: {str(e)}")
def parse_input(input_str):
    points = input_str.split()
    return [tuple(map(int, point.strip('()').split(','))) for point in points]
if __name__ == "__main__":
    main()