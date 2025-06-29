'''
Main entry point of the application.
'''
from game_logic import can_complete_moves
def main():
    # Example input values
    N = 5  # Number of moves
    M = 5  # Example grid size (columns)
    H = 10  # Initial health
    K = 10  # Health restore value
    S = "RRUUD"  # Moves string
    items = [(1, 1), (2, 2)]  # Example item coordinates
    result = can_complete_moves(N, M, H, K, S, items)
    print("YES" if result else "NO")
if __name__ == "__main__":
    main()