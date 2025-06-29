'''
Main application file for calculating minimum travel time between cities.
'''
import sys
from dijkstra import minimum_travel_time
def main():
    try:
        N = int(input("Enter number of cities (N): "))
        A = int(input("Enter A (car speed factor): "))
        B = int(input("Enter B (train speed factor): "))
        C = int(input("Enter C (not used in current logic): "))
        D = []
        print("Enter distance matrix (comma-separated rows, end with an empty line):")
        while True:
            line = input()
            if line == "":
                break
            D.append(list(map(int, line.split(','))))
        min_time = minimum_travel_time(N, A, B, C, D)
        print(f"Minimum Travel Time: {min_time}")
    except Exception as e:
        print(f"Input Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()