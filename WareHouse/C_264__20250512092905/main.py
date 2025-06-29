'''
Main application file for the matrix transformation checker.
'''
import sys
from matrix_utils import canTransformMatrix
def main():
    try:
        # Read dimensions for matrix A
        h1, w1 = map(int, input("Enter dimensions for Matrix A (H W): ").split())
        if h1 <= 0 or w1 <= 0:
            print("Error: Dimensions for Matrix A must be positive integers.")
            return
        # Read dimensions for matrix B
        h2, w2 = map(int, input("Enter dimensions for Matrix B (H W): ").split())
        if h2 <= 0 or w2 <= 0:
            print("Error: Dimensions for Matrix B must be positive integers.")
            return
        # Check if dimensions of B are valid
        if h2 > h1 or w2 > w1:
            print("No, transformation is not possible.")
            return
        # Read elements for matrix A
        print(f"Enter {h1 * w1} elements for Matrix A (space-separated):")
        try:
            a_elements = list(map(int, input().split()))
        except ValueError:
            print("Error: Please enter valid integers for the elements of Matrix A.")
            return
        if len(a_elements) != h1 * w1:
            print("Error: Number of elements for Matrix A does not match the specified dimensions.")
            return
        A = [a_elements[i * w1:(i + 1) * w1] for i in range(h1)]
        # Read elements for matrix B
        print(f"Enter {h2 * w2} elements for Matrix B (space-separated):")
        try:
            b_elements = list(map(int, input().split()))
        except ValueError:
            print("Error: Please enter valid integers for the elements of Matrix B.")
            return
        if len(b_elements) != h2 * w2:
            print("Error: Number of elements for Matrix B does not match the specified dimensions.")
            return
        B = [b_elements[i * w2:(i + 1) * w2] for i in range(h2)]
        # Check if transformation is possible
        if canTransformMatrix(A, B):
            print("Yes, transformation is possible.")
        else:
            print("No, transformation is not possible.")
    except ValueError:
        print("Error: Please enter valid integers for dimensions and elements.")
if __name__ == "__main__":
    main()