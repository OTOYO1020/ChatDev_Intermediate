Here's a detailed user manual for the grid lighting application, formatted in Markdown as requested:

```markdown
# Grid Lighting Application

A Python application designed to calculate the maximum number of squares that can be lighted by placing a lamp optimally on a grid layout.

## Overview

This application allows users to input a grid layout consisting of obstacles and empty squares. The program calculates how many squares can be illuminated from each position in the grid and determines the optimal placement of a lamp to maximize the number of lighted squares.

## Main Functions

1. **Input Handling**: 
   - Reads the dimensions of the grid (H x W).
   - Accepts H strings representing the grid layout, where `#` indicates an obstacle and `.` indicates an empty square.

2. **Light Count Calculation**:
   - Computes the number of squares that can be lighted from each position in the grid, considering both horizontal and vertical lighting.

3. **Maximum Lighted Squares**:
   - Determines the maximum number of squares that can be lighted by placing a lamp optimally on the grid.

4. **Error Handling**:
   - Validates user input to ensure grid dimensions and characters are correct.

## Installation

To run the Grid Lighting Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have the source code in a repository, clone it using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: This application does not require any external libraries beyond Python's standard library. Ensure you have Python installed correctly.

## How to Use the Application

1. **Run the Application**:
   - Open your terminal or command prompt.
   - Navigate to the directory where `main.py` is located.
   - Execute the following command:
     ```bash
     python main.py
     ```

2. **Input the Grid Dimensions**:
   - When prompted, enter the grid dimensions in the format `H W` (e.g., `3 4` for a grid with 3 rows and 4 columns).

3. **Input the Grid Layout**:
   - For each row, enter a string of length W consisting of `#` and `.` characters. For example:
     ```
     Enter row 1 of the grid layout: #..#
     Enter row 2 of the grid layout: .##.
     Enter row 3 of the grid layout: ..#.
     ```

4. **View the Result**:
   - After entering the grid layout, the application will process the input and output the maximum number of lighted squares. For example:
     ```
     Max Lighted Squares: 5
     ```

## Error Handling

- If you enter invalid dimensions (non-positive integers), the application will prompt you to enter valid positive integers.
- If the rows do not match the specified width, an error message will be displayed.
- The application will also check for invalid characters in the grid layout and notify you accordingly.

## Conclusion

The Grid Lighting Application is a simple yet effective tool for determining optimal lamp placement in a grid layout. By following the instructions above, users can easily set up and utilize the application to solve grid lighting challenges.

For any further questions or support, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand the application, its functionalities, installation steps, and usage instructions.