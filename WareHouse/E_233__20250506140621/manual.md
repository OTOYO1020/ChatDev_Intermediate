Here's a detailed user manual for the software based on the provided task and code structure. This manual will guide users on how to install the necessary dependencies, understand the main functions of the software, and how to use it effectively.

```markdown
# Cumulative Floor Value Calculator

A Python application designed to calculate the cumulative sum of floor values based on user-provided integer input.

## Main Functions

The Cumulative Floor Value Calculator performs the following main functions:

1. **Input Validation**: Ensures that the input integer \(X\) falls within the specified range \(1 \leq X < 10^{500000}\).
2. **Cumulative Calculation**: Computes the cumulative sum of floor values derived from the powers of 10 until \(10^k\) exceeds \(X\).
3. **Output**: Displays the total cumulative sum to the user.

## Quick Install

To run the application, ensure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

*Note: Currently, there are no external dependencies required beyond Python itself.*

## How to Use

1. **Run the Application**: Execute the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Prompt**: You will be prompted to enter an integer \(X\). Make sure that your input meets the following criteria:
   - It must be a positive integer.
   - It must be less than \(10^{500000}\).
   - It must be at least 1.

3. **View Output**: After entering a valid integer, the application will calculate and display the cumulative sum of the floor values based on the powers of 10.

### Example Usage

```plaintext
Enter an integer X (1 ≤ X < 10^500000): 12345
Total Sum: 12345 + 1234 + 123 + 12 + 1 = 13615
```

## Error Handling

If the input does not meet the specified criteria, the application will return an error message. For example:

```plaintext
Input Error: X must be in the range 1 ≤ X.
```

## Code Structure

The application consists of two main files:

- **main.py**: The entry point for user interaction. It handles input validation and invokes the calculation logic.
- **calculator.py**: Contains the `Calculator` class that implements the logic for calculating the cumulative sum of floor values.

## Conclusion

This application provides a straightforward way to calculate the cumulative sum of floor values based on user input. Ensure that your input adheres to the specified constraints for a smooth experience. For any issues or further inquiries, please contact support.

```

This manual provides a comprehensive overview of the software, guiding users through installation, usage, and error handling, while also explaining the code structure for better understanding.