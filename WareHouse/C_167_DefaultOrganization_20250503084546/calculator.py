'''
Module containing the function to calculate the result based on input data.
'''
def calculate_result(N, M, X, C, A):
    # Initialize result counter
    result = 0
    # Iterate through each row of A
    for i in range(N):
        # Calculate the weighted sum of the current row
        row_sum = sum(A[i][j] * C[j] for j in range(M))
        # Check if the weighted sum meets or exceeds X
        if row_sum >= X:  # Updated to include equality
            result += 1  # Increment result if condition is met
    return result