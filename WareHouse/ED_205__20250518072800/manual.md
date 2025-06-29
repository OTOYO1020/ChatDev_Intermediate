Here's a detailed user manual for the ball arrangement application, formatted in Markdown as requested:

```markdown
# Ball Arrangement Calculator

Calculate the number of valid arrangements of white and black balls based on specific conditions.

## Overview

The Ball Arrangement Calculator allows users to compute the number of valid arrangements of white and black balls, ensuring that the arrangements meet the condition `w_i <= b_i + K`. This application is designed to be user-friendly and can be accessed via a command-line interface or a graphical user interface (GUI).

## Main Functions

- **Count Valid Arrangements**: The core function `countArrangements(N: int, M: int, K: int) -> int` calculates the number of valid arrangements of `N` white balls and `M` black balls, considering the maximum difference `K`.
- **Input Parsing**: The application reads user input for the number of white balls, black balls, and the maximum difference.
- **Modular Arithmetic**: Results are returned modulo \(10^9 + 7\) to handle large integers efficiently.
- **Edge Case Handling**: The application is designed to handle edge cases, including minimum and maximum values for `N`, `M`, and `K`.

## Installation

To run the Ball Arrangement Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   You can install the required dependencies using pip. Open your terminal and run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   You can run the application using either the command line or the GUI.

   - **Command Line**:
     ```bash
     python main.py
     ```

   - **Graphical User Interface**:
     ```bash
     python gui.py
     ```

## How to Use the Application

### Command Line Interface

1. Run the application using the command line.
2. When prompted, enter the number of white balls (N), black balls (M), and the maximum difference (K) separated by spaces.
   ```
   Enter N, M, K separated by spaces: 3 5 2
   ```
3. The application will display the number of valid arrangements.

### Graphical User Interface

1. Run the GUI application.
2. Enter the number of white balls (N) in the first input field.
3. Enter the number of black balls (M) in the second input field.
4. Enter the maximum difference (K) in the third input field.
5. Click the "Calculate" button.
6. A message box will display the number of valid arrangements.

## Example Usage

- **Example 1**:
  - Input: `N = 3`, `M = 5`, `K = 2`
  - Output: `Valid arrangements: 56`

- **Example 2**:
  - Input: `N = 0`, `M = 0`, `K = 0`
  - Output: `Valid arrangements: 1`

## Testing Edge Cases

The application has been designed to handle various edge cases, including:
- Minimum values: `N = 0`, `M = 0`, `K = 0`
- Maximum values: Test with large integers for `N` and `M` to ensure performance and correctness.

## Conclusion

The Ball Arrangement Calculator is a powerful tool for calculating valid arrangements of balls based on specific conditions. Whether you prefer using the command line or a GUI, the application is designed to be intuitive and efficient.

For any issues or feature requests, please contact the support team.
```

This user manual provides a comprehensive guide for users to understand and utilize the Ball Arrangement Calculator effectively.