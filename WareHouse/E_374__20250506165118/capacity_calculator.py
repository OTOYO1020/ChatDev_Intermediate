'''
Module for calculating the maximum production capacity based on machine capacities and costs.
'''
def calculate_max_capacity(A, B, P, Q, X):
    max_capacity = 0  # Initialize to 0 for maximum capacity
    found_capacity = False  # Flag to check if any capacity was found
    for i in range(len(A)):
        for machines_S in range(X // P[i] + 1):
            remaining_budget = X - machines_S * P[i]
            if remaining_budget >= 0:
                machines_T = remaining_budget // Q[i] if Q[i] > 0 else 0
                W_i = A[i] * machines_S + B[i] * machines_T
                max_capacity = max(max_capacity, W_i)  # Update to find the maximum capacity
                found_capacity = True  # Set flag if capacity is found
    return max_capacity if found_capacity else 0  # Return max_capacity directly or 0 if no capacity was found