Here's the user manual for the Atcoder swap calculator software, formatted in Markdown:

```markdown
# Atcoder Swap Calculator

Calculate the minimum number of adjacent swaps needed to transform a string into 'atcoder'.

## Overview

The Atcoder Swap Calculator is a utility that helps you determine how many adjacent swaps are required to rearrange a given permutation of the string 'atcoder' back into its original order. This tool is particularly useful for understanding string manipulation and permutation problems.

## Main Functions

- **`min_operations_to_atcoder(S: str) -> int`**: This function calculates the minimum number of adjacent swaps needed to transform the string `S` into 'atcoder'. It validates that `S` is a permutation of 'atcoder' and returns -1 if it is not.

- **`count_inversions(S: str) -> int`**: This helper function counts the number of inversions in the string `S`, which is used to determine the number of swaps needed.

## Installation

To run the Atcoder Swap Calculator, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install required packages**:
   You can install any required dependencies using pip. If there are specific dependencies, they should be listed in a `requirements.txt` file. For this project, no additional packages are required beyond Python's standard library.

   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. **Run the main application**:
   Execute the `main.py` file to start the application. You can do this from your terminal or command prompt:
   ```bash
   python main.py
   ```

2. **Input a permutation of 'atcoder'**:
   When prompted, enter a valid permutation of the string 'atcoder'. For example:
   ```
   Enter a permutation of 'atcoder': ocatder
   ```

3. **View the result**:
   The application will output the minimum number of swaps needed to transform the input string into 'atcoder'. If the input is not a valid permutation, it will display an error message.

   Example output:
   ```
   Minimum swaps needed: 3
   ```

## Testing

You can test the function with various permutations of 'atcoder' to ensure correctness and efficiency. Here are some examples:

- Input: `atcoder` → Output: `0`
- Input: `atcodre` → Output: `1`
- Input: `ratcoder` → Output: `Error: Input is not a valid permutation of 'atcoder'.`

## Conclusion

The Atcoder Swap Calculator is a straightforward tool for calculating the number of adjacent swaps needed to rearrange a string. It is designed to be user-friendly and efficient, making it suitable for both educational and practical applications in string manipulation.

For further assistance or inquiries, please contact the development team.
```

This manual provides a comprehensive guide for users to understand, install, and utilize the Atcoder Swap Calculator effectively.