'''
Main entry point for the city traversal application.
'''
from city_graph import CityGraph
from typing import List, Tuple
def main():
    # Example input for testing
    N = 5
    roads = [(1, 2), (2, 3), (3, 4), (4, 5)]
    graph = CityGraph(N, roads)
    result = graph.find_visited_cities()
    print(result)
if __name__ == "__main__":
    main()