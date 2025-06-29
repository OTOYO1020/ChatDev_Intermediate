```markdown
# Strongest Programmer Application

This application determines the strongest programmer based on superiority relations among a group of programmers. It utilizes a directed graph to represent these relations and employs depth-first search (DFS) to analyze reachability.

## Main Functions

- **Input Handling**: Reads the number of programmers (N) and the number of superiority relations (M) from standard input.
- **Graph Representation**: Initializes a directed graph using an adjacency list to store superiority relations.
- **Relation Addition**: Updates the graph with pairs of programmers indicating superiority.
- **Strongest Programmer Identification**: Implements a function to find the strongest programmer based on reachability from others.
- **Output**: Prints the index of the strongest programmer or -1 if there are multiple candidates.

## Installation

To run the Strongest Programmer application, ensure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can create one with the necessary dependencies. For this application, the standard Python library is sufficient.

## How to Use

1. **Prepare Input**: The input should be formatted as follows:
   - The first line contains two integers, N (number of programmers) and M (number of superiority relations).
   - The next M lines each contain two integers A and B, indicating that programmer A is stronger than programmer B.

   Example Input:
   ```
   5 4
   1 2
   1 3
   2 4
   3 5
   ```

2. **Run the Application**: You can run the application from the command line. Make sure to redirect the input from a file or provide it directly in the terminal.

   ```bash
   python main.py < input.txt
   ```

   Or, if you want to input directly:
   ```bash
   python main.py
   ```

   Then paste your input and press Enter.

3. **View Output**: The application will output a single integer on a new line, which is the index of the strongest programmer or -1 if there are multiple candidates.

## Example Usage

Given the input:
```
4 3
1 2
1 3
2 4
```

The output will be:
```
0
```

This indicates that programmer 1 (index 0 in 0-based indexing) is the strongest programmer.

## Error Handling

The application includes basic error handling for the following scenarios:
- The number of programmers must be at least 1.
- The number of relations provided must match M.
- Programmer indices must be within the valid range (1 to N).

If any of these conditions are not met, an error message will be printed.

## Conclusion

The Strongest Programmer application is a powerful tool for determining superiority relations among programmers. By leveraging graph theory and DFS, it provides an efficient way to identify the strongest individual in a programming team.
```
