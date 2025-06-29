Here's a detailed user manual for the probability calculator software, formatted in Markdown as requested:

```markdown
# Probability Calculator

A simple application to calculate the probability based on the doubling of natural numbers.

## Overview

The Probability Calculator allows users to input two natural numbers, N and K, and computes a probability based on how many times each natural number from 1 to N must be doubled until it exceeds K. This application is useful for understanding exponential growth in a straightforward manner.

## Main Functions

- **Input Handling**: The application prompts the user to enter two natural numbers, N and K.
- **Probability Calculation**: For each natural number from 1 to N, the application calculates how many times it must be doubled to exceed K and updates the probability accordingly.
- **Output**: The final probability is printed as a single number.

## Installation

To run the Probability Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have the code in a repository, clone it using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not require any external libraries, but ensure you have Python installed. If you need to manage dependencies in the future, consider using `pip` or `conda`.

## How to Use the Application

1. **Run the Application**: Open your terminal or command prompt, navigate to the directory where `main.py` is located, and run:
   ```bash
   python main.py
   ```

2. **Input Values**: You will be prompted to enter two natural numbers:
   - Enter a natural number for N (the number of iterations).
   - Enter a natural number for K (the threshold for doubling).

3. **View Results**: After entering the values, the application will compute the probability and display it as a single number.

## Example Usage

```
Enter a natural number N: 5
Enter a natural number K: 20
```

Output:
```
0.5
```

## Error Handling

- If you enter a non-natural number or a number less than or equal to zero, the application will prompt you to enter valid natural numbers.

## Conclusion

The Probability Calculator is a straightforward tool for exploring the concept of exponential growth through doubling. Feel free to modify the code to suit your needs or to enhance its functionality.

For any issues or feature requests, please reach out to the development team.
```

This manual provides a comprehensive guide for users to understand how to install and use the Probability Calculator effectively.