'''
Main application file for calculating maximum product from permutations of digits.
'''
from utils import generate_permutations, calculate_product
def main():
    while True:
        try:
            N = input("Enter a positive integer (no leading zeros): ")
            if not N.isdigit() or int(N) <= 0:
                print("Error: Input must be a positive integer.")
                continue  # Prompt again for valid input
            break  # Exit loop if input is valid
        except Exception as e:
            print(f"Error: {str(e)}")
    digits = list(N)
    max_product = 0
    # Generate unique permutations and check for valid splits
    for perm in generate_permutations(digits):
        for i in range(1, len(perm)):
            A_str = ''.join(perm[:i])
            B_str = ''.join(perm[i:])
            # Ensure both parts are non-empty and check for leading zeros
            if A_str and B_str and A_str[0] != '0' and B_str[0] != '0':
                A = int(A_str)
                B = int(B_str)
                product = calculate_product(A, B)
                max_product = max(max_product, product)
    if max_product == 0:
        print("No valid products found.")
    else:
        print(f"Max Product: {max_product}")
if __name__ == "__main__":
    main()