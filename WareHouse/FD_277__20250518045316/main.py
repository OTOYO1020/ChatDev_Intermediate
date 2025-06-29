'''
Main application file for the Matrix Sorter.
'''
from matrix_utils import can_matrix_be_sorted
def main():
    try:
        dimensions = input("Enter matrix dimensions (H W): ").split()
        H = int(dimensions[0])
        W = int(dimensions[1])
        if H <= 0 or W <= 0:
            raise ValueError("H and W must be positive integers.")
        print("Enter matrix rows (space-separated):")
        A = []
        for _ in range(H):
            row = list(map(int, input().split()))
            if len(row) != W:
                raise ValueError("Number of columns does not match W.")
            A.append(row)
        result = can_matrix_be_sorted(H, W, A)
        if result:
            print("The matrix can be sorted.")
        else:
            print("The matrix cannot be sorted.")
    except ValueError as ve:
        print(f"Input Error: {str(ve)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
if __name__ == "__main__":
    main()