'''
Main entry point for the City Connections application.
'''
from city_graph import CityGraph
def main():
    # Read number of cities and roads from standard input
    N, M = map(int, input().split())
    # Validate N and M to ensure they are positive integers
    if N <= 0 or M < 0:
        print("Number of cities must be a positive integer and number of roads must be a non-negative integer.")
        return
    graph = CityGraph(N)
    # Read each road and add to the graph
    for _ in range(M):
        city_a, city_b = map(int, input().split())
        try:
            graph.add_road(city_a, city_b)
        except ValueError as e:
            print(e)  # Print error message for invalid city indices
    # Get and print the connections
    results = graph.get_connections()
    for result in results:
        print(result)
if __name__ == "__main__":
    main()