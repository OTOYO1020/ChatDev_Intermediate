'''
Main application file for the Max Product Calculator.
'''
from product_calculator import max_product
def main():
    # Input handling
    N = int(input("Enter N: "))
    K = int(input("Enter K: "))
    A = list(map(int, input("Enter List A (space-separated): ").split()))
    if len(A) != N:
        raise ValueError("Length of A must be equal to N.")
    result = max_product(N, K, A)
    print(f"Max Product: {result}")
if __name__ == "__main__":
    main()