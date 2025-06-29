Here is the `manual.md` file for the Pawn Game application, detailing its main functions, installation instructions, and usage guidelines.

```markdown
# Pawn Game

A strategic game where a white pawn navigates a grid while avoiding black pawns.

## Overview

The Pawn Game application allows users to simulate the movement of a white pawn on a grid while avoiding black pawns. The objective is to determine how many valid positions the white pawn can reach in the last row of the grid after applying the movement rules.

## Main Functions

- **count_possible_Y(N: int, M: int, black_pawns: List[Tuple[int, int]]) -> int**: 
  - This function calculates the number of valid Y positions in the last row (2N, Y) that can be reached by the white pawn.
  - **Parameters**:
    - `N`: The maximum row number (a positive integer).
    - `M`: The number of black pawns (a non-negative integer).
    - `black_pawns`: A list of tuples representing the positions of black pawns on the grid.
  - **Returns**: An integer representing the count of valid Y positions.

## Installation

To run the Pawn Game application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Open your terminal or command prompt and run the following command to install the required dependencies:

   ```bash
   pip install typing
   ```

   Note: The `typing` module is included in Python 3.5 and later, so you may not need to install it separately if you are using a compatible version.

## How to Use the Application

1. **Run the Application**: Navigate to the directory where the `main.py` file is located and execute the following command:

   ```bash
   python main.py
   ```

2. **Input Parameters**:
   - You will be prompted to enter the maximum row number (N) and the number of black pawns (M).
   - Enter the black pawn positions in the format (X,Y) separated by commas. For example: `1,2, 2,3` for two black pawns at positions (1,2) and (2,3).

3. **Output**: The application will calculate and display the number of valid Y positions that the white pawn can reach in the last row.

## Example Usage

```
Enter the maximum row number (N): 3
Enter the number of black pawns (M): 2
Enter black pawn positions (X,Y) separated by commas: 1,2, 2,3
Valid Y positions: 2
```

## Error Handling

The application includes error handling for the following scenarios:
- Invalid input types (e.g., non-integer values for N or M).
- Black pawn positions that are out of bounds or overlap.
- Mismatch between the number of black pawn positions provided and the expected count.

## Conclusion

The Pawn Game application provides a fun and strategic way to explore pawn movements on a grid. Feel free to modify the code to enhance functionality or adapt it to your needs. Happy gaming!
```

This manual provides a comprehensive guide for users to understand the Pawn Game application, its functionality, and how to get started.