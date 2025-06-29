'''
Main entry point of the application that manages the application flow.
'''
import sys
from query_handler import QueryHandler
from utilities import validate_input
def main():
    # Read integers N and K from standard input
    n, k = map(int, sys.stdin.readline().strip().split())
    validate_input(n, k)
    query_handler = QueryHandler(n, k)
    result = query_handler.execute_queries()
    # Print the result in the required format
    print(f"! {' '.join(map(str, result))}")
    sys.stdout.flush()
if __name__ == "__main__":
    main()