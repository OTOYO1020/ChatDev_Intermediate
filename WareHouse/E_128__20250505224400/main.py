'''
Main application file for the Roadwork Distance Calculator.
'''
import sys
from distance_calculator import calculate_distances
def main():
    # Read integers N and Q from standard input
    N, Q = map(int, input("Enter the number of roadworks (N) and number of people (Q): ").split())
    roadworks = []
    # Collect roadwork data
    for _ in range(N):
        try:
            x, s, t = map(int, input("Enter X_i (coordinate), S_i (start time), T_i (end time): ").split())
            roadworks.append((x, s, t))
        except ValueError:
            print("Invalid input. Please enter integers.")
            sys.exit(1)
    people = []
    # Collect person data
    for _ in range(Q):
        try:
            d = int(input("Enter D_i (starting time): "))
            people.append(d)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            sys.exit(1)
    # Calculate distances
    distances = calculate_distances(roadworks, people)
    print("Distances:", ", ".join(map(str, distances)))
if __name__ == "__main__":
    main()