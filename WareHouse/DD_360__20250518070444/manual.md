Here's a detailed user manual for the Ant Passing Pairs Calculator software, formatted in Markdown:

```markdown
# Ant Passing Pairs Calculator

A simple application to calculate the number of passing pairs of ants based on their initial positions and directions.

## Overview

The Ant Passing Pairs Calculator allows users to input the number of ants, the time they move, their initial directions, and their starting positions. The application then calculates how many pairs of ants pass each other based on their final positions after a specified time.

## Main Functions

- **Input Parsing**: Accepts user input for the number of ants (N), time (T), direction string (S), and positions (X).
- **Final Position Calculation**: Computes the final position of each ant after moving for time `T + 0.1`.
- **Passing Pair Counting**: Counts the number of pairs of ants that pass each other based on their final positions and initial directions.
- **Error Handling**: Validates input to ensure correctness and provides user-friendly error messages.

## Installation

To run the Ant Passing Pairs Calculator, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

The application uses the Tkinter library for the GUI, which is included with most Python installations. If you encounter any issues, ensure you have Tkinter installed.

## How to Use

1. **Run the Application**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the `main.py` file is located.
   - Run the application using the command:
     ```bash
     python main.py
     ```

2. **Input Data**:
   - In the application window, you will see a text entry field.
   - Enter the values for N, T, S, and X in the following format:
     ```
     N, T, S, X1, X2, ..., XN
     ```
     - **N**: Number of ants (an integer greater than 0).
     - **T**: Time (a float).
     - **S**: A binary string of length N (e.g., "0101").
     - **X**: A list of distinct integers representing the initial positions of the ants (e.g., "1, 3, 2, 4").

3. **Calculate Passing Pairs**:
   - Click the "Calculate Passing Pairs" button.
   - The result will be displayed in the text area below the button.

4. **Error Handling**:
   - If the input is invalid, an error message will be displayed in the text area, indicating what went wrong (e.g., "N must be greater than zero.").

## Example Input

To calculate the passing pairs for 4 ants with the following parameters:
- N = 4
- T = 2.5
- S = "0101"
- X = [1, 3, 2, 4]

You would enter:
```
4, 2.5, 0101, 1, 3, 2, 4
```

## Conclusion

The Ant Passing Pairs Calculator is a straightforward tool for analyzing the movement of ants based on their initial positions and directions. With its user-friendly interface and robust error handling, it provides an efficient way to calculate passing pairs.

For further assistance or feedback, please contact the development team.
```

This manual provides a comprehensive guide for users to understand and utilize the Ant Passing Pairs Calculator effectively.