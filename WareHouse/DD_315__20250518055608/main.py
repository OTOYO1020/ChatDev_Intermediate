'''
Main function to handle input and output for counting remaining cookies.
'''
from cookie_counter import count_remaining_cookies
def main() -> None:
    input_data = input("Enter cookie grid (comma-separated rows): ")
    grid = [row.split(',') for row in input_data.split(';')]
    # Validate that all rows have the same length
    if len(set(len(row) for row in grid)) != 1:
        print("Error: All rows must have the same number of columns.")
        return
    remaining_cookies = count_remaining_cookies(len(grid), len(grid[0]), grid)
    print(f"Remaining Cookies: {remaining_cookies}")
if __name__ == "__main__":
    main()