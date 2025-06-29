'''
Main application file for the Max Product Calculator.
'''
from utils import calculate_max_product
def main():
    # Read integers N and K from standard input
    N, K = map(int, input("Enter N and K (space-separated): ").split())
    # Read the array of integers A
    array = list(map(int, input("Enter array elements (space-separated): ").split()))
    if len(array) != N:
        raise ValueError("The number of elements in the array does not match N.")
    max_product = calculate_max_product(array, K)
    print(f"Max Product: {max_product}")
if __name__ == "__main__":
    main()