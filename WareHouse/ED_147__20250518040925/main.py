'''
Main application file for the Min Unbalancedness Calculator.
'''
from min_unbalancedness import min_unbalancedness
def main():
    try:
        H = int(input("Enter the number of rows (H): "))
        W = int(input("Enter the number of columns (W): "))
        print("Enter grid A (space-separated rows):")
        A = [list(map(int, input().split())) for _ in range(H)]
        print("Enter grid B (space-separated rows):")
        B = [list(map(int, input().split())) for _ in range(H)]
        # Check if the dimensions of A and B match H and W
        if len(A) != H or len(B) != H or any(len(row) != W for row in A) or any(len(row) != W for row in B):
            raise ValueError("Grid dimensions do not match the specified H and W.")
        min_unbalanced = min_unbalancedness(H, W, A, B)
        print(f"Minimum Unbalancedness: {min_unbalanced}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()