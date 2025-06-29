'''
Main application file to run the matrix isolation checker.
'''
def main():
    H, W = map(int, input("Enter dimensions (H W): ").split())
    if H <= 0 or W <= 0:
        print("Impossible")
        return
    matrix = []
    print("Enter matrix (0s and 1s):")
    for _ in range(H):
        row = list(map(int, input().split()))
        if len(row) != W:
            print("Invalid row length. Please ensure each row has W elements.")
            return
        matrix.append(row)
    # Check if the matrix is entirely filled with 0s or 1s
    if all(matrix[i][j] == 0 for i in range(H) for j in range(W)):
        print("Total operations: 0")
        return
    if all(matrix[i][j] == 1 for i in range(H) for j in range(W)):
        print("Impossible")
        return
    operations = 0
    while True:
        rows_to_flip = set()
        for i in range(H):
            for j in range(W):
                if is_isolated(matrix, i, j):
                    rows_to_flip.add(i)
        if not rows_to_flip:
            break  # No more isolated elements, exit the loop
        # Flip the collected rows
        for i in rows_to_flip:
            flip_row(matrix, i)
            operations += 1
        # Check if any new isolated elements have been created
        if any(is_isolated(matrix, i, j) for i in rows_to_flip for j in range(W)):
            print("Impossible")
            return
    if any(is_isolated(matrix, i, j) for i in range(H) for j in range(W)):
        print("Impossible")
    else:
        print(f"Total operations: {operations}")
def is_isolated(matrix, i, j):
    """
    Check if the element at position (i, j) in the matrix is isolated.
    An element is considered isolated if it is 1 and all its adjacent elements (up, down, left, right)
    are 0 or out of bounds of the matrix.
    Parameters:
    matrix (list of list of int): The matrix to check.
    i (int): The row index of the element.
    j (int): The column index of the element.
    Returns:
    bool: True if the element is isolated, False otherwise.
    """
    if matrix[i][j] == 0:
        return False
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] == 1:
            return False
    return True
def flip_row(matrix, i):
    """
    Flip all elements in row i of the matrix.
    This function changes all 0s to 1s and all 1s to 0s in the specified row.
    Parameters:
    matrix (list of list of int): The matrix to modify.
    i (int): The row index to flip.
    """
    for j in range(len(matrix[0])):
        matrix[i][j] = 1 - matrix[i][j]
if __name__ == "__main__":
    main()