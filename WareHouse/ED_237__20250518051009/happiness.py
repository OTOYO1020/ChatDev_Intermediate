'''
Contains the function to calculate maximum happiness.
'''
from graph import Graph  # Ensure the Graph class is imported
def max_happiness(N: int, M: int, H: list[int], slopes: list[tuple[int, int]]) -> int:
    graph = Graph(N, H, slopes)  # Create a Graph instance
    return graph.max_happiness()  # Call the max_happiness method from the Graph instance