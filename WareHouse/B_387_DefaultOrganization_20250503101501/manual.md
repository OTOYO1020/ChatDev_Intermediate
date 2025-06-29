Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Product Sum Calculator

A simple application to calculate the sum of products of two numbers from 1 to 9, excluding a specified product.

## Overview

The Product Sum Calculator allows users to input an integer \( X \) and calculates the total sum of all products \( i \times j \) (where \( i \) and \( j \) range from 1 to 9) that are not equal to \( X \). This application is designed for educational purposes and to demonstrate basic programming concepts in Python.

## Main Functions

- **Input Handling**: The application prompts the user to enter an integer \( X \) and validates the input to ensure it is a product of two numbers between 1 and 9.
- **Calculation**: It calculates the total sum of products \( i \times j \) for \( i, j \) in the range of 1 to 9, excluding the product equal to \( X \).
- **Output**: Displays the total sum after the calculations are complete.

## Installation

To run the Product Sum Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/). Ensure that you check the box to add Python to your PATH during installation.

2. **Clone the Repository**: If you have the source code in a repository, clone it using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not require any additional dependencies beyond Python itself. You can run the application directly after installation.

## How to Use the Application

1. **Run the Application**: Open your terminal or command prompt, navigate to the directory where `main.py` is located, and run the following command:
   ```bash
   python main.py
   ```

2. **Input Prompt**: The application will prompt you to enter an integer \( X \). Make sure to enter a valid product of two numbers between 1 and 9 (valid range: 1 to 81). For example, you can enter `6` (which is the product of `2` and `3`).

3. **View Results**: After entering a valid integer, the application will calculate the total sum of all products \( i \times j \) that are not equal to \( X \) and display the result in the terminal.

## Example Usage

- **Input**: 
  ```
  Enter an integer (X) that is a product of two numbers between 1 and 9 (valid range: 1 to 81, e.g., 6 for 2*3): 6
  ```
- **Output**: 
  ```
  Total Sum: 396
  ```

## Troubleshooting

- **Invalid Input**: If you enter a number outside the valid range (1 to 81) or a number that is not a product of two numbers between 1 and 9, the application will prompt you to enter a valid integer again.
- **ValueError**: If you enter a non-integer value, the application will notify you and ask for a valid integer input.

## Conclusion

The Product Sum Calculator is a straightforward application that helps users understand basic multiplication and summation concepts through interactive input and output. Feel free to modify the code to enhance its functionality or adapt it for educational purposes.
```

This manual provides a comprehensive guide for users to understand the purpose of the application, how to install it, and how to use it effectively.