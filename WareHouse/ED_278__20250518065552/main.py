'''
Main application file for the distinct integers counter with blackout functionality.
'''
from grid_processor import GridProcessor
def main():
    try:
        H = int(input("Enter Height (H): "))
        W = int(input("Enter Width (W): "))
        N = int(input("Enter Number of Rows (N): "))
        # Improved grid input handling
        A = []
        for i in range(N):
            row_input = input(f"Enter Row {i + 1} (space-separated integers): ").strip()
            row = list(map(int, row_input.split()))
            if len(row) != W:
                raise ValueError(f"Row {i + 1} does not match the specified width (W).")
            A.append(row)
        h = int(input("Enter Blackout Height (h): "))
        w = int(input("Enter Blackout Width (w): "))
        # Validate grid dimensions
        if len(A) != N:
            raise ValueError("Grid dimensions do not match specified height and width.")
        processor = GridProcessor()
        results = processor.count_distinct_integers(H, W, N, A, h, w)
        print("Results:", results)
    except Exception as e:
        print("Input Error:", str(e))
if __name__ == "__main__":
    main()