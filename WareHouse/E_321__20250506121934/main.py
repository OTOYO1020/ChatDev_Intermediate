'''
Main application file for the distance calculator.
'''
import sys
from tree_distance_calculator import TreeDistanceCalculator
def main():
    input = sys.stdin.read
    data = input().splitlines()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N, X, K = map(int, data[i].split())
        calculator = TreeDistanceCalculator(N, X, K)
        count = calculator.count_vertices_at_distance()
        results.append(count)
    for result in results:
        print(result)
if __name__ == "__main__":
    main()