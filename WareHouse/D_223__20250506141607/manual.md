Here's a detailed user manual for the topological sorting application, formatted in Markdown as requested:

```markdown
# Topological Sorting Application

This application provides a solution for determining valid permutations of integers based on given constraints using topological sorting. It reads integers and constraints, constructs a directed graph, and outputs the lexicographically smallest valid permutation or indicates if a cycle exists.

## Main Functions

- **Input Handling**: Reads integers N (number of vertices) and M (number of constraints) from standard input.
- **Constraints Storage**: Initializes an empty list to store pairs of constraints (A_i, B_i).
- **Graph Representation**: Constructs a directed graph where each A_i points to B_i based on the constraints.
- **Topological Sorting**: Performs a topological sort to determine if a valid permutation exists.
- **Cycle Detection**: Checks for cycles in the graph and returns '-1' if detected.
- **Output**: Prints the resulting permutation as a space-separated string or an error message if no valid permutation exists.

## Installation

To run this application, you need Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This application uses the following Python libraries:
- `collections`
- `heapq`

These libraries are included in the Python standard library, so no additional installation is required.

## How to Use

1. **Clone the Repository**: 
   If you haven't already, clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**:
   You can run the application by executing the `main.py` file. Make sure to provide input in the expected format.

   ```bash
   python main.py
   ```

3. **Input Format**:
   The input should be provided in the following format:
   - The first line contains two integers, N and M.
   - The next M lines each contain two integers A_i and B_i representing the constraints.

   **Example Input**:
   ```
   5 4
   2 1
   3 2
   4 3
   5 4
   ```

4. **Output**:
   The application will output either:
   - A space-separated string of the lexicographically smallest valid permutation.
   - `-1` if a cycle is detected or if no valid permutation exists.

   **Example Output**:
   ```
   5 4 3 2 1
   ```

## Error Handling

The application includes error handling for the following cases:
- If N is not a positive integer.
- If M is a negative integer.
- If constraints are out of the range of 1 to N.
- If self-loops are present in the constraints.
- If duplicate edges are detected.

In case of an error, the application will print an appropriate error message.

## Conclusion

This topological sorting application is a powerful tool for solving problems involving directed graphs and constraints. By following the instructions above, you can easily set up and use the application to find valid permutations based on your specific constraints.
```

This manual provides a comprehensive overview of the application, including its functions, installation instructions, usage guidelines, and error handling. Let me know if you need any further modifications or additional information!