```markdown
# Minimum Path Weights Application

This application calculates the minimum path weights in a graph, taking into account both vertex and edge weights. It uses Dijkstra's algorithm to efficiently find the shortest paths from a starting vertex to all other vertices in the graph.

## Main Functions

- **find_minimum_path_weights(N: int, M: int, A: List[int], edges: List[Tuple[int, int, int]]) -> List[int]**: 
  - This is the main function that initializes the graph and computes the minimum path weights from vertex 1 to all other vertices.
  - **Parameters**:
    - `N`: Number of vertices in the graph.
    - `M`: Number of edges in the graph.
    - `A`: A list of weights for each vertex.
    - `edges`: A list of tuples representing each edge with its weights.
  - **Returns**: A list of minimum path weights from vertex 1 to vertices 2 through N.

## Installation

To run this application, you need to have Python installed on your machine. You can install the required dependencies using pip. 

### Step 1: Install Python

Make sure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Dependencies

Open your terminal or command prompt and run the following command:

```bash
pip install heapq
```

(Note: `heapq` is part of the Python standard library, so no installation is needed for it.)

## How to Use the Application

### Running the Application

1. **Using Command Line**:
   - Save the `main.py` and `graph.py` files in the same directory.
   - Open your terminal and navigate to the directory where the files are located.
   - Run the application using the command:
     ```bash
     python main.py
     ```
   - Input the required parameters in the following format:
     ```
     N
     M
     A1,A2,A3,...,AN
     u1,v1,w1
     u2,v2,w2
     ...
     ```
     Where:
     - `N` is the number of vertices.
     - `M` is the number of edges.
     - `A1, A2, ..., AN` are the weights of the vertices.
     - Each line after that represents an edge in the format `u,v,weight`.

2. **Using the GUI**:
   - Save the `app.py` file in the same directory.
   - Run the application using the command:
     ```bash
     python app.py
     ```
   - A GUI window will open where you can input:
     - Number of Vertices (N)
     - Number of Edges (M)
     - Vertex Weights (A) in the format `A1,A2,A3,...,AN`
     - Edges in the format `u,v,weight` separated by semicolons (e.g., `1,2,5; 1,3,10`).
   - Click on the "Calculate" button to compute the minimum path weights.

### Example Input

For a graph with 4 vertices and 4 edges, with vertex weights as follows:

```
4
4
1,2,3,4
1,2,5
1,3,10
2,4,2
3,4,1
```

### Output

The application will output the minimum path weights from vertex 1 to all other vertices (2 through N). If a vertex is unreachable, it will display `-1` for that vertex.

## Error Handling

The application includes error handling for:
- Invalid input formats.
- Negative or zero values for vertices and edges.
- Mismatched number of edges and the provided edges list.

## Conclusion

This application provides a robust solution for calculating minimum path weights in a graph. It is designed to handle large graphs efficiently, making it suitable for various applications in network analysis, routing, and more.
```