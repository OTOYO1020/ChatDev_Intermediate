Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Query Handler Application

A simple application for managing a list of distinct integers through a series of queries.

## Overview

The Query Handler Application allows users to manipulate a list of distinct integers by performing insertion and removal operations based on user-defined queries. The application ensures that the list remains non-empty and contains only distinct elements after each operation.

## Main Functions

1. **Initialization**: The application initializes a list `A` with distinct integers.
2. **Processing Queries**: The application processes a series of queries that can either:
   - Insert a new integer immediately after a specified integer in the list.
   - Remove a specified integer from the list.
3. **Output**: After processing all queries, the application outputs the final state of the list in a string format.

## Installation

To run the Query Handler Application, you need to have Python installed on your system. Follow the steps below to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Install Dependencies**: Open your terminal or command prompt and run the following command to install any required dependencies (if applicable):
   ```bash
   pip install typing
   ```

## How to Use the Application

1. **Clone the Repository**: If you have the code in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Edit the `main.py` File**: Open the `main.py` file to modify the sample input as needed. You can change the values of `N`, `A`, `Q`, and `queries` to test different scenarios.

3. **Run the Application**: Execute the `main.py` file to run the application.
   ```bash
   python main.py
   ```

4. **View the Output**: After running the application, the final state of the list will be printed to the console.

## Example Usage

Here is a sample configuration in the `main.py` file:

```python
N = 5
A = [1, 2, 3, 4, 5]  # Initialize with distinct integers
Q = 3  # Number of queries
queries = [
    (1, 3, 6),  # Insert 6 after 3
    (2, 2),     # Remove 2
    (1, 4, 7)   # Insert 7 after 4
]
```

### Query Format

- **Type 1 Query**: `(1, x, y)` - Insert `y` after `x`.
- **Type 2 Query**: `(2, x)` - Remove `x`.

### Important Notes

- Ensure that the list `A` remains non-empty after each operation.
- All elements in the list must be distinct; attempts to insert duplicate values will be ignored.
- If an element to be removed is the last remaining element in the list, the operation will be skipped to maintain a non-empty list.

## Conclusion

The Query Handler Application is a straightforward tool for managing a list of integers through defined queries. It is designed to be easy to use and modify for various scenarios. For further assistance or feature requests, please contact the development team.
```

This manual provides a comprehensive guide for users to understand and utilize the Query Handler Application effectively.