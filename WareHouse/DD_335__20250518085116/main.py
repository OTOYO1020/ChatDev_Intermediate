'''
Main application file for the Dragon Arrangement software.
'''
from dragon_arrangement import arrange_dragon_parts
def main():
    N = int(input("Enter grid size (N): "))
    if N < 1:
        print("Grid size must be at least 1.")
        return
    positions = arrange_dragon_parts(N)
    display_grid(N, positions)
def display_grid(N, positions):
    '''
    Displays the grid with Takahashi and dragon parts.
    Parameters:
    N (int): The size of the grid.
    positions (List[Tuple[int, int]]): The positions of the dragon parts.
    '''
    grid = [[' ' for _ in range(N)] for _ in range(N)]
    center = (N // 2, N // 2)
    grid[center[0]][center[1]] = 'T'  # T for Takahashi
    for pos in positions:
        grid[pos[0]][pos[1]] = 'D'  # D for Dragon part
    for row in grid:
        print(' '.join(row))
if __name__ == "__main__":
    main()