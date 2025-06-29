Here is the `manual.md` file for the Knight Ways Calculator software, detailing its main functions, installation instructions, and usage guidelines.

```markdown
# Knight Ways Calculator

Calculate the number of ways a knight can reach a specific square on a chessboard.

## Overview

The Knight Ways Calculator is a Python application that allows users to determine the number of distinct paths a knight can take to reach a given square (X, Y) on a chessboard starting from the position (0, 0). The knight moves in an "L" shape, and the application efficiently computes the number of ways to reach the target square using dynamic programming.

## Main Functions

- **countKnightWays(X: int, Y: int) -> int**: This function calculates the number of ways a knight can reach the square (X, Y) from the starting position (0, 0). It utilizes a dynamic programming approach to store intermediate results and ensure efficient computation.

## Installation

To run the Knight Ways Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Download or clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not have any external dependencies at this time, so you can run it directly without installing additional packages. However, if you want to create a virtual environment, you can do so with the following commands:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Run the Application**: You can run the application by executing the `main.py` file.

   ```bash
   python main.py
   ```

## Usage

1. **Input**: When prompted, enter the X and Y coordinates of the square you want to reach. Both values should be non-negative integers.

   ```
   Enter X coordinate: 3
   Enter Y coordinate: 2
   ```

2. **Output**: The application will calculate and display the number of ways the knight can reach the specified square.

   ```
   Ways to reach (3, 2): 4
   ```

3. **Error Handling**: If you enter invalid input (non-integer values), the application will prompt you to enter valid integers.

   ```
   Please enter valid integers.
   ```

## Example

To find the number of ways a knight can reach the square (3, 2):

1. Start the application.
2. Input `3` for X and `2` for Y.
3. The output will show the number of ways to reach (3, 2).

## Conclusion

The Knight Ways Calculator is a simple yet powerful tool for exploring knight moves on a chessboard. Whether you're a chess enthusiast or a programmer looking to understand dynamic programming, this application provides a clear and efficient solution to the problem of counting knight paths.

For further inquiries or support, please contact the development team.
```

This manual provides a comprehensive guide for users to understand the functionality of the Knight Ways Calculator, how to set it up, and how to use it effectively.