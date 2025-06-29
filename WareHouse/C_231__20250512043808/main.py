'''
Main application file for the Student Height Counter.
'''
import sys
from height_counter import count_students_with_min_height
def read_input():
    """
    Reads and validates input from standard input.
    Returns:
    tuple: A tuple containing the number of students, list of heights, number of queries, and list of queries.
    """
    N = int(sys.stdin.readline().strip())
    if N < 0:
        raise ValueError("Number of students cannot be negative.")
    heights = []
    if N > 0:
        heights_input = sys.stdin.readline().strip()
        heights = list(map(int, heights_input.split()))
        if len(heights) != N or any(h < 0 for h in heights):
            raise ValueError("Heights must match the number of students and cannot be negative.")
    Q = int(sys.stdin.readline().strip())
    if Q < 0:
        raise ValueError("Number of queries cannot be negative.")
    queries = []
    if Q > 0:
        queries_input = sys.stdin.readline().strip()
        queries = list(map(int, queries_input.split()))
        if len(queries) != Q or any(q < 0 for q in queries):
            raise ValueError("Queries must match the number of queries and cannot be negative.")
    return N, heights, Q, queries
def main():
    try:
        N, heights, Q, queries = read_input()
        results = count_students_with_min_height(heights, queries)
        for result in results:
            print(result)
    except ValueError as e:
        print(f"Input error: {e}")
if __name__ == "__main__":
    main()