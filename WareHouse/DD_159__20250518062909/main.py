'''
Main application file for counting equal pairs in a list of integers.
'''
import sys
from utils import count_equal_pairs
def main():
    # Input handling
    try:
        n = int(input("Enter the number of elements (N): "))
        a = list(map(int, input("Enter the list of integers (space-separated): ").split()))
        if len(a) != n:
            raise ValueError("The number of elements does not match N.")
        results = count_equal_pairs(n, a)
        print("Results:")
        for result in results:
            print(result)
    except Exception as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()