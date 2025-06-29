```markdown
# Graph BFS Shortest Path Finder

A Python application that implements a breadth-first search (BFS) algorithm to find the shortest path in a transformed graph structure. The graph is represented in a three-layer format based on modulo 3 states for each vertex.

## Main Functions

- **Graph Representation**: The graph is represented using an adjacency list, where each vertex is expanded into three states: (v,0), (v,1), and (v,2).
- **Shortest Path Search**: The application performs a BFS to find the shortest path from a starting vertex S to a target vertex T, considering the three-layer structure.
- **Distance Calculation**: The result of the BFS is divided by three to reflect the minimum number of moves required.

## Installation

To run the application, ensure you have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install collections
```

## How to Use

1. **Input Format**: Prepare your input in the following format:
   - The first line should contain two integers, N (number of vertices) and M (number of edges).
   - The next M lines should contain pairs of integers representing the edges (u, v).
   - The last line should contain two integers representing the starting vertex S and the target vertex T.

   Example input:
   ```
   5 6
   1 2
   1 3
   2 4
   3 4
   4 5
   1 5
   ```

2. **Running the Application**: You can run the application from the command line. Save your input in a text file (e.g., `input.txt`) and execute the following command:

   ```bash
   python main.py < input.txt
   ```

3. **Output**: The application will output the shortest distance divided by three. If no valid path exists, it will output -1.

## Example

Given the following input:
```
5 6
1 2
1 3
2 4
3 4
4 5
1 5
```

The output will be:
```
1
```

This indicates that the shortest path from vertex 1 to vertex 5 requires 1 move in the transformed graph structure.

## Performance

The implementation is optimized to run in O(N + M) time complexity, making it efficient for large graphs with constraints up to N, M ≤ 10^5.

## Conclusion

This application provides a robust solution for finding the shortest path in a transformed graph structure using BFS. It is designed to be efficient and easy to use, making it suitable for various graph-related tasks.
```