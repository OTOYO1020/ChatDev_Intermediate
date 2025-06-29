Here's a detailed user manual for the `find_lexicographically_smallest_permutation` application, formatted in Markdown:

```markdown
# Lexicographically Smallest Permutation Application

This application allows users to find the lexicographically smallest permutation of integers from 1 to N, subject to a set of constraints. It utilizes a directed graph and topological sorting to determine valid orderings based on the provided constraints.

## Main Functions

- **find_lexicographically_smallest_permutation(N: int, M: int, constraints: List[Tuple[int, int]])**: 
  - This function takes the size of the permutation (N), the number of constraints (M), and a list of constraints as input.
  - It constructs a directed graph based on the constraints and performs a topological sort to find the smallest valid permutation.
  - Returns the permutation as a list of integers or -1 if no valid permutation exists due to cycles in the constraints.

## Installation

To run this application, you need to have Python installed on your system. You can install the required dependencies using the following methods:

1. **Using pip**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Using conda** (if you prefer using Anaconda):
   ```bash
   conda install --file requirements.txt
   ```

Make sure you have the following dependencies in your `requirements.txt`:
```
# Add any required dependencies here, for example:
# heapq is part of the standard library, no need to install it
```

## How to Use the Application

1. **Run the Application**:
   Execute the `main.py` file in your terminal or command prompt:
   ```bash
   python main.py
   ```

2. **Input Parameters**:
   - You will be prompted to enter the size of the permutation (N).
   - Next, enter the number of constraints (M).
   - If M is greater than 0, you will be asked to enter the constraints in the format `(A B)` separated by semicolons. For example:
     ```
     1 2; 2 3; 3 4
     ```

3. **Output**:
   - The application will output the lexicographically smallest permutation if it exists.
   - If a valid permutation cannot be formed due to cycles in the constraints, it will inform you that no valid permutation exists.

## Example Usage

Here’s an example of how to use the application:

1. Start the application:
   ```
   python main.py
   ```

2. Input the following when prompted:
   ```
   Enter N: 4
   Enter M: 3
   Enter Constraints (A B) separated by semicolons:
   1 2; 2 3; 3 4
   ```

3. The output will be:
   ```
   Permutation: 1 2 3 4
   ```

## Error Handling

- If you enter a self-loop (e.g., `1 1`), the application will raise a `ConstraintError` and inform you about the issue.
- If any constraint is out of bounds (not between 1 and N), it will also raise a `ConstraintError`.

## Conclusion

This application provides a straightforward way to compute the lexicographically smallest permutation under given constraints. For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive guide for users to understand the application, install it, and use it effectively.