'''
Main application file for counting square pairs using standard input and output.
'''
from utils import validate_input  # Ensure this import is present
import math  # Import math for square root calculation
def count_square_pairs(N: int) -> int:
    '''
    Counts the number of pairs (i, j) such that 1 <= i, j <= N and i * j is a perfect square.
    '''
    count = 0  # Initialize count to 0
    for i in range(1, N + 1):  # Iterate through all i
        for j in range(1, N + 1):  # Iterate through all j
            product = i * j  # Calculate the product
            if math.isqrt(product) ** 2 == product:  # Check if product is a perfect square
                count += 1  # Increment count if it is a perfect square
    return count  # Return the total count
if __name__ == "__main__":
    while True:  # Loop until valid input is received
        user_input = input("Enter a number (N): ")
        if validate_input(user_input):
            N = int(user_input)
            result = count_square_pairs(N)
            print(result)  # Output the result as an integer
            break  # Exit the loop after valid input
        else:
            print("Please enter a valid positive integer.")