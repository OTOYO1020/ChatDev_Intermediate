```markdown
# Geometric Series Calculator

A simple application to calculate the sum of a geometric series based on user-defined parameters.

## Overview

The Geometric Series Calculator allows users to compute the sum of a geometric series using the formula:

- If \( A > 1 \): 
  \[
  \text{sum} = \frac{A^X - 1}{A - 1} \mod M
  \]
- If \( A = 1 \): 
  \[
  \text{sum} = X \mod M
  \]

This application efficiently handles large values of \( X \) and performs calculations under modulo \( M \).

## Features

- Input handling for parameters \( A \), \( X \), and \( M \).
- Validation of input constraints.
- Efficient computation using modular exponentiation.
- Error handling for invalid inputs and edge cases.
- Outputs the final result to standard output.

## Installation

To run the Geometric Series Calculator, ensure you have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can manually install any necessary libraries (though the current implementation does not require any external libraries beyond Python's standard library).

## Usage

1. **Run the Application**: Execute the main application file `main.py` in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Parameters**: When prompted, enter the values for \( A \), \( X \), and \( M \). Ensure that:
   - \( 1 \leq A, M \leq 10^9 \)
   - \( 1 \leq X \leq 10^{12} \)

3. **View Result**: The application will compute the sum of the geometric series and display the result.

### Example

```plaintext
Enter A: 2
Enter X: 10
Enter M: 1000
Result: 1023
```

## Error Handling

The application includes error handling for:
- Input values that are out of bounds.
- Division by zero when \( A = 1 \) and \( M \) is not coprime with \( A - 1 \).
- General calculation errors.

If an error occurs, a descriptive message will be printed to the console.

## Conclusion

The Geometric Series Calculator is a straightforward tool for computing geometric series sums efficiently. It is designed to handle large inputs and provide accurate results while ensuring user-friendly interactions.

For any issues or feature requests, please contact the development team.
```