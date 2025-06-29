'''
Main entry point for the ABC Query application.
'''
from abc_query import process_queries
import sys
from typing import List, Tuple
def main():
    input_string = sys.stdin.readline().strip()  # Read the input string
    queries_count = int(sys.stdin.readline().strip())  # Read the number of queries
    queries = []
    for _ in range(queries_count):
        query = sys.stdin.readline().strip().split()
        index = int(query[0])
        char = query[1]
        queries.append((index, char))
    results = process_queries(input_string, queries)
    print(results)
if __name__ == "__main__":
    main()