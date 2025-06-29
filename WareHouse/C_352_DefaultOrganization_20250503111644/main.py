'''
Main entry point for the application.
Reads input for the number of giants and their respective heights,
then calculates and prints the maximum height of the topmost giant.
'''
import itertools
def main():
    try:
        N = int(input("Enter the number of giants: "))
        if N <= 0:
            print("No giants to stack.")
            return
        A = read_heights("shoulder heights")
        B = read_heights("head heights")
        if len(A) != N or len(B) != N:
            print("Error: The number of heights provided does not match the number of giants.")
            return
        max_height = calculate_max_height(A, B)
        print(f"Max Height: {max_height}")
    except ValueError:
        print("Error: Please enter valid integers for the number of giants.")
def read_heights(prompt):
    '''
    Reads heights from user input and validates that they are integers.
    Parameters:
    prompt (str): The prompt message to display to the user.
    Returns:
    list: A list of integers representing the heights.
    '''
    while True:
        try:
            heights = list(map(int, input(f"Enter the {prompt} (space-separated): ").split()))
            if any(height < 0 for height in heights):
                print("Error: Heights cannot be negative.")
                continue
            return heights
        except ValueError:
            print("Error: Please enter valid integers for heights.")
def calculate_max_height(A, B):
    '''
    Calculate the maximum height of the topmost giant by evaluating all permutations.
    Parameters:
    A (list): List of shoulder heights of the giants.
    B (list): List of head heights of the giants.
    Returns:
    int: The maximum possible height of the head of the topmost giant.
    '''
    max_height = 0
    N = len(A)
    # Generate all permutations of indices
    for perm in itertools.permutations(range(N)):
        current_height = 0
        for i in perm:
            current_height += A[i]
            max_height = max(max_height, current_height + B[i])
    return max_height
if __name__ == "__main__":
    main()