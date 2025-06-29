Here's a detailed user manual for the software you developed, formatted in Markdown as requested:

```markdown
# Permutation Finder

A Python application to find the previous permutation in lexicographical order based on a given permutation list.

## Introduction

The Permutation Finder is designed to help users identify the (K-1)-th permutation from a sorted list of all permutations of integers from 1 to N. This application is particularly useful for combinatorial problems and can be utilized in various scenarios where permutations are involved.

## Main Functions

- **find_previous_permutation(N: int, P: List[int], K: int) -> List[int]**: 
  - This function takes three parameters:
    - `N`: The size of the permutation.
    - `P`: The permutation list.
    - `K`: The index of the permutation.
  - It validates the input, generates all permutations, sorts them, and retrieves the (K-1)-th permutation.

## Installation

To run the Permutation Finder, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

1. **Install Python**: Ensure you have Python 3.6 or higher.
2. **Install Required Libraries**: You can install the necessary libraries using pip. Open your terminal or command prompt and run:

   ```bash
   pip install itertools
   ```

## How to Use

1. **Clone the Repository**: If you haven't already, clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Prepare Input**: The application reads input from standard input. You need to provide the following:
   - The first line should contain the integer `N` (size of the permutation).
   - The second line should contain the integer `K` (index of the permutation).
   - The third line should contain the permutation list `P`, formatted as a comma-separated string (e.g., `3,1,2`).

3. **Run the Application**: You can run the application using the command line. Make sure you are in the directory where `main.py` is located. Execute the following command:

   ```bash
   python main.py
   ```

4. **Input Example**: When prompted, provide the input in the following format:

   ```
   3
   2
   3,1,2
   ```

   This input indicates that you are looking for the previous permutation of the list `[3, 1, 2]` in a set of permutations of size 3.

5. **Output**: The application will output the (K-1)-th permutation as a list of integers. If the input is invalid, it will display an error message.

## Error Handling

The application includes error handling for various scenarios:
- If `N` is not between 2 and 100.
- If `P` does not contain unique integers within the range 1 to N.
- If `P` is the identity permutation.
- If `K` is out of bounds for the number of permutations.
- If `P` is not a valid permutation.

## Conclusion

The Permutation Finder is a powerful tool for working with permutations in Python. By following the instructions above, you can easily set up and use the application to find previous permutations based on your input.

For further inquiries or support, please contact the development team.
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and error handling. Let me know if you need any further modifications or additional information!