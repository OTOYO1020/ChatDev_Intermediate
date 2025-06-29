'''
Main application file for the GCD calculator.
'''
import sys
from gcd_calculator import max_gcd_with_k_elements
def main():
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    sequence = list(map(int, input_data[0].split(',')))
    k = int(input_data[1])
    # Validate K
    if k < 1 or k > len(sequence):
        raise ValueError("K must be between 1 and the length of the sequence.")
    results = max_gcd_with_k_elements(sequence, k)
    print(f"Maximum GCDs: {results}")
if __name__ == "__main__":
    main()