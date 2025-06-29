Here's a detailed user manual for the Star Tree Checker application, formatted in Markdown:

```markdown
# Star Tree Checker

A simple application to determine if a given tree structure is a star tree based on vertex degrees.

## Overview

A star tree is a type of tree where one central vertex is connected to all other vertices (leaves), which only connect to the center. This application reads the number of vertices and edges from the user and checks if the tree structure meets the criteria of a star tree.

## Main Functions

- **Input Handling**: Reads the number of vertices and edges from standard input.
- **Degree Calculation**: Initializes a degree list to track the number of connections for each vertex.
- **Star Tree Validation**: Checks if the tree is a star by counting vertices with specific degrees.
- **Output**: Returns "YES" if the tree is a star, otherwise "NO".

## Installation

To run the Star Tree Checker, you need to have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

To ensure that all necessary dependencies are installed, create a `requirements.txt` file with the following content:

```
# Future dependencies can be added here
```

You can install any required dependencies using pip:

```bash
pip install -r requirements.txt
```

## How to Use

1. **Run the Application**: Execute the main application file `main.py` in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input the Number of Vertices**: When prompted, enter the integer value for the number of vertices (N). Ensure that N is at least 2, as a tree must have a minimum of 2 vertices.

   ```
   Enter the number of vertices (N): 5
   ```

3. **Input the Edges**: You will be prompted to enter N-1 edges in the format `a b`, where `a` and `b` are the vertex numbers connected by the edge. Enter each edge on a new line.

   ```
   Please enter 4 edges (format: a b) separated by new lines:
   1 2
   1 3
   1 4
   1 5
   ```

   - Ensure that:
     - Vertices are in the range from 1 to N.
     - No edge connects a vertex to itself.
     - No duplicate edges are entered.

4. **View the Result**: After entering all edges, the application will output "YES" if the tree is a star tree, or "NO" if it is not.

   ```
   YES
   ```

## Error Handling

The application includes error handling for various input scenarios:

- If the number of vertices is less than 2, an error message will be displayed.
- If the edges are not entered in the correct format, an error message will prompt for re-entry.
- Duplicate edges and self-connecting edges will also trigger error messages.

## Conclusion

The Star Tree Checker is a straightforward tool for validating tree structures. By following the instructions above, users can easily determine if their tree is a star tree. For any further assistance or feature requests, please contact the development team.

```

This manual provides a comprehensive guide for users to understand the functionality of the Star Tree Checker application, how to install it, and how to use it effectively.