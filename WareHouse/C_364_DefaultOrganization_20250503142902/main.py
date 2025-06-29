'''
Main application file for the dish calculator.
'''
def calculate_dishes(N, X, Y, A, B):
    """
    Calculate the minimum number of dishes that can be eaten without exceeding
    the sweetness and saltiness limits.
    Parameters:
    N (int): Number of dishes.
    X (int): Sweetness limit.
    Y (int): Saltiness limit.
    A (list): List of sweetness values.
    B (list): List of saltiness values.
    Returns:
    int: Minimum number of dishes eaten.
    """
    dishes = list(zip(A, B))
    # Sort by a custom heuristic that considers both sweetness and saltiness
    dishes.sort(key=lambda dish: (dish[0] / (X + 1), dish[1] / (Y + 1)))  # Normalize by limits to prioritize dishes
    total_sweetness = 0
    total_saltiness = 0
    count = 0
    for sweetness, saltiness in dishes:
        if total_sweetness + sweetness > X or total_saltiness + saltiness > Y:
            break
        total_sweetness += sweetness
        total_saltiness += saltiness
        count += 1
    return count
def get_input():
    """
    Get user input for the number of dishes, sweetness limit, saltiness limit,
    and the sweetness and saltiness values.
    Returns:
    tuple: A tuple containing N, X, Y, A, and B.
    """
    while True:
        try:
            N = int(input("Enter the number of dishes (N): "))
            X = int(input("Enter the sweetness limit (X): "))
            Y = int(input("Enter the saltiness limit (Y): "))
            A = list(map(int, input("Enter sweetness values (comma-separated): ").split(',')))
            B = list(map(int, input("Enter saltiness values (comma-separated): ").split(',')))
            if len(A) != N or len(B) != N:
                print("Error: Length of A and B must match N.")
                continue
            return N, X, Y, A, B
        except ValueError:
            print("Error: Please enter valid integers for N, X, Y, and the sweetness and saltiness values.")
if __name__ == "__main__":
    N, X, Y, A, B = get_input()
    result = calculate_dishes(N, X, Y, A, B)
    print(result)