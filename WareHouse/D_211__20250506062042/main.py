'''
Main application file to run the city graph shortest path application.
'''
from city_graph import CityGraph
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    # Validate input length
    if len(data) < 2:
        print("Invalid input: Not enough data provided.")
        return
    try:
        N = int(data[0])  # Number of cities
        M = int(data[1])  # Number of roads
    except ValueError:
        print("Invalid input: N and M must be integers.")
        return
    # Check for the case where there are no roads
    if M < 0 or N <= 0:
        print("Invalid input: Number of cities and roads must be positive.")
        return
    # Check if M exceeds the maximum possible roads in a simple undirected graph
    max_roads = N * (N - 1) // 2
    if M > max_roads:
        print(f"Invalid input: Number of roads cannot exceed {max_roads}.")
        return
    if M == 0:
        print(0 if N > 1 else 1)  # If there are no roads and more than one city, no path exists.
        return
    graph = CityGraph(N)
    for i in range(2, 2 + M):
        if i >= len(data):
            print(f"Invalid input: Expected {M} roads but got less.")
            return
        try:
            A, B = map(int, data[i].split())
            if A < 1 or A > N or B < 1 or B > N:
                print(f"Invalid road: Cities {A} and {B} must be between 1 and {N}.")
                return
            if not graph.add_road(A, B):
                print(f"Invalid road: Road between cities {A} and {B} could not be added.")
                return
        except ValueError:
            print(f"Invalid input: Road data must be two integers on line {i + 1}.")
            return
    # After reading roads, validate if we have read exactly M roads
    if len(data) < 2 + M:
        print(f"Invalid input: Expected {M} roads but got less.")
        return
    result = graph.find_shortest_paths()
    print(result)
if __name__ == "__main__":
    main()