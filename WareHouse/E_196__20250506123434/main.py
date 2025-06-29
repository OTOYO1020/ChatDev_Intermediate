'''
Main application file for the sequence processing.
'''
from logic import f
def validate_integer_input(input_list, expected_length):
    if len(input_list) != expected_length:
        raise ValueError(f"Expected {expected_length} integers, but got {len(input_list)}.")
    if any(not i.isdigit() for i in input_list):
        raise ValueError("All inputs must be integers.")
    return list(map(int, input_list))
def main():
    # Read integers N and Q from standard input
    try:
        N, Q = map(int, input("Enter two integers N (length of sequences A and T) and Q (length of sequence X) separated by space: ").split())
    except ValueError:
        print("Error: Please enter two valid integers for N and Q.")
        return
    # Read the sequence A of length N from standard input
    A_input = input(f"Enter {N} integers for sequence A (space-separated): ").split()
    try:
        A = validate_integer_input(A_input, N)
    except ValueError as e:
        print(f"Error: {e}. Please try again.")
        return
    # Read the sequence T of length N from standard input
    T_input = input(f"Enter {N} integers for sequence T (space-separated): ").split()
    try:
        T = validate_integer_input(T_input, N)
    except ValueError as e:
        print(f"Error: {e}. Please try again.")
        return
    # Validate the contents of sequence T
    if any(not isinstance(t, int) or t not in {1, 2, 3} for t in T):
        print("Error: Sequence T must only contain integer values 1, 2, or 3.")
        return
    # Read the sequence X of length Q from standard input
    X_input = input(f"Enter {Q} integers for sequence X (space-separated): ").split()
    try:
        X = validate_integer_input(X_input, Q)
    except ValueError as e:
        print(f"Error: {e}. Please try again.")
        return
    results = []
    # Process each x_i in X
    for x in X:
        result = x
        for i in range(N):
            try:
                result = f(result, A[i], T[i])
            except ValueError as e:
                print(f"Error processing f({result}, {A[i]}, {T[i]}): {e}. Ensure T[i] is 1, 2, or 3.")
                result = None  # Set result to None to indicate failure
                break  # Exit the loop for this x if an error occurs
        if result is not None:
            results.append(result)  # Only append if result is valid
        else:
            results.append(f"Error processing x={x}")  # Append a more informative error message
    # Print the results for all x_i in sequence
    print("Results:", ' '.join(map(str, results)))
if __name__ == "__main__":
    main()