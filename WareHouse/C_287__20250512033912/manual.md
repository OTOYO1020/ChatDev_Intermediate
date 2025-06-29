Here's a detailed user manual for the Graph Path Checker software, formatted in Markdown as requested:

```markdown
# Graph Path Checker

A tool to determine if a given graph is a path graph based on its vertices and edges.

## Quick Install

To install the necessary dependencies for the Graph Path Checker, you can use pip:

```bash
pip install typing
```

## 🤔 What is this?

The Graph Path Checker is a Python application designed to check if a given graph is a path graph. A path graph is defined as a graph that consists of a sequence of vertices where each vertex is connected to exactly two other vertices, except for the endpoints which are connected to only one vertex.

### Main Functions

- **is_path_graph(N: int, M: int, edges: List[Tuple[int, int]]) -> bool**: This function checks if the provided graph is a path graph by:
  - Validating the number of edges against the number of vertices.
  - Ensuring there are no self-loops or multiple edges.
  - Performing a depth-first search (DFS) to check for connectivity.
  - Verifying that the graph meets the path graph conditions.

## How to Use

1. **Run the Application**: Execute the `main.py` file in your Python environment.

   ```bash
   python main.py
   ```

2. **Input Parameters**:
   - **Number of Vertices (N)**: Enter the total number of vertices in the graph.
   - **Number of Edges (M)**: Enter the total number of edges in the graph.
   - **Edges Input**: Enter the edges in the format `(u v)` separated by commas. For example, for edges between vertex 1 and 2, and vertex 2 and 3, you would input `1 2, 2 3`.

3. **Output**: The application will output whether the provided graph is a path graph or not.

### Example Usage

```plaintext
Enter the number of vertices (N): 4
Enter the number of edges (M): 3
Enter edges (u v) separated by commas: 1 2, 2 3, 3 4
Is path graph: True
```

## Error Handling

- If the number of edges provided does not match the specified M, an error message will be displayed.
- If any vertex is out of the valid range (1 to N), or if there are self-loops or multiple edges, appropriate error messages will be shown.

## Conclusion

The Graph Path Checker is a straightforward tool for validating path graphs. By following the installation and usage instructions, you can easily determine the structure of your graph.

For any further questions or support, please reach out to our support team.
```

This manual provides a comprehensive guide for users to understand the functionality of the Graph Path Checker, how to install it, and how to use it effectively.