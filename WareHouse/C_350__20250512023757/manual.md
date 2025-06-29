Here's a detailed user manual for the permutation sorter application, formatted in Markdown as requested:

```markdown
# Permutation Sorter

A simple application to sort permutations of integers using a selection sort algorithm with pair swapping.

## Main Functions

The Permutation Sorter application provides the following main functionalities:

- **Input Handling**: Reads the size of the permutation and the permutation list from standard input.
- **Validation**: Verifies that the input list is a valid permutation of integers from `1` to `N`.
- **Sorting**: Sorts the permutation into the ordered sequence `(1, 2, ..., N)` using a selection sort algorithm.
- **Output**: Returns the sorted permutation as a list of integers.

## Installation

To run the Permutation Sorter application, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

You may need to install the following dependencies:

```bash
pip install typing
```

## How to Use the Application

1. **Clone the Repository**: If you haven't already, clone the repository containing the application code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the `main.py` file to start the application.

   ```bash
   python main.py
   ```

3. **Input the Data**: When prompted, enter the size of the permutation (N) and the permutation itself as space-separated integers. For example:

   ```
   Enter the size of the permutation (N): 5
   Enter the permutation (space-separated): 3 1 4 5 2
   ```

4. **View the Output**: The application will process the input and output the sorted permutation.

   ```
   Sorted Permutation: [1, 2, 3, 4, 5]
   ```

## Error Handling

The application includes error handling for the following scenarios:

- If `N` is not a positive integer, an error message will be displayed.
- If the permutation list `A` is not a valid permutation of integers from `1` to `N`, an error message will be displayed.

## Example Usage

Here’s an example of how to use the application:

1. Start the application:

   ```bash
   python main.py
   ```

2. Input example:

   ```
   Enter the size of the permutation (N): 4
   Enter the permutation (space-separated): 4 3 2 1
   ```

3. Output:

   ```
   Sorted Permutation: [1, 2, 3, 4]
   ```

## Conclusion

The Permutation Sorter application is a straightforward tool for sorting permutations of integers. It is designed to be user-friendly and provides clear error messages for invalid input. Enjoy using the application to sort your permutations!
```

This manual provides a comprehensive guide for users to understand the functionality of the Permutation Sorter application, how to install it, and how to use it effectively.