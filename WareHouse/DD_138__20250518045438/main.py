'''
Main application file to run the increment counters application.
'''
from typing import List, Tuple
from tree import Tree
def increment_counters(N: int, edges: List[Tuple[int, int]], Q: int, operations: List[Tuple[int, int]]) -> List[int]:
    tree = Tree(N, edges)
    for node, increment in operations:
        tree.increment_counters(node, increment)
    tree.apply_lazy()  # Apply lazy propagation after all operations
    return tree.get_final_counters()
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip().splitlines()
    N = int(input_data[0])
    edges_input = input_data[1].strip().split(';')  # Assuming edges are separated by semicolons
    edges = [tuple(map(int, edge.split(','))) for edge in edges_input]
    Q = int(input_data[2])  # Adjusted index for Q
    operations_input = input_data[3:3 + Q]  # Adjusted to read operations correctly
    operations = [tuple(map(int, line.split(','))) for line in operations_input]
    result = increment_counters(N, edges, Q, operations)
    print(result)