'''
Main application file for the integer query application using standard input and output.
'''
from data_handler import DataHandler  # Ensure this line is present
def main():
    try:
        # Read integers N and Q from standard input
        input_line = input("Enter N and Q: ").strip()
        if not input_line:
            raise ValueError("Input for N and Q cannot be empty. Please enter two integers.")
        # Validate that exactly two integers are provided
        parts = input_line.split()
        if len(parts) != 2:
            raise ValueError("Please enter exactly two integers for N and Q.")
        N, Q = map(int, parts)
        # Validate that N and Q are positive integers
        if N <= 0 or Q <= 0:
            raise ValueError("Both N and Q must be positive integers.")
        # Prompt for the sequence of integers A
        print("Please enter the sequence of integers (length should be N):")
        int_sequence = list(map(int, input().strip().split()))
        if len(int_sequence) != N:
            raise ValueError(f"The length of the sequence must be {N}, but got {len(int_sequence)}.")
        # Check if there are enough queries
        queries = []
        for _ in range(Q):
            while True:  # Loop until valid input is received
                query_input = input("Enter query in the format 'x k' (where x is the integer to search for and k is the occurrence number): ").strip()
                if not query_input:
                    print("Query input cannot be empty. Please enter two integers.")
                    continue
                try:
                    x, k = map(int, query_input.split())
                    queries.append((x, k))
                    break  # Exit the loop if input is valid
                except ValueError:
                    print("Invalid input. Please enter two integers for x and k in the format 'x k'.")
        # Initialize DataHandler with the integer sequence
        data_handler = DataHandler(int_sequence)
        results = []
        # Process each query
        for x, k in queries:
            result = data_handler.get_kth_occurrence(x, k)
            results.append(result)
        # Print results for all queries
        for res in results:
            print(res)
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()