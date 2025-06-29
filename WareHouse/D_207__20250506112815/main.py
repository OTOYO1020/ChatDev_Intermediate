'''
Main application file to run the point transformation application.
'''
import re
from transformations import transform_and_compare
def main():
    N = int(input("Enter the number of points in sets S and T: "))
    S = []
    T = []
    for i in range(N):
        while True:
            try:
                points_s = input(f"Enter coordinates for point {i + 1} in set S (format: x,y): ")
                if not re.match(r"^-?\d+(\.\d+)?,-?\d+(\.\d+)?$", points_s):
                    raise ValueError("Coordinates must be in the format x,y where x and y are numbers.")
                S.append(tuple(map(float, points_s.split(','))))
                break
            except ValueError as e:
                print(f"Invalid input. {e}")
        while True:
            try:
                points_t = input(f"Enter coordinates for point {i + 1} in set T (format: x,y): ")
                if not re.match(r"^-?\d+(\.\d+)?,-?\d+(\.\d+)?$", points_t):
                    raise ValueError("Coordinates must be in the format x,y where x and y are numbers.")
                T.append(tuple(map(float, points_t.split(','))))
                break
            except ValueError as e:
                print(f"Invalid input. {e}")
    result = transform_and_compare(S, T)
    print("YES" if result else "NO")
if __name__ == "__main__":
    main()