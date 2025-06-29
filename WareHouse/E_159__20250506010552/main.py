'''
Main application file for the chocolate bar cutting program.
'''
def calculate_cuts(H, W, K, matrix):
    cut_count = 0
    current_white_count = 0
    for i in range(H):
        for j in range(W):
            if matrix[i][j] == '1':
                current_white_count += 1
            if current_white_count > K:
                cut_count += 1
                current_white_count = 1 if matrix[i][j] == '1' else 0  # Reset to current square's value
        # Final check after processing all columns in the row
        if current_white_count > K:
            cut_count += 1
            current_white_count = 0  # Reset after counting the cut for the row
        # Account for cuts between rows only if there are white squares in the next row
        if i < H - 1 and current_white_count > 0 and '1' in matrix[i + 1]:  # Check next row for whites
            cut_count += 1  # Increment cut count for the cut between rows
            current_white_count = 0  # Reset for the next row
    return cut_count
if __name__ == "__main__":
    H = int(input("Enter height (H): "))
    W = int(input("Enter width (W): "))
    K = int(input("Enter max white squares (K): "))
    matrix = []
    print("Enter the matrix row by row (0 for dark, 1 for white):")
    for _ in range(H):
        row = input().strip().split()
        matrix.append(row)
    cuts_needed = calculate_cuts(H, W, K, matrix)
    print(cuts_needed)