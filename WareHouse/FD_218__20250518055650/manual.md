```markdown
# Shortest Distance Calculator

A Python application designed to calculate the shortest distance between vertices in a directed graph while excluding specific edges.

## Main Functions

- **Graph Representation**: The application uses an adjacency list to represent directed edges in the graph.
- **Shortest Distance Calculation**: It calculates the shortest distance from Vertex 1 to Vertex N after temporarily removing each edge from the graph.
- **Breadth-First Search (BFS)**: The application employs BFS to determine the shortest path in the graph.
- **Edge Handling**: It restores the graph to its original state after each edge removal to ensure accurate calculations.

## Installation

To run the Shortest Distance Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: Open your terminal or command prompt and run the following command to install the necessary libraries:

   ```bash
   pip install collections
   ```

   Note: The `collections` module is part of the Python standard library, so no additional installation is required for it.

## How to Use the Application

### Running the Application

1. **Main Application**: You can run the main application by executing the `main.py` file. This file contains an example input for testing.

   ```bash
   python main.py
   ```

2. **Graph Input**: You can modify the values of `N`, `M`, and `edges` in `main.py` to test with different graphs. For example:

   ```python
   N = 5  # Number of vertices
   M = 6  # Number of edges
   edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (2, 5)]  # List of directed edges
   ```

3. **Graphical User Interface (GUI)**: Alternatively, you can run the GUI version of the application by executing the `gui.py` file:

   ```bash
   python gui.py
   ```

   - Enter the number of vertices in the first input field.
   - Enter the edges in the second input field, separated by commas (e.g., `1 2, 1 3, 2 4`).
   - Click the "Calculate" button to see the results displayed below.

### Example Usage

- **Input**: 
  - Number of vertices: `5`
  - Edges: `1 2, 1 3, 2 4, 3 4, 4 5, 2 5`
  
- **Output**: The application will display the shortest distances from Vertex 1 to Vertex 5 after removing each edge.

## Edge Cases

- If there are no edges or if the number of vertices is less than 2, the application will return a list of `-1` for each edge removal attempt.
- If Vertex 1 cannot reach Vertex N initially, the application will return `-1` for all edges.

## Conclusion

The Shortest Distance Calculator is a powerful tool for analyzing directed graphs and understanding the impact of edge removal on shortest path calculations. Feel free to explore and modify the code to suit your needs!
```