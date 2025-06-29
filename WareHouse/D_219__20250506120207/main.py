'''
Main entry point for the lunchbox application.
'''
from lunchbox import Lunchbox, LunchboxManager  # Ensure Lunchbox is imported
def main():
    # Read integers N, X, and Y from standard input
    N, X, Y = map(int, input().split())
    # Input validation for constraints
    if not (1 <= N <= 300) or not (1 <= X <= 300) or not (1 <= Y <= 300):
        print("Error: N, X, and Y must be in the range 1 to 300.")
        return
    # Handle edge case where no lunchboxes are needed
    if X == 0 and Y == 0:
        print(0)
        return
    # Initialize LunchboxManager
    manager = LunchboxManager()
    # Read lunchboxes
    for _ in range(N):
        A_i, B_i = map(int, input().split())
        lunchbox = Lunchbox(A_i, B_i)
        manager.add_lunchbox(lunchbox)
    # Find the minimum lunchboxes needed
    min_lunchboxes = manager.find_min_lunchboxes(X, Y)
    # Output the result
    if min_lunchboxes == -1:
        print("Impossible")
    else:
        print(min_lunchboxes)
if __name__ == "__main__":
    main()