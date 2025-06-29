```markdown
# Score Calculator

A Python application designed to calculate the minimum score needed in the final round of a scoring system based on previous rounds' scores.

## Main Functions

The Score Calculator performs the following key functions:

1. **Input Validation**: Ensures that the input values for the number of rounds (N), minimum final grade (X), and scores are within specified constraints.
2. **Score Calculation**: Computes the minimum score required in the final round to achieve the desired final grade based on the scores from previous rounds.
3. **Output Results**: Displays the minimum score needed or indicates if achieving the required grade is impossible.

## Installation

To run the Score Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the Score Calculator code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: If there are any additional dependencies, install them using pip. For this application, no external libraries are required beyond Python's standard library.

## How to Use the Score Calculator

1. **Run the Application**: Open your terminal or command prompt, navigate to the directory where the `main.py` file is located, and run the following command:
   ```bash
   python main.py
   ```

2. **Input Format**: The application expects input in the following format:
   - The first line should contain two integers, N (number of rounds) and X (minimum final grade), separated by a space.
   - The second line should contain N-1 integers representing the scores for the first N-1 rounds, separated by spaces.

   **Example Input**:
   ```
   5 250
   80 90 70 85
   ```

3. **Output**: After entering the input, the application will calculate and print the minimum score needed in the final round. If it is impossible to achieve the required grade, it will print a corresponding message.

   **Example Output**:
   ```
   95
   ```

## Edge Cases Handled

- The application checks for cases where all scores are the same and determines if achieving the required grade is possible.
- It validates inputs to ensure they meet the specified constraints:
  - 3 ≤ N ≤ 100
  - 0 ≤ X ≤ 100 × (N-2)
  - 0 ≤ A_i ≤ 100

## Conclusion

The Score Calculator is a straightforward tool for determining the minimum score needed in a scoring system. By following the installation and usage instructions, you can easily run the application and calculate scores based on your input.

For any issues or further assistance, please refer to the documentation or contact support.
```