'''
Main application file for the Alphametic Solver.
'''
import sys
from alphametic import is_alphametic
def main():
    S1 = input("Enter first string (S1): ")
    S2 = input("Enter second string (S2): ")
    S3 = input("Enter third string (S3): ")
    result = is_alphametic(S1, S2, S3)
    if result:
        print(f"Solution: {result[0]} {result[1]} {result[2]}")
    else:
        print("No solution")
if __name__ == "__main__":
    main()