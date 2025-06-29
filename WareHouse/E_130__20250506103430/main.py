'''
Main application file for the subsequence counter.
'''
from utils import count_subsequences, calculate_total_pairs
def main():
    # Read integers N and M
    try:
        N, M = map(int, input().split())
        # Read sequences S and T
        sequence_S = list(map(int, input().split()))
        sequence_T = list(map(int, input().split()))
        # Validate the lengths of the sequences
        if len(sequence_S) != N or len(sequence_T) != M:
            raise ValueError("The lengths of the sequences do not match the specified N and M.")
        # Check for empty sequences
        if N == 0 or M == 0:
            print(0)
            return
    except ValueError as e:
        print(f"Input error: {e}")
        return
    # Count subsequences
    subseq_count_S = count_subsequences(sequence_S)
    subseq_count_T = count_subsequences(sequence_T)
    # Calculate total pairs
    total_pairs = calculate_total_pairs(subseq_count_S, subseq_count_T)
    # Print the result
    print(total_pairs)
if __name__ == "__main__":
    main()