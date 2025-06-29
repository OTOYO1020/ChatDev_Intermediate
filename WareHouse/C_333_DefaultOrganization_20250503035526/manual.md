Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Repunit Sum Calculator

A Python application for calculating the N-th smallest sum of three repunit numbers.

## Overview

This application allows users to input an integer N (between 1 and 333) and calculates the N-th smallest integer that can be expressed as the sum of exactly three repunit numbers. A repunit is a number consisting entirely of the digit '1', such as 1, 11, 111, etc.

## Main Functions

1. **Input Handling**: The application reads an integer N from standard input and ensures it is within the range of 1 to 333.
2. **Repunit Generation**: Generates repunit numbers by concatenating the digit '1' up to a specified limit (default is 333).
3. **Unique Sum Calculation**: Computes all unique sums of combinations of three repunits and retrieves the N-th smallest sum.
4. **Error Handling**: Provides informative error messages for invalid inputs or if the requested N-th sum exceeds available unique sums.

## Installation

To run the Repunit Sum Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.x installed. You can install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, the application does not have external dependencies beyond the Python standard library.

## Usage

1. **Run the Application**:
   To start the application, execute the following command in your terminal:
   ```bash
   python main.py
   ```

2. **Input Prompt**:
   You will be prompted to enter an integer N. Please enter a value between 1 and 333 (inclusive).

   ```
   Please enter an integer N (between 1 and 333 inclusive):
   ```

3. **Output**:
   The application will calculate and print the N-th smallest sum of three repunits as a single integer.

   Example output:
   ```
   3
   ```

4. **Error Handling**:
   If you enter a value outside the specified range or an invalid input, the application will display an error message:
   ```
   Input Error: N must be between 1 and 333.
   ```

## Example

To find the 5th smallest sum of three repunits:

1. Run the application.
2. Input `5` when prompted.
3. The application will output the result.

## Conclusion

The Repunit Sum Calculator is a straightforward application that demonstrates the power of Python for mathematical computations involving unique number combinations. Feel free to modify the code for further enhancements or additional features.

For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.