'''
Main application file for counting elements in a list based on user queries.
'''
from count_elements import count_elements
def main():
    try:
        # Input for the number of elements in the list
        while True:
            try:
                N = int(input("Enter the number of elements in the list (N): "))
                if N <= 0:
                    raise ValueError("N must be a positive integer.")
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer for N.")
        # Input for the list of integers
        while True:
            try:
                A = list(map(int, input(f"Enter {N} integers (space-separated): ").strip().split()))
                if len(A) == N:
                    break
                else:
                    print(f"Please enter exactly {N} integers. You entered {len(A)} integers.")
            except ValueError as ve:
                print("Invalid input. Please enter integers only. Error: ", ve)
        # Input for the number of queries
        while True:
            try:
                Q = int(input("Enter the number of queries (Q): "))
                if Q <= 0:
                    raise ValueError("Q must be a positive integer.")
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer for Q.")
        queries = []
        for _ in range(Q):
            while True:
                query_input = input("Enter L, R, X (space-separated): ")
                try:
                    L, R, X = map(int, query_input.split())
                    # Validate the input constraints
                    if not (1 <= L <= R <= N):
                        raise ValueError("Input values for L and R are out of bounds.")
                    if X not in A:  # Ensure X is an element in the list A
                        raise ValueError(f"X must be an element in the list A. You entered: {X}")
                    queries.append((L, R, X))
                    break  # Exit the loop if input is valid
                except ValueError:
                    print("Invalid input. Please enter three integers L, R, and X.")
        # Count elements
        results = count_elements(A, queries)
        # Output results
        for result in results:
            print(result)
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()