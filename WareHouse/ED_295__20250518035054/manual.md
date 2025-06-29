Here's a detailed user manual for the software that implements the `expected_value` function. This manual will guide users on how to install the necessary dependencies, understand the main functions of the software, and how to use it effectively.

```markdown
# Expected Value Calculator

A Python application for calculating the expected value of a list of integers based on user-defined parameters.

## Overview

The `expected_value` function computes the expected value of the K-th element in a sorted list of integers, where zeros in the list are replaced by uniformly random integers between 1 and M. The result is returned as an integer R, satisfying the condition \( R \cdot Q \equiv P \mod 998244353 \).

## Main Functions

- **Input Parsing**: The application takes a list of integers, an index K, and a maximum integer value M from the user.
- **Expected Value Calculation**: The function calculates the expected value of the K-th element after sorting the modified list.
- **Modular Arithmetic**: The result is computed using modular arithmetic to ensure it fits within the specified bounds.

## Installation

To run the application, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

This application requires no external libraries beyond the standard Python library. However, ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: If you have the source code, clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Open your terminal or command prompt and navigate to the directory containing `main.py`. Run the application using:
   ```bash
   python main.py
   ```

3. **Input Data**: When prompted, enter the following:
   - A list of integers (comma-separated), e.g., `0, 2, 0, 4, 5`.
   - The index K (1-based), e.g., `3`.
   - The maximum integer value M, e.g., `10`.

4. **View Results**: After entering the inputs, the application will calculate and display the result.

### Example Usage

```plaintext
Enter a list of integers (comma-separated): 0, 2, 0, 4, 5
Enter the index K (1-based): 3
Enter the maximum integer value M: 10
Result: <calculated_value>
```

## Error Handling

The application includes basic error handling for the following scenarios:
- If K is not within the valid range (1 to length of A).
- If M is not a positive integer.

## Testing

To ensure the correctness and performance of the function, you can test it with various inputs. Consider edge cases such as:
- All elements being zero.
- K being equal to the length of the list.
- Large values for M.

## Conclusion

This application provides a straightforward way to calculate expected values based on user-defined parameters. For any issues or feature requests, please reach out to the development team.

```

This manual provides a comprehensive guide for users to understand and utilize the software effectively. It covers installation, usage, and error handling, ensuring that users can navigate the application with ease.