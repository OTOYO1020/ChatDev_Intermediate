Here's the `manual.md` file for the graph cycle detection application:

```markdown
# Graph Cycle Detection Application

Detect cycles in directed graphs using Depth-First Search (DFS).

## Overview

This application allows users to input a directed graph defined by its vertices and edges, and it detects cycles starting from vertex 1. If a cycle exists that includes vertex 1, the application will output the minimum number of edges in that cycle. If no such cycle exists, it will provide an appropriate message.

## Main Functions

- **Input Vertices and Edges**: Users can input the number of vertices (N) and edges (M) in the directed graph.
- **Add Directed Edges**: Users can define directed edges between vertices.
- **Cycle Detection**: The application implements a DFS algorithm to detect cycles in the graph.
- **Output Results**: The application will output the minimum cycle length containing vertex 1 or indicate that no such cycle exists.

## Installation

To run this application, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This application does not require any external libraries beyond Python's standard library. Ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: If you have the source code in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main Python file.
   ```bash
   python main.py
   ```

3. **Input Data**: 
   - First, input the number of vertices (N).
   - Next, input the number of edges (M).
   - Then, for each edge, input the pair of integers (a_i, b_i) representing a directed edge from vertex a_i to vertex b_i.

   Example input:
   ```
   5
   6
   1 2
   2 3
   3 1
   3 4
   4 5
   5 3
   ```

4. **View Results**: After inputting the data, the application will process the graph and output either the minimum cycle length containing vertex 1 or a message indicating that no such cycle exists.

## Example Output

- If a cycle exists:
  ```
  Minimum cycle length containing vertex 1: 3
  ```

- If no cycle exists:
  ```
  No cycle exists containing vertex 1.
  ```

## Conclusion

This application provides a straightforward way to detect cycles in directed graphs using DFS. It is designed to be user-friendly and efficient for graph analysis tasks. For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive guide for users to understand the functionality of the application, how to set it up, and how to use it effectively.