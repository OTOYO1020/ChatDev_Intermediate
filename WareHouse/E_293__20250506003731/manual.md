Here’s a detailed user manual for the Sum Calculator application, formatted in Markdown:

```markdown
# Sum Calculator

A simple application to compute the cumulative sum of powers of a given integer.

## Overview

The Sum Calculator allows users to input three integers: A, X, and M. It computes the sum of A raised to the power of i (where i ranges from 0 to X-1) and takes the result modulo M. This application is useful for mathematical computations involving powers and modular arithmetic.

## Main Functions

- **Input Handling**: The application prompts the user to enter three integers: A (a positive integer), X (a non-negative integer), and M (a positive integer).
- **Computation**: 
  - If A is equal to 1, it computes the result as `X % M`.
  - If A is greater than 1, it calculates the cumulative sum of A raised to the power of i for i from 0 to X-1, taking modulo M at each step.
- **Output**: The final result is printed to the console.

## Installation

To run the Sum Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have the code in a repository, clone it using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not have any external dependencies beyond Python's standard library. Ensure you have the necessary environment set up.

## How to Use the Application

1. **Run the Application**: Open your terminal or command prompt, navigate to the directory where `main.py` is located, and run:
   ```bash
   python main.py
   ```

2. **Input Values**: The application will prompt you to enter values for A, X, and M. Enter the values as instructed:
   - A: Enter a positive integer (e.g., 2).
   - X: Enter a non-negative integer (e.g., 3).
   - M: Enter a positive integer (e.g., 5).

3. **View the Result**: After entering the values, the application will compute the result and display it in the console.

## Example Usage

```plaintext
Enter a positive integer for A (e.g., 2): 2
Enter a non-negative integer for X (e.g., 3): 3
Enter a positive integer for M (e.g., 5): 5
Result: 3
```

In this example, the application computes the sum of 2^0 + 2^1 + 2^2 = 1 + 2 + 4 = 7, and then takes 7 modulo 5, resulting in 3.

## Error Handling

- If invalid inputs are provided (e.g., non-integer values or out-of-range integers), the application will prompt the user to enter valid integers.
- The application ensures that A is a positive integer, X is a non-negative integer, and M is a positive integer.

## Conclusion

The Sum Calculator is a straightforward tool for performing modular arithmetic involving powers. It is designed to be user-friendly and provides clear prompts for input. For any issues or feature requests, please contact the development team.

```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and examples to help users effectively utilize the Sum Calculator.