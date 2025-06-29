'''
Handles user input and validates it.
'''
def get_input():
    M = int(input("Enter the number of sets (M): "))
    N = int(input("Enter the maximum integer value (N): "))
    if M < 1 or N < 1:
        raise ValueError("M and N must be positive integers.")
    sets = []
    for i in range(M):
        set_input = input(f"Enter integers for set {i + 1} (comma-separated): ")
        while not set_input:  # Ensure the input is not empty
            set_input = input(f"Set {i + 1} cannot be empty. Please enter integers (comma-separated): ")
        current_set = list(map(int, set_input.split(',')))
        # Validate that all integers are within the range [1, N]
        if any(x < 1 or x > N for x in current_set):
            raise ValueError(f"All integers in set {i + 1} must be between 1 and {N}.")
        if not current_set:  # Check if the current set is empty
            raise ValueError(f"Set {i + 1} cannot be empty.")
        sets.append(current_set)
    return M, N, sets