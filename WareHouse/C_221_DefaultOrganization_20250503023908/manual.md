Here's a detailed user manual for the software that calculates the maximum product from permutations of digits:

```markdown
# Maximum Product from Permutations

This application calculates the maximum product of two integers formed by splitting the permutations of the digits of a given positive integer \( N \).

## Overview

The software reads an integer \( N \) from standard input, generates all unique permutations of its digits, and evaluates the maximum product of two integers \( A \) and \( B \) formed by splitting these permutations. The integers must not have leading zeros.

## Main Functions

- **Input Handling**: Prompts the user to enter a positive integer and validates the input.
- **Permutation Generation**: Generates all unique permutations of the digits of \( N \).
- **Product Calculation**: Splits each permutation into two non-empty parts, checks for leading zeros, and calculates the product of valid pairs.
- **Maximum Product Evaluation**: Keeps track of the maximum product found during the iterations and displays it.

## Installation

To run this application, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

This application uses the built-in `itertools` library for generating permutations, so no additional dependencies are required. However, ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: If you haven't already, clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the `main.py` file using Python.

   ```bash
   python main.py
   ```

3. **Input a Positive Integer**: When prompted, enter a positive integer without leading zeros. For example, you can enter `123`.

4. **View the Result**: The application will process the input and display the maximum product of valid pairs formed from the permutations of the digits.

   ```
   Max Product: <maximum-product-value>
   ```

## Example Usage

- Input: `123`
- Output: `Max Product: 6` (since 1 * 23 = 23, 2 * 13 = 26, and 3 * 12 = 36, the maximum product is 36)

## Error Handling

- If the input is not a positive integer or has leading zeros, the application will prompt you to enter a valid input again.

## Conclusion

This application provides a straightforward way to explore the mathematical properties of permutations of digits and their products. Feel free to modify the code for further enhancements or to suit your specific needs.

For any issues or feature requests, please contact the development team.

```

This manual provides a comprehensive guide for users to understand and utilize the software effectively.