Here's the user manual for the software, formatted in Markdown as requested:

```markdown
# Tree Star Counter

A Python application for counting level-k stars in a tree structure.

## Overview

The Tree Star Counter application reads a tree structure from standard input and calculates the number of level-k stars based on the vertices and edges provided. A level-k star is defined as a leaf node connected to a vertex with a degree of k (where k >= 2).

## Main Functions

- **Input Handling**: Reads the number of vertices and edges from standard input.
- **Tree Representation**: Constructs an adjacency list to represent the tree.
- **Star Counting**: Counts the number of level-k stars in the tree based on the degrees of the vertices.
- **Error Handling**: Validates input to ensure the tree structure is correctly formed.

## Installation

To run the Tree Star Counter application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

The application does not require any external libraries beyond the standard Python library. Ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: If you haven't already, clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the `main.py` file. You can provide input directly through the terminal or redirect from a file.

   ```bash
   python main.py
   ```

3. **Input Format**: 
   - First, input an integer `N` representing the number of vertices in the tree.
   - Then, input `N-1` pairs of integers representing the edges of the tree. Each pair should be in the format `(u, v)`, where `u` and `v` are the vertices connected by the edge.

   **Example Input:**
   ```
   5
   1 2
   1 3
   2 4
   2 5
   ```

4. **Output**: The application will output the count of level-k stars in the tree.

   **Example Output:**
   ```
   2
   ```

## Error Handling

The application includes error handling for various input issues, including:
- Invalid vertex numbers (must be between 1 and N).
- Self-loops (edges connecting a vertex to itself).
- Duplicate edges.
- Incorrect number of edges (must be exactly N-1 for a tree).
- Non-connected trees.

If an error occurs, an appropriate message will be printed to standard error.

## Conclusion

The Tree Star Counter application is a simple yet effective tool for analyzing tree structures and counting level-k stars. For any issues or feature requests, please reach out to the development team.

```

This manual provides a comprehensive guide for users to understand the functionality of the Tree Star Counter application, how to install it, and how to use it effectively.