'''
Main file to run the Binary String Application.
'''
from query_processor import process_queries
def main():
    binary_string = input("Enter binary string (only 0s and 1s): ")
    if not binary_string:  # Check for empty input
        print("Error: The binary string cannot be empty.")
        return
    if not all(c in '01' for c in binary_string):  # Validate binary string
        print("Error: The binary string must consist only of '0's and '1's.")
        return
    queries_input = input("Enter queries (format: c L R, separated by semicolons): ")
    # Parse queries
    queries = []
    for query in queries_input.split(';'):
        parts = query.split()
        if len(parts) == 3:
            c, L, R = map(int, parts)
            queries.append((c, L, R))
    try:
        results = process_queries(binary_string, queries)
        print("Results:", results)
    except Exception as e:
        print("Error:", str(e))
if __name__ == "__main__":
    main()