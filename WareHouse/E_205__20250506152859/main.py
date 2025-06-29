'''
Main entry point for the Ball Arrangement application.
'''
import sys
from arrangement_calculator import count_valid_arrangements
def main():
    try:
        N = int(input("Enter number of white balls (N): "))
        M = int(input("Enter number of black balls (M): "))
        K = int(input("Enter maximum difference (K): "))
        if N < 0 or M < 0 or K < 0:
            raise ValueError("N, M, and K must be non-negative integers.")
        valid_count = count_valid_arrangements(N, M, K)
        print(f"Valid arrangements: {valid_count}")
    except ValueError as e:
        print(f"Input error: {e}")
if __name__ == "__main__":
    main()