'''
Module to calculate the number of ways a knight can reach a given square on a chessboard.
'''
def countKnightWays(X: int, Y: int) -> int:
    MOD = 10**9 + 7
    dp = [[0] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = 1  # Base case: one way to be at the starting position (0, 0)
    # Possible knight moves
    knight_moves = [
        (1, 2), (1, -2), (-1, 2), (-1, -2), 
        (2, 1), (2, -1), (-2, 1), (-2, -1)
    ]
    # Iterate through each square on the board
    for i in range(X + 1):
        for j in range(Y + 1):
            for move in knight_moves:
                ni, nj = i + move[0], j + move[1]
                if 0 <= ni <= X and 0 <= nj <= Y:
                    dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD
    return dp[X][Y]