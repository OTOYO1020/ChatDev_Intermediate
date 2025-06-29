'''
Main application file for the black square counting application.
'''
from typing import List, Tuple
from grid import Grid
def count_black_squares(N: int, P: List[List[str]], queries: List[Tuple[int, int, int, int]]) -> List[int]:
    grid = Grid(N, P)
    return grid.handle_query(queries)
if __name__ == "__main__":
    N = int(input("Enter N (size of grid): "))
    P = [input(f"Enter row {i + 1} of the grid: ").strip().split() for i in range(N)]
    Q = int(input("Enter number of queries: "))
    queries = []
    for _ in range(Q):
        A, B, C, D = map(int, input("Enter query (A B C D): ").strip().split())
        queries.append((A, B, C, D))
    results = count_black_squares(N, P, queries)
    print("Results:", results)