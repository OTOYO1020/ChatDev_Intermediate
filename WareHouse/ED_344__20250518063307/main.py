'''
Main application file for managing a list of distinct integers without a GUI.
'''
from query_handler import process_queries
def main():
    # Sample input for testing
    N = 5
    A = [1, 2, 3, 4, 5]  # Initialize with distinct integers
    Q = 3  # Number of queries
    queries = [
        (1, 3, 6),  # Insert 6 after 3
        (2, 2),     # Remove 2
        (1, 4, 7)   # Insert 7 after 4
    ]
    final_list = process_queries(N, A, Q, queries)
    print("Final List:", final_list)
if __name__ == "__main__":
    main()