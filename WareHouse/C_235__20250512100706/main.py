'''
Main application file for the occurrence finder.
'''
from occurrence_finder import find_kth_occurrence
def main():
    # Input reading
    while True:
        try:
            N = int(input("Enter the number of elements in the sequence: "))
            if N < 0:
                raise ValueError("N must be a non-negative integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    while True:
        A = input("Enter sequence (space-separated): ").split()
        try:
            if N > 0 and len(A) == 0:
                raise ValueError(f"The sequence cannot be empty when N is {N}.")
            A = list(map(int, A))
            if len(A) != N:
                raise ValueError(f"The number of elements must be {N}.")
            break
        except ValueError:
            print("Invalid input. Please enter integers only.")
    while True:
        try:
            Q = int(input("Enter the number of queries: "))
            if Q < 0:
                raise ValueError("Q must be a non-negative integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    queries = []
    for _ in range(Q):
        while True:
            try:
                x, k = map(int, input("Enter query (x k): ").split())
                if k <= 0:
                    raise ValueError("k must be a positive integer.")
                queries.append((x, k))
                break
            except ValueError:
                print("Invalid input. Please enter two integers for the query.")
    # Finding k-th occurrences
    results = find_kth_occurrence(N, A, Q, queries)
    # Display results
    print("Results:", results)
if __name__ == "__main__":
    main()