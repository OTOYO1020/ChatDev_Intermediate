Here's a detailed user manual for the product calculator software, formatted in Markdown as requested:

```markdown
# Product Calculator

A simple application to compute the K-th smallest product of unique pairs from an array of integers.

## Main Functions

The Product Calculator provides the following main functionalities:

- **Input Handling**: Reads integers N (length of the array) and K (position of the smallest product) from the user.
- **Product Calculation**: Computes the product of all unique pairs of integers in the provided array.
- **Sorting and Retrieval**: Sorts the computed products and retrieves the K-th smallest product based on 1-based indexing.
- **Error Handling**: Provides user-friendly error messages for invalid inputs.

## Installation

To run the Product Calculator, ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

This application does not require any external libraries beyond the standard Python library. Simply ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: If you have the source code, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file.

   ```bash
   python main.py
   ```

3. **Input Prompts**: Follow the prompts in the terminal:
   - Enter the value for N (the length of the array). Ensure it is a positive integer of at least 2.
   - Enter the value for K (the position of the smallest product). Ensure it is a positive integer.
   - Enter the array elements as space-separated non-negative integers.

4. **Output**: The application will compute and display the K-th smallest product of the unique pairs.

### Example Usage

```plaintext
Enter N (length of array): 5
Enter K (position of smallest product): 3
Enter array elements (space-separated, non-negative integers only): 1 2 3 4 5
K-th smallest product: 6
```

## Error Handling

The application includes error handling for various input scenarios:

- If N is less than 2, an error message will prompt the user to enter a valid number.
- If K is less than or equal to 0, an error message will indicate that K must be a positive integer.
- If the length of the array does not match N, an error message will inform the user of the mismatch.
- If any array element is negative or not an integer, the application will prompt the user to enter valid non-negative integers.
- If K is out of bounds (greater than the number of products), an error message will be displayed.

## Conclusion

The Product Calculator is a straightforward tool for calculating the K-th smallest product from an array of integers. With its user-friendly interface and error handling, it is designed to be accessible for users of all levels.

For any further questions or support, please contact the development team.
```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, usage guidelines, and error handling. It should help users effectively utilize the Product Calculator.