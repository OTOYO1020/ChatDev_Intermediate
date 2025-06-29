'''
Main application file to calculate maximum sum based on user inputs.
'''
def calculate_max_sum(A, B, C, K):
    '''
    Calculate the maximum possible sum based on the number of cards picked from each type.
    Parameters:
    A (int): Number of cards with value 1.
    B (int): Number of cards with value 0.
    C (int): Number of cards with value -1.
    K (int): Total number of cards to pick.
    Returns:
    int: The maximum sum calculated based on the cards picked.
    '''
    # Initialize max_sum
    max_sum = 0
    # Determine how many cards to pick from A (value 1)
    pick_from_A = min(A, K)
    remaining_K = K - pick_from_A
    # Determine how many cards to pick from B (value 0)
    pick_from_B = min(B, remaining_K)
    remaining_K -= pick_from_B
    # Determine how many cards to pick from C (value -1)
    pick_from_C = min(C, remaining_K)
    # Calculate the maximum sum
    max_sum = (pick_from_A * 1) + (pick_from_B * 0) + (pick_from_C * -1)
    return max_sum
if __name__ == "__main__":
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    C = int(input("Enter C: "))
    K = int(input("Enter K: "))
    result = calculate_max_sum(A, B, C, K)
    print(f"Max Sum: {result}")