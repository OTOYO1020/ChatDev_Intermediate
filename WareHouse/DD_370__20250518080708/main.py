'''
Main application file for the Wall Destroyer application.
'''
from grid_manager import count_remaining_walls
def main():
    H = 5  # Height of the grid
    W = 5  # Width of the grid
    Q = int(input("Enter the number of queries: "))  # Number of queries
    queries = []
    for _ in range(Q):
        query = input("Enter the query (R_q C_q): ")
        R_q, C_q = map(int, query.split())
        queries.append((R_q, C_q))
    remaining_walls = count_remaining_walls(H, W, Q, queries)
    print(f"Remaining Walls: {remaining_walls}")
if __name__ == "__main__":
    main()