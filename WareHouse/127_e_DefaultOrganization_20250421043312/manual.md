Here's the `manual.md` file for the software that calculates the Manhattan distances based on the provided code:

```markdown
# Manhattan Distance Calculator

A Python application for calculating the sum of Manhattan distances between pairs for all different configurations in which K pieces are placed on an N x M grid.

## Quick Install

To run the application, ensure you have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

This software calculates the total Manhattan distance for K pieces placed on an N x M grid. The Manhattan distance is the sum of the absolute differences of their Cartesian coordinates. The application efficiently computes the distances by precalculating combinations and using modular arithmetic to handle large numbers.

### Main Functions

1. **Input Handling**: The application receives integers N (number of rows), M (number of columns), and K (number of pieces) from standard input.

2. **Combination Calculation**: It precalculates the factorials and their modular inverses to efficiently compute combinations C(n, k) in O(1) time.

3. **Distance Calculation**:
   - **Row Direction**: Calculates the sum of distances for all pairs in the same row.
   - **Column Direction**: Calculates the sum of distances for all pairs in the same column.
   - Combines the results from both directions to provide the total Manhattan distance.

4. **Output**: The application outputs the total Manhattan distance modulo \(10^9 + 7\).

## 📖 How to Use

1. **Run the Application**: Execute the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Values**: When prompted, enter the values for N, M, and K. For example:
   ```
   Please enter the number of rows (N): 3
   Please enter the number of columns (M): 3
   Please enter the number of pieces (K): 2
   ```

3. **View Results**: After entering the values, the application will calculate and display the total Manhattan distance:
   ```
   Total Manhattan Distance: <result>
   ```

## Example

To calculate the Manhattan distance for a 3x3 grid with 2 pieces:

1. Run the application.
2. Input:
   ```
   Please enter the number of rows (N): 3
   Please enter the number of columns (M): 3
   Please enter the number of pieces (K): 2
   ```
3. Output:
   ```
   Total Manhattan Distance: <calculated_value>
   ```

## Dependencies

Ensure you have the following dependencies installed:

- Python 3.x
- Any additional libraries specified in `requirements.txt` (if applicable).

## Support

For any issues or questions, please contact our support team or refer to the documentation for further assistance.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage, and examples to help users effectively utilize the Manhattan Distance Calculator.