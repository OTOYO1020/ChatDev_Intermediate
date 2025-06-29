'''
Grid class to manage the block grid and perform calculations.
'''
class Grid:
    def __init__(self, H, W):
        self.H = H
        self.W = W
        self.A = [[0] * W for _ in range(H)]
    def get_input(self):
        '''
        Prompts the user to enter values for each square in the grid.
        Validates input to ensure all entries are non-negative integers.
        '''
        print("Enter the values for each square in the grid (space-separated non-negative integers).")
        for i in range(self.H):
            while True:
                row_values = input(f"Row {i + 1}: ").strip()
                if len(row_values) == 0:
                    print("Error: Input cannot be empty. Please enter values for the row.")
                    continue  # Prompt for input again
                row_values = row_values.split()
                if len(row_values) != self.W:
                    print(f"Error: Please enter exactly {self.W} integers for row {i + 1}. You entered {len(row_values)} values.")
                    continue  # Prompt for input again
                try:
                    self.A[i] = [int(value) for value in row_values]
                    # Check for negative values
                    if any(value < 0 for value in self.A[i]):
                        print("Error: Please enter non-negative integers only.")
                        continue  # Prompt for input again
                    break  # Exit the loop if input is valid
                except ValueError:
                    print("Error: Please enter valid non-negative integers. Ensure there are no non-integer values.")
                    print("Example of valid input: '1 2 3' for a row of three columns.")
    def calculate_blocks_to_remove(self):
        '''
        Calculates the total number of blocks to remove to equalize the number of blocks in each square.
        Returns the total number of blocks that need to be removed.
        '''
        # Check for zero dimensions to avoid division by zero
        if self.H == 0 or self.W == 0:
            print("Error: Grid dimensions cannot be zero.")
            return 0  # Or handle it as needed
        total_blocks = sum(sum(row) for row in self.A)
        if total_blocks == 0:  # Handle case where total blocks is zero
            return 0
        target_blocks = total_blocks // (self.H * self.W)
        blocks_to_remove = 0
        for i in range(self.H):
            for j in range(self.W):
                if self.A[i][j] > target_blocks:
                    blocks_to_remove += self.A[i][j] - target_blocks
        return blocks_to_remove