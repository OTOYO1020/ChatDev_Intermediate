'''
Main application file for the sum of K smallest elements.
'''
from calculator import sum_of_k_smallest
def main():
    while True:
        try:
            A = list(map(int, input("Enter the integer sequence (comma-separated): ").split(',')))
            if not A:  # Check if the list is empty
                raise ValueError("The integer sequence cannot be empty.")
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Invalid input. {e}")
    N = len(A)  # Calculate N based on the length of A
    M = int(input("Enter M (subarray length): "))
    K = int(input("Enter K (number of smallest elements): "))
    # Validate input values
    if M <= 0 or M > N:
        raise ValueError("M must be a positive integer and less than or equal to N.")
    if K <= 0 or K > M:
        raise ValueError("K must be a positive integer and less than or equal to M.")
    # Calculate results
    results = sum_of_k_smallest(A, N, M, K)
    # Display results
    print("Results:", results)
if __name__ == "__main__":
    main()