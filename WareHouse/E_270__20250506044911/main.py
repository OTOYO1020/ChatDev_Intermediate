'''
Main application file for the apple eating simulation.
'''
def eat_apples(N, K, A):
    """
    Simulates eating apples from baskets.
    Parameters:
    N (int): The number of baskets.
    K (int): The number of apples to eat.
    A (list): The list containing the number of apples in each basket.
    Returns:
    list: The updated list of apples remaining in each basket.
    """
    total_eaten = 0
    current_basket = 0
    while total_eaten < K:
        if A[current_basket] > 0:
            A[current_basket] -= 1
            total_eaten += 1
        current_basket = (current_basket + 1) % N
        # Check if all baskets are empty
        if all(apples == 0 for apples in A):
            break  # Exit the loop if no apples are left to eat
    return A
if __name__ == "__main__":
    # Read input values
    N = int(input())
    if N <= 0:
        print("Error: The number of baskets must be greater than 0. Please enter a valid number.")
        exit(1)  # Exit the program if there are no baskets
    K = int(input())
    if K < 0:
        print("Error: The number of apples to eat must be non-negative.")
        exit(1)  # Exit the program if K is negative
    A = list(map(int, input().split()))
    if len(A) != N:
        print("Error: The number of apples must match the number of baskets.")
        exit(1)  # Exit the program if the number of apples does not match the number of baskets
    else:
        total_apples = sum(A)  # Calculate total apples in all baskets
        if K > total_apples:
            print(f"Adjusted K from {K} to {total_apples} as it exceeds the total number of apples.")
            K = total_apples
        remaining_apples = eat_apples(N, K, A)
        print(" ".join(map(str, remaining_apples)))