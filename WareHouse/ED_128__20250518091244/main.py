'''
Main application file for the Distance Calculator.
'''
from distance_calculator import calculate_distances
def main():
    # Read the number of roadworks and people
    N, Q = map(int, input("Enter number of roadworks and people (N Q): ").split())
    # Read roadworks data
    roadworks = []
    for _ in range(N):
        X, S, T = map(int, input("Enter roadwork (X, S, T): ").split())
        roadworks.append((X, S, T))
    # Read people data
    people = []
    for i in range(Q):
        D = int(input(f"Enter starting time for person {i + 1} (D): "))
        people.append((D, i))
    # Calculate distances
    distances = calculate_distances(N, Q, roadworks, people)
    # Print results
    print("Distances:", ' '.join(map(str, distances)))
if __name__ == "__main__":
    main()