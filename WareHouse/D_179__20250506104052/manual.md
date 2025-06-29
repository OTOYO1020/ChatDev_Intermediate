Here's a detailed user manual for the software based on the provided code and requirements:

```markdown
# Segment Calculator

A Python application for calculating the number of ways to reach a specific cell in a sequence based on defined segments.

## Overview

The Segment Calculator allows users to input a total number of cells (N) and a number of non-intersecting segments (K). It computes the number of ways to reach the last cell (Cell N) using the defined segments. This application is useful for problems involving dynamic programming and combinatorial counting.

## Main Functions

- **Input Handling**: Reads integers N and K from standard input, followed by K segments defined by their endpoints (L_i, R_i).
- **Segment Validation**: Ensures that segments are non-intersecting and within the bounds of N.
- **Dynamic Programming Calculation**: Computes the number of ways to reach Cell N using the defined segments.
- **Output**: Prints the total number of ways to reach Cell N modulo 998244353.

## Installation

To run the Segment Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted on a version control system like Git, clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not have external dependencies beyond Python's standard library. Ensure you have the latest version of Python.

## How to Use

1. **Run the Application**: Open your terminal and navigate to the directory where the `main.py` file is located. Run the application using:
   ```bash
   python main.py
   ```

2. **Input Format**: When prompted, enter the values for N and K, followed by K pairs of integers representing the segments. For example:
   ```
   5 2
   1 2
   3 4
   ```

   This input means there are 5 cells and 2 segments: the first segment covers cells 1 to 2, and the second segment covers cells 3 to 4.

3. **Output**: After entering the input, the application will calculate and print the number of ways to reach Cell N based on the defined segments.

## Example

### Input
```
5 2
1 2
3 4
```

### Output
```
2
```

This output indicates that there are 2 distinct ways to reach Cell 5 using the provided segments.

## Error Handling

The application includes error handling for the following scenarios:
- Invalid input for N and K (must be integers).
- Segments that are out of bounds.
- Intersecting segments.
- Invalid segment definitions.

If any errors occur, the application will print an appropriate error message and terminate.

## Conclusion

The Segment Calculator is a powerful tool for solving combinatorial problems involving segments and paths. By following the instructions above, users can easily set up and utilize the application for their specific needs.

For further assistance or to report issues, please contact the development team.
```

This manual provides a comprehensive guide for users to understand the functionality, installation, and usage of the Segment Calculator application.