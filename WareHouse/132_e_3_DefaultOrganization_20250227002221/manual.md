```markdown
# BFS Shortest Path Finder

A command-line application for finding the shortest path in a graph using Breadth-First Search (BFS) with a three-layer transformation of vertices.

## Main Functions

- **Graph Representation**: The application represents a graph using vertices and edges, allowing for efficient storage and traversal.
- **Three-Layer Transformation**: Each vertex is expanded into three states based on modulo 3, creating a transformed graph structure.
- **Shortest Path Search**: Implements BFS to find the shortest path from a starting vertex to a target vertex, considering the three-layer structure.
- **Output**: Returns the shortest distance divided by three or -1 if no valid path exists.

## Installation

To run the BFS Shortest Path Finder, ensure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install collections
```

## How to Use

1. **Input Format**: Prepare your input in the following format:
   - The first line contains two integers, `N` (number of vertices) and `M` (number of edges).
   - The next `M` lines each contain two integers representing an edge between vertices `u` and `v`.
   - The last line contains two integers, `S` (starting vertex) and `T` (target vertex).

   Example input:
   ```
   5 6
   1 2
   1 3
   2 4
   3 4
   4 5
   2 5
   1 5
   ```

2. **Running the Application**: 
   - Save the provided code in a file named `main.py`.
   - Open a terminal and navigate to the directory containing `main.py`.
   - Run the application using the command:
     ```bash
     python main.py
     ```

3. **Providing Input**: You can provide input directly in the terminal or redirect input from a file. For example:
   ```bash
   python main.py < input.txt
   ```

4. **Output**: The application will print the shortest path length or -1 if no path exists.

## Example Usage

Given the input:
```
5 6
1 2
1 3
2 4
3 4
4 5
2 5
1 5
```

The output will be:
```
Shortest Path Length: 1
```

This indicates that the shortest path from vertex 1 to vertex 5 is found in 1 move (considering the three-layer structure).

## Conclusion

The BFS Shortest Path Finder is a powerful tool for efficiently finding the shortest path in a graph with a unique three-layer transformation. It is designed to handle large graphs with up to 100,000 vertices and edges, making it suitable for various applications in graph theory and network analysis.
```