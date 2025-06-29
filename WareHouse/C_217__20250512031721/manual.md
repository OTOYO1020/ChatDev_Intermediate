Here’s a detailed user manual for the Permutation Calculator software, formatted in Markdown as requested:

```markdown
# Permutation Calculator

A simple application to compute the permutation of a list of integers based on user input.

## Main Functions

The Permutation Calculator provides the following main functionalities:

- **Input Handling**: Prompts the user to enter an integer N and a list of integers P.
- **Validation**: Checks if the input list P is a valid permutation of integers from 1 to N.
- **Permutation Calculation**: Computes a new list Q based on the input list P, where each index corresponds to the position of integers in the permutation.
- **Output Handling**: Displays the resulting list Q as space-separated integers.

## Quick Install

To run the Permutation Calculator, you need to have Python installed on your machine. You can install the necessary dependencies using pip. 

```bash
pip install -r requirements.txt
```

Make sure you have the following dependencies in your `requirements.txt` file:

```
# requirements.txt
# Add any required libraries here
```

## How to Use

1. **Run the Application**: Execute the main application file `main.py` in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Values**: When prompted, enter the integer N (the size of the permutation) and the list P (space-separated integers).

   Example Input:
   ```
   Enter N: 5
   Enter P (space-separated): 3 1 4 5 2
   ```

3. **Validation**: The application will validate the input. If the input is invalid, an error message will be displayed.

4. **Output**: If the input is valid, the application will compute the permutation and display the result.

   Example Output:
   ```
   Result: 2 5 1 3 4
   ```

## Error Handling

The application includes error handling for the following scenarios:

- N must be greater than 0.
- P cannot be empty.
- The length of P must be equal to N.
- P must contain unique integers.
- All elements in P must be between 1 and N.
- P must be a valid permutation of integers from 1 to N.

If any of these conditions are not met, an appropriate error message will be displayed.

## Testing

The application has been tested with various edge cases, including:

- Minimum value of N (1).
- Maximum value of N (up to system limits).
- Valid and invalid permutations.

Feel free to test the application with different inputs to ensure its correctness and robustness.

## Documentation

For further details on the code structure and functions, refer to the source code in `permutation.py` and `main.py`. The code is well-documented with comments explaining the purpose of each function and its parameters.

---

Thank you for using the Permutation Calculator! We hope it meets your needs for computing permutations efficiently.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and error handling, ensuring users can effectively utilize the Permutation Calculator.