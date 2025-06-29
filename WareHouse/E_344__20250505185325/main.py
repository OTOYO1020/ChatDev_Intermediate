'''
Main entry point of the application that handles user interactions through standard input and output.
'''
from sequence_manager import SequenceManager
from query import Query
def main():
    # Read N and Q from standard input
    N, Q = map(int, input().split())
    # Read the sequence A from standard input
    A = list(map(int, input().split()))
    sequence_manager = SequenceManager(A)
    # Process each query
    for _ in range(Q):
        query = list(map(int, input().split()))
        query_type = query[0]
        if query_type == 1:
            x, y = query[1], query[2]
            try:
                sequence_manager.insert_after(x, y)
            except ValueError as e:
                print(e)  # Log the error but continue processing
                continue
        elif query_type == 2:
            x = query[1]
            try:
                sequence_manager.remove(x)
            except ValueError as e:
                print(e)  # Log the error but continue processing
                continue
    # Final check for sequence state
    final_sequence = sequence_manager.get_sequence()
    if not final_sequence:
        print("Warning: The sequence is empty after processing all queries.")
    elif len(final_sequence) != len(set(final_sequence)):
        print("Warning: The sequence contains duplicates.")
    else:
        print(final_sequence)
if __name__ == "__main__":
    main()