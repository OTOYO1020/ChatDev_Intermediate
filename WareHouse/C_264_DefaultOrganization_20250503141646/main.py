'''
Main application file for the matrix transformation checker.
'''
from matrix_utils import can_transform
def main():
    # Read dimensions of matrix A
    H1, W1 = map(int, input("Enter dimensions of matrix A (H1 W1): ").split())
    if H1 <= 0 or W1 <= 0:
        print("Matrix A must have positive dimensions.")
        return
    A = []
    print("Enter matrix A values row by row (space-separated integers):")
    for _ in range(H1):
        while True:
            try:
                row = list(map(int, input().strip().split()))
                if len(row) != W1:
                    print(f"Each row of matrix A must have exactly {W1} elements. Please try again.")
                    continue  # Prompt for input again
                A.append(row)
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input. Please enter integers only. Please try again.")
    # Read dimensions of matrix B
    H2, W2 = map(int, input("Enter dimensions of matrix B (H2 W2): ").split())
    if H2 <= 0 or W2 <= 0:
        print("Matrix B must have positive dimensions.")
        return
    B = []
    print("Enter matrix B values row by row (space-separated integers):")
    for _ in range(H2):
        while True:
            try:
                row = list(map(int, input().strip().split()))
                if len(row) != W2:
                    print(f"Each row of matrix B must have exactly {W2} elements. Please try again.")
                    continue  # Prompt for input again
                B.append(row)
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input. Please enter integers only. Please try again.")
    # Check if transformation is possible
    result = can_transform(A, B)
    print("YES" if result else "NO")
if __name__ == "__main__":
    main()