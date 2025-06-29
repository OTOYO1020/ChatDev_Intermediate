Here's a detailed user manual for the Median Calculator software, formatted in Markdown as requested:

```markdown
# Median Calculator

A software application to calculate distinct median values based on input ranges.

## Quick Install

To run the Median Calculator, ensure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

The Median Calculator allows users to input a number of integers along with their respective lower and upper bounds. It calculates the distinct median values that can be formed from the specified ranges. This tool is particularly useful for statistical analysis and data processing tasks.

## Main Functions

### `count_median_values(N: int, A: List[int], B: List[int]) -> int`

- **Parameters:**
  - `N`: An integer representing the number of integers (2 ≤ N ≤ 200000).
  - `A`: A list of integers representing the lower bounds (1 ≤ A_i ≤ B_i ≤ 10^9).
  - `B`: A list of integers representing the upper bounds (1 ≤ A_i ≤ B_i ≤ 10^9).

- **Returns:** 
  - An integer representing the count of distinct median values that can be formed from the ranges defined by A and B.

- **Functionality:**
  - Validates input constraints.
  - Sorts the lists A and B.
  - Calculates possible median values based on the sorted lists.
  - Returns the count of distinct median values.

## How to Use

1. **Run the Application:**
   Execute the main script to start the application:

   ```bash
   python main.py
   ```

2. **Input Parameters:**
   - You will be prompted to enter the integer `N`, followed by the lists `A` and `B`.
   - Enter the values for `A` and `B` as comma-separated integers.

   Example Input:
   ```
   Enter N: 5
   Enter list A (comma-separated): 1,2,3,4,5
   Enter list B (comma-separated): 5,6,7,8,9
   ```

3. **Output:**
   - The application will output the count of distinct median values based on the provided input.

   Example Output:
   ```
   Distinct Median Values Count: 4
   ```

## Error Handling

The application includes error handling for various input scenarios:
- If the length of lists A and B does not match N, an error message will be displayed.
- If any of the values in A or B do not meet the specified constraints, an appropriate error message will be shown.

## Example Usage

To see the application in action, you can use the following example:

```bash
python main.py
```

Input:
```
Enter N: 4
Enter list A (comma-separated): 1,2,3,4
Enter list B (comma-separated): 4,5,6,7
```

Output:
```
Distinct Median Values Count: 3
```

## Conclusion

The Median Calculator is a powerful tool for calculating distinct median values from specified ranges. By following the instructions above, users can easily install and utilize the software for their statistical needs.
```

This manual provides a comprehensive overview of the Median Calculator, including installation instructions, main functions, usage guidelines, and error handling. It should serve as a useful resource for users looking to understand and operate the software effectively.