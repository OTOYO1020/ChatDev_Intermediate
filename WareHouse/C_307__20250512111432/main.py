'''
Main application file for the sheet configuration checker.
'''
from utils import can_create_sheet
def main():
    # Input dimensions and representations of sheets A, B, and X
    A = input("Enter dimensions and representation of sheet A (H_A,W_A,A): ").split(',')
    B = input("Enter dimensions and representation of sheet B (H_B,W_B,B): ").split(',')
    X = input("Enter dimensions and representation of sheet X (H_X,W_X,X): ").split(',')
    try:
        H_A, W_A = int(A[0]), int(A[1])
        H_B, W_B = int(B[0]), int(B[1])
        H_X, W_X = int(X[0]), int(X[1])
        result = can_create_sheet(H_A, W_A, A[2], H_B, W_B, B[2], H_X, W_X, X[2])
        # Output the result
        print("YES" if result else "NO")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()