```markdown
# Coin Collector

A dynamic programming application for collecting coins on a grid.

## Overview

The Coin Collector application allows users to calculate the maximum number of coins that can be collected while moving from the top-left corner (1,1) to the bottom-right corner (H,W) of a grid. The movement is restricted to only down or right directions. The application also tracks the path taken to achieve the maximum coins collected.

## Main Functions

- **max_coins(H: int, W: int, N: int, coins: List[Tuple[int, int]]) -> Tuple[int, List[Tuple[int, int]]]**: 
  - Calculates the maximum number of coins that can be collected and the path taken to collect them.
  - Parameters:
    - `H`: Height of the grid.
    - `W`: Width of the grid.
    - `N`: Number of coins.
    - `coins`: List of tuples representing the positions of the coins.
  - Returns:
    - A tuple containing the maximum number of coins collected and the path taken as a list of tuples.

- **input_validation(H: int, W: int, N: int, coins: List[Tuple[int, int]])**: 
  - Validates the input parameters to ensure they meet the required constraints.

## Installation

To run the Coin Collector application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: You can install the required dependencies using pip. Open your terminal or command prompt and run:

   ```bash
   pip install typing
   ```

## How to Use

1. **Run the Application**: 
   - Navigate to the directory where `main.py` is located.
   - Run the application using the command:

   ```bash
   python main.py
   ```

2. **Input Parameters**: 
   - The application will prompt you to enter the following:
     - **Height (H)**: The height of the grid (positive integer).
     - **Width (W)**: The width of the grid (positive integer).
     - **Number of Coins (N)**: The number of coins (non-negative integer).
     - **Coin Positions (R,C)**: Enter the positions of the coins in the format (R,C) separated by semicolons. For example: `1,2;2,3;3,1`.

3. **View Results**: 
   - After entering the inputs, the application will calculate and display:
     - The maximum number of coins collected.
     - The path taken to collect the coins in the format of coordinates.

## Example Usage

```
Enter Height (H): 3
Enter Width (W): 3
Enter Number of Coins (N): 3
Enter Coin Positions (R,C) separated by semicolons: 1,2;2,3;3,1
Max Coins Collected: 3
Path: (1, 1) -> (1, 2) -> (2, 2) -> (2, 3) -> (3, 3)
```

## Edge Cases

- If there are no coins (`N = 0`), the application will return `0` coins collected and an empty path.
- If the grid size is minimal (e.g., `H = 1` and `W = 1`), the application will still function correctly as long as the input parameters are valid.

## Conclusion

The Coin Collector application provides a straightforward way to calculate the maximum coins collectible on a grid while adhering to movement constraints. Follow the instructions above to set it up and start collecting coins!
```