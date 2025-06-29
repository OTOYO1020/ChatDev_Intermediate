'''
Main application file for the 11/22 subsequence query processor.
'''
import sys
from typing import List, Tuple
from utils import max_11_22_subsequence
def main():
    # Input handling
    S = input("Enter the string (S): ")
    Q = int(input("Enter number of queries (Q): "))
    queries = []
    for _ in range(Q):
        L, R = map(int, input("Enter query (L R): ").split())
        # Validate L and R
        if L < 1 or R > len(S) or L > R:
            print(f"Invalid query (L={L}, R={R}). Please ensure 1 <= L <= R <= {len(S)}.")
        else:
            queries.append((L, R))
    # Process queries only if there are valid queries
    if queries:
        results = max_11_22_subsequence(S, queries)
        # Output handling
        for result in results:
            print(result)
    else:
        print("No valid queries to process.")
if __name__ == "__main__":
    main()