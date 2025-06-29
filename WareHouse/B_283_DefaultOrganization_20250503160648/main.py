'''
Main application file for managing a sequence of integers through standard input and output.
'''
from sequence_manager import SequenceManager
def main():
    # Read the integer N and the sequence A
    try:
        N = int(input())
        if N <= 0:
            print("Error: N must be greater than 0.")
            return
    except ValueError:
        print("Error: Invalid input for N.")
        return
    # Read the sequence and validate its length
    sequence_input = input().strip()
    sequence = list(map(int, sequence_input.split()))
    if len(sequence) != N:
        print(f"Error: Expected sequence length of {N}, but got {len(sequence)}.")
        return
    # Initialize the SequenceManager with the sequence
    sequence_manager = SequenceManager()
    sequence_manager.set_sequence(sequence, N)
    # Read the integer Q representing the number of queries
    try:
        Q = int(input())
        if Q <= 0:
            print("Error: Q must be greater than 0.")
            return
    except ValueError:
        print("Error: Invalid input for Q.")
        return
    results = []
    # Loop through Q queries
    for _ in range(Q):
        query = list(map(int, input().strip().split()))
        if len(query) < 2:
            print("Error: Invalid query format.")
            continue
        query_type = query[0]
        if query_type == 1 and len(query) == 3:
            # Update value
            k, x = query[1], query[2]
            try:
                sequence_manager.update_value(k, x)
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")
        elif query_type == 2 and len(query) == 2:
            # Print value
            k = query[1]
            try:
                result = sequence_manager.print_value(k)
                if result is not None:  # Only append if result is valid
                    results.append(result)
            except (ValueError, IndexError) as e:
                print(f"Error: {e}")
        else:
            print("Error: Invalid query type or parameters. Please enter a valid query.")
    # Print all results for type '2' queries
    for res in results:
        print(res)
if __name__ == "__main__":
    main()