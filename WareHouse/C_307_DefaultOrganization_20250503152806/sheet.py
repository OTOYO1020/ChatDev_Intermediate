'''
Module for handling sheet operations including combining sheets and checking cut-outs.
'''
def create_sheet_C(A, B):
    H_A = len(A)
    W_A = len(A[0]) if H_A > 0 else 0
    H_B = len(B)
    W_B = len(B[0]) if H_B > 0 else 0
    H_C = max(H_A, H_B)
    W_C = max(W_A, W_B)
    # Initialize sheet C with dots
    C = [['.' for _ in range(W_C)] for _ in range(H_C)]
    for i in range(H_C):
        for j in range(W_C):
            if i < H_A and j < W_A and A[i][j] == '#':
                C[i][j] = '#'
            elif i < H_B and j < W_B and B[i][j] == '#':
                C[i][j] = '#'
    return C
def can_cut_out(C, X, H_X, W_X, A, B):
    H_C = len(C)
    W_C = len(C[0]) if H_C > 0 else 0
    # Collect black square coordinates from both A and B
    black_squares_A = {(i, j) for i in range(len(A)) for j in range(len(A[0])) if i < len(A) and j < len(A[0]) and A[i][j] == '#'}
    black_squares_B = {(i, j) for i in range(len(B)) for j in range(len(B[0])) if i < len(B) and j < len(B[0]) and B[i][j] == '#'}
    all_black_squares = black_squares_A.union(black_squares_B)
    # Ensure C is large enough to contain X
    if H_C < H_X or W_C < W_X:
        return False
    # Iterate through all possible positions for the cut-out
    for start_row in range(H_C - H_X + 1):
        for start_col in range(W_C - W_X + 1):
            cut_out = [C[start_row + i][start_col:start_col + W_X] for i in range(H_X)]
            if cut_out == X:
                # Collect black squares in the cut-out
                cut_out_black_squares = {(start_row + i, start_col + j) for i in range(H_X) for j in range(W_X) if cut_out[i][j] == '#'}
                # Check if cut-out contains all black squares from A and B
                if all((i, j) in cut_out_black_squares for (i, j) in all_black_squares):
                    return True
    return False