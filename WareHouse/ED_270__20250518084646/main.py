'''
Main application file for the Apple Basket application.
'''
from apple_basket import remaining_apples
def main():
    '''
    Main function to execute the Apple Basket application.
    '''
    # Parse input
    N = int(input("Enter the number of baskets (N): "))
    while True:
        try:
            A = list(map(int, [x.strip() for x in input("Enter the number of apples in each basket (comma-separated): ").split(',')]))
            if len(A) != N:
                raise ValueError("The number of apples must match the number of baskets.")
            if any(x < 0 for x in A):  # Check for negative values
                raise ValueError("The number of apples must be non-negative.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    K = int(input("Enter the number of apples to eat (K): "))
    # Calculate remaining apples
    remaining = remaining_apples(N, A, K)
    print(f"Remaining apples: {remaining}")
if __name__ == "__main__":
    main()