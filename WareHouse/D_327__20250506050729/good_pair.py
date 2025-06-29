'''
Module containing the logic to check if sequences form a good pair.
'''
def is_good_pair(N, M, A, B):
    X = [-1] * N  # Initialize array X with -1
    for i in range(M):
        a_index = A[i] - 1
        b_index = B[i] - 1
        # Check if both indices are assigned
        if X[a_index] != -1 and X[b_index] != -1:
            if X[a_index] == X[b_index]:  # They cannot be the same
                return "No"
        elif X[a_index] == -1 and X[b_index] == -1:
            X[a_index] = 0
            X[b_index] = 1
        elif X[a_index] == -1 and X[b_index] != -1:  # If A is unassigned but B is assigned
            X[a_index] = 1 - X[b_index]  # Assign opposite of B
        elif X[b_index] == -1 and X[a_index] != -1:  # If B is unassigned but A is assigned
            X[b_index] = 1 - X[a_index]  # Assign opposite of A
    # Final check to ensure all pairs satisfy the condition
    for i in range(M):
        if X[A[i] - 1] == X[B[i] - 1]:  # If they are the same
            return "No"
    return "Yes"