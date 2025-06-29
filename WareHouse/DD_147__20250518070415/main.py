'''
Main application file for the XOR sum calculator.
'''
from xor_sum import calculate_xor_sum
def main():
    '''
    Main function to handle input and output for the XOR sum calculation.
    '''
    try:
        N = int(input("Enter the number of elements (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")
        A = list(map(int, input("Enter the elements (space-separated): ").split()))
        if len(A) != N:
            raise ValueError("The length of the list A must be equal to N.")
        for number in A:
            if not (0 <= number < 2**60):
                raise ValueError("Each element must satisfy the constraint 0 <= A[i] < 2^60.")
        result = calculate_xor_sum(N, A)
        print(f"XOR Sum: {result}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()