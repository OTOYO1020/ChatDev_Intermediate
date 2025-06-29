'''
Main application file for the travel time calculator using Dijkstra's algorithm.
'''
import math
import heapq
import sys
from dijkstra import DijkstraAlgorithm
def main():
    # Read integers N, A, B, and C from standard input
    N, A, B, C = map(int, input("Enter N, A, B, C: ").split())
    # Initialize a 2D array 'D' of size N x N to store the travel times between cities
    D = []
    print(f"Enter the travel times matrix (size {N}x{N}):")
    for _ in range(N):
        row = list(map(int, input().split()))
        if len(row) != N:
            raise ValueError(f"Each row must have exactly {N} entries.")
        D.append(row)
    # Initialize Dijkstra's algorithm and find the minimum time
    dijkstra = DijkstraAlgorithm(N, A, B, C, D)
    min_time = dijkstra.find_shortest_path()
    # Print the minimum time from city 1 to city N
    print(f"Minimum time from city 1 to city {N}: {min_time}")
if __name__ == "__main__":
    main()