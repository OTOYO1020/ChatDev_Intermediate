'''
Main entry point for the grid matching application.
'''
def main():
    # Read dimensions of grids S and T
    try:
        n, m = map(int, input("Enter dimensions N and M: ").split())
        if n < m or n <= 0 or m <= 0:
            raise ValueError("Invalid dimensions. Ensure N >= M and both are positive integers.")
        # Read grid S
        grid_s = []
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            if len(row) != n:
                raise ValueError("Each row must have exactly N elements.")
            grid_s.append(row)
        # Read grid T
        grid_t = []
        for _ in range(m):
            row = list(map(int, input().strip().split()))
            if len(row) != m:
                raise ValueError("Each row must have exactly M elements.")
            grid_t.append(row)
        # Find match
        matcher = GridMatcher(grid_s, grid_t)
        result = matcher.find_match()
        if result:
            print(f"{result[0]} {result[1]}")
        else:
            print("No match found.")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    from grid_matcher import GridMatcher
    main()