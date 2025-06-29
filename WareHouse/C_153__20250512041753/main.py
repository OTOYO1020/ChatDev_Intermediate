'''
Main application file for the Monster Attack program.
'''
from typing import List
from monster_attack import minimum_attacks
def main():
    # Read input from standard input
    N = int(input("Enter the number of monsters (N): "))
    K = int(input("Enter the special move limit (K): "))
    H = list(map(int, input("Enter the monster healths (H) separated by spaces: ").split()))
    # Calculate the minimum attacks needed
    result = minimum_attacks(N, K, H)
    # Output the result
    print(f"Minimum Attacks Needed: {result}")
if __name__ == "__main__":
    main()