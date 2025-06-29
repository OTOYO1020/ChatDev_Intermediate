'''
Main file to run the Matrix Transposition application.
'''
def main():
    # Read dimensions H and W
    while True:
        try:
            H, W = map(int, input("Enter the number of rows (H) and columns (W) of the matrix, separated by a space: ").split())
            if H <= 0 or W <= 0:
                raise ValueError("Dimensions must be positive integers.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter two positive integers.")
    # Initialize matrix A
    A = []
    # Populate matrix A
    for i in range(H):
        while True:
            try:
                row = list(map(int, input(f"Please enter the integers for row {i + 1}, separated by spaces: ").split()))
                if len(row) != W:
                    raise ValueError("Row length does not match specified width.")
                A.append(row)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter {W} integers.")
    # Initialize transposed matrix B with dimensions W x H to hold transposed values from A
    B = [[0] * H for _ in range(W)]  # Create a 2D list to hold transposed values
    # Transpose the matrix
    for i in range(H):
        for j in range(W):
            B[j][i] = A[i][j]  # Assign transposed values from A to B
    # Print the transposed matrix B
    for row in B:
        print(' '.join(map(str, row)))
if __name__ == "__main__":
    main()