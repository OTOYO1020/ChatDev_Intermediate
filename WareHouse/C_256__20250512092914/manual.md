Here's a detailed user manual for the Grid Counter application, formatted in Markdown:

```markdown
# Grid Counter

Count valid configurations of a 3x3 grid based on specified row and column sums.

## Overview

The Grid Counter application allows users to find the number of valid configurations for a 3x3 grid where the sum of each row and column meets specified criteria. This is useful for various applications in combinatorial mathematics and grid-based puzzles.

## Main Functions

- **Input Parsing**: The application prompts the user to enter six integers representing the sums of the rows and columns.
- **Validation**: Ensures that all input integers are within the range of [3, 30].
- **Grid Configuration Counting**: Uses a recursive algorithm to count valid configurations that satisfy the given row and column sums.
- **Output**: Displays the total number of valid configurations.

## Installation

To run the Grid Counter application, ensure you have Python installed on your machine. You can install the required dependencies using pip. 

1. Open your terminal or command prompt.
2. Run the following command to install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   *(Note: If there are no specific dependencies, you can skip this step.)*

## How to Use the Application

1. **Run the Application**: Execute the `main.py` file in your terminal or command prompt:

   ```bash
   python main.py
   ```

2. **Input Row and Column Sums**: When prompted, enter the values for the row sums (`h1`, `h2`, `h3`) and column sums (`w1`, `w2`, `w3`). Ensure that all values are integers within the range of 3 to 30.

   Example Input:
   ```
   Enter Row sum 1 (h1): 10
   Enter Row sum 2 (h2): 15
   Enter Row sum 3 (h3): 20
   Enter Column sum 1 (w1): 15
   Enter Column sum 2 (w2): 15
   Enter Column sum 3 (w3): 15
   ```

3. **View Results**: After entering the sums, the application will calculate and display the number of valid configurations that satisfy the specified conditions.

   Example Output:
   ```
   Valid configurations: 5
   ```

## Edge Cases

- If any of the input integers are outside the range of [3, 30], the application will return `0` valid configurations.
- If no valid configurations exist for the provided sums, the application will also return `0`.

## Testing the Function

You can test the function with various input scenarios to ensure correctness. Consider edge cases such as:
- All sums being equal.
- Maximum and minimum values within the allowed range.
- Cases where no valid configuration is possible.

## Conclusion

The Grid Counter application is a powerful tool for counting valid grid configurations based on specified row and column sums. By following the instructions above, users can easily install and run the application to explore various grid configurations.

For further questions or support, please contact the development team.
```

This manual provides a comprehensive guide for users to understand, install, and utilize the Grid Counter application effectively.