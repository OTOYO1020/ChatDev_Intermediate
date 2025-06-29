Here is the `manual.md` file for the Tree Coloring application, detailing the main functions, installation instructions, and usage guidelines:

```markdown
# Tree Coloring Application

A simple application to color a tree using a depth-first search (DFS) algorithm. The application reads a tree structure from input, colors the vertices, and outputs the colors in a specified format.

## Main Functions

- **Tree Structure**: The application represents a tree using an adjacency list, allowing efficient traversal and edge management.
- **Coloring Algorithm**: The `color_tree` function colors the tree using DFS, ensuring that no two adjacent vertices share the same color.
- **Input Handling**: The application reads the number of vertices and edges from standard input, ensuring that the tree is connected before proceeding with the coloring.
- **Output Format**: The colors of the vertices are printed in a single line, space-separated, where 0 represents white and 1 represents black.

## Installation Instructions

To run the Tree Coloring application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application files.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not require any external dependencies beyond Python's standard library. Ensure you have Python installed correctly.

## How to Use the Application

1. **Run the Application**: Execute the main application file.
   ```bash
   python main.py
   ```

2. **Input Format**: Provide the input in the following format:
   - First line: An integer `N` representing the number of vertices in the tree.
   - Next `N-1` lines: Each line contains three integers `u_i`, `v_i`, and `w_i`, representing an edge between vertices `u_i` and `v_i` with weight `w_i`. The weight is not used in the coloring process but is required for the input format.

   Example input:
   ```
   5
   1 2 3
   1 3 4
   2 4 5
   2 5 6
   ```

3. **Output**: After providing the input, the application will output the colors of the vertices in a single line, space-separated. For example:
   ```
   0 1 1 0 0
   ```

## Error Handling

- If the input vertices are out of bounds (not between 1 and N), the application will print an error message and terminate.
- If the tree is not connected, an error message will be displayed.
- If a conflict in coloring is detected (two adjacent vertices with the same color), an error message will be raised.

## Conclusion

The Tree Coloring application provides a straightforward way to visualize tree structures and their properties through coloring. It can be extended or modified for various applications in graph theory and computer science.

For any issues or feature requests, please reach out to the development team.
```

This manual provides a comprehensive overview of the Tree Coloring application, ensuring users can easily understand how to install and use the software effectively.