Here's a detailed user manual for the Illumination application, formatted in Markdown as requested:

```markdown
# Illumination Application

Illuminate your grid with bulbs while avoiding blocks!

## Overview

The Illumination application allows users to define a grid of specified dimensions and place bulbs and blocks within it. The bulbs illuminate squares in all four directions until they encounter a block or the edge of the grid. This application counts the total number of illuminated squares, ensuring that no square is double-counted.

## Main Functions

- **Grid Creation**: Create a grid based on user-defined height and width.
- **Bulb Placement**: Place bulbs at specified coordinates to illuminate the grid.
- **Block Placement**: Place blocks at specified coordinates to prevent illumination.
- **Illumination Counting**: Count the total number of illuminated squares that are not blocked.

## Installation

To run the Illumination application, ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

The application requires the following Python packages:

- `typing` (included in Python standard library)

You can install any additional dependencies using pip if needed, but the current implementation does not require external libraries.

## How to Use

1. **Clone the Repository**: Download or clone the repository containing the `main.py` and `grid.py` files.

2. **Run the Application**: Open your terminal or command prompt, navigate to the directory containing the files, and run the following command:
   ```bash
   python main.py
   ```

3. **Input Parameters**: The application will prompt you to enter the following:
   - **Height**: The height of the grid (integer).
   - **Width**: The width of the grid (integer).
   - **Bulbs**: Enter the positions of the bulbs in the format `(x,y)` separated by semicolons (e.g., `1,1;2,2`).
   - **Blocks**: Enter the positions of the blocks in the same format (e.g., `1,2;2,3`).

   **Note**: The coordinates are 1-based, meaning the top-left corner of the grid is (1,1).

4. **Output**: After entering the parameters, the application will calculate and display the total number of illuminated squares.

### Example Usage

```
Enter Height: 5
Enter Width: 5
Enter Bulbs (x,y) separated by semicolon: 1,1;2,2
Enter Blocks (x,y) separated by semicolon: 1,2;3,3
Illuminated Squares: 10
```

## Error Handling

- The application will notify you if:
  - The bulb or block positions are out of bounds.
  - Bulb and block positions overlap.
  - Invalid formats are used for input.

## Additional Notes

- Ensure that the bulbs and blocks do not overlap.
- The grid is represented as a 2D list, where each square can be 'empty', 'bulb', or 'block'.
- The illumination logic checks all four directions (up, down, left, right) for each bulb.

For any further questions or issues, please contact the support team.
```

This manual provides a comprehensive guide for users to understand the Illumination application, including installation, usage, and error handling. Let me know if you need any modifications or additional information!