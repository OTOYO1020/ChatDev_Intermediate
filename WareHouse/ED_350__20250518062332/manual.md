Here is the `manual.md` file that provides a detailed user manual for the cost calculator software:

```markdown
# Cost Calculator

A software tool designed to calculate the minimum expected cost based on user-defined parameters.

## Overview

The Cost Calculator allows users to compute the minimum expected cost of operations based on a given integer `N` and other parameters. It utilizes memoization to optimize calculations and provides a user-friendly interface for input.

## Main Functions

- **min_expected_cost(N: int, A: int, X: int, Y: int) -> float**: This function calculates the minimum expected cost based on the operations defined. It takes four integer parameters:
  - `N`: The initial value to be processed (must be greater than 0).
  - `A`: The divisor for the first operation (must be greater than 0).
  - `X`: The cost associated with the die operation (must be non-negative).
  - `Y`: The cost associated with the operation using `A` (must be non-negative).

## Installation

To run the Cost Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Open your terminal or command prompt and run the following command to install any required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Note: If you don't have a `requirements.txt` file, the current implementation does not require any external libraries beyond Python's standard library.

## How to Use

1. **Run the Application**: Navigate to the directory containing the `main.py` file and run the following command:

   ```bash
   python main.py
   ```

2. **Input Parameters**: When prompted, enter four integers separated by spaces:
   - `N`: The initial value (must be greater than 0).
   - `A`: The divisor for the first operation (must be greater than 0).
   - `X`: The cost associated with the die operation (must be non-negative).
   - `Y`: The cost associated with the operation using `A` (must be non-negative).

   Example input:
   ```
   Enter four integers N (N > 0), A (A > 0), X (X >= 0), Y (Y >= 0) separated by spaces: 10 2 1 2
   ```

3. **View Results**: After entering the parameters, the program will compute and display the minimum expected cost formatted to two decimal places.

   Example output:
   ```
   Minimum Expected Cost: 5.00
   ```

## Error Handling

- If the input values do not meet the specified constraints (e.g., `N` or `A` is less than or equal to 0, or `X` or `Y` is negative), the program will raise an error and prompt the user to enter valid values.

## Conclusion

The Cost Calculator is a powerful tool for calculating expected costs based on user-defined parameters. By following the installation and usage instructions, users can easily compute the minimum expected cost for their specific scenarios.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.