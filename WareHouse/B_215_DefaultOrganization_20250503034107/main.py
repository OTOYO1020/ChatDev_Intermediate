'''
This is the main file for the Power of Two application.
It reads a positive integer N from standard input and calculates
the largest integer k such that 2^k <= N.
'''
def main():
    while True:
        try:
            N = int(input("Enter a positive integer greater than zero (N): "))
            if N <= 0:
                raise ValueError("N must be a positive integer.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Input Error: {e}. Please try again.")
    k = calculate_power_of_two(N)
    print(f"The largest integer k such that 2^k <= N is: {k}")
def calculate_power_of_two(N):
    """
    Calculate the largest integer k such that 2^k <= N.
    Parameters:
    N (int): A positive integer input.
    Returns:
    int: The largest integer k satisfying the condition.
    """
    k = 0
    while (2 ** k) <= N:
        k += 1
    return k - 1
if __name__ == "__main__":
    main()