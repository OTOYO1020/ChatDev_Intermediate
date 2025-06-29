'''
Main application file for counting operations to make two integers equal.
'''
def count_operations(A: int, B: int) -> int:
    """
    Count the number of operations required to make two integers equal
    by repeatedly subtracting the smaller from the larger.
    Parameters:
    A (int): The first integer.
    B (int): The second integer.
    Returns:
    int: The number of operations performed until A equals B.
    """
    count = 0
    while A != B:
        if A > B:
            count += A // B  # Count how many times B can be subtracted from A
            A %= B  # Update A to the remainder
        else:
            count += B // A  # Count how many times A can be subtracted from B
            B %= A  # Update B to the remainder
    return count
if __name__ == "__main__":
    import sys
    from utils import validate_input  # Import the validate_input function
    def get_input():
        while True:
            try:
                A = input("Enter the first positive integer A (or type 'exit' to quit): ").strip()
                if A.lower() == "exit":
                    print("Exiting the program.")
                    return None, None
                B = input("Enter the second positive integer B (or type 'exit' to quit): ").strip()
                if B.lower() == "exit":
                    print("Exiting the program.")
                    return None, None
                if validate_input(A) and validate_input(B):
                    return int(A), int(B)
                else:
                    print("Input Error: Please enter valid integers between 1 and 10^18 for both A and B.")
            except ValueError:
                print("Input Error: Please enter valid integers.")
    A, B = get_input()
    if A is not None and B is not None:
        result = count_operations(A, B)
        print(result)