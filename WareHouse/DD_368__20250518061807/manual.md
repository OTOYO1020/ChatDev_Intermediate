```markdown
# Minimum Vertices in Tree

This application is designed to determine the minimum number of vertices required to connect all specified vertices in a tree structure. It utilizes Depth First Search (DFS) to traverse the tree and calculate the required vertices efficiently.

## Main Functions

- **parse_input(N: int, K: int, edges: List[Tuple[int, int]], specified_vertices: List[int])**: Validates and parses the input parameters.
  
- **Tree Class**: 
  - **__init__(N: int, edges: List[Tuple[int, int]])**: Initializes the tree with the number of vertices and edges.
  - **build_tree()**: Constructs the adjacency list representation of the tree.
  - **min_vertices_in_tree(K: int, specified_vertices: List[int]) -> int**: Calculates the minimum number of vertices required to connect all specified vertices.

## Installation

To run this application, you need to have Python installed on your machine. You can install the required dependencies using pip. 

1. Open your terminal or command prompt.
2. Run the following command to install the necessary packages:

```bash
pip install typing
```

## How to Use

1. **Clone the Repository**: Download the source code to your local machine.

2. **Navigate to the Directory**: Open your terminal and navigate to the directory where the files are located.

3. **Run the Application**: You can execute the application by running the `main.py` file. You can modify the example input in the `main` function to test with different values.

```bash
python main.py
```

### Example Input

You can modify the input parameters in the `main.py` file as follows:

```python
N = 5  # Number of vertices
K = 3  # Number of specified vertices
edges = [(1, 2), (1, 3), (2, 4), (2, 5)]  # List of edges
specified_vertices = [4, 5, 3]  # List of specified vertices
```

### Expected Output

When you run the application with the example input, it will output the minimum number of vertices required to connect all specified vertices:

```
Minimum Vertices: X
```

Where `X` is the calculated minimum number of vertices.

## Edge Cases

- If `K` equals 1, the function will return 1 since only one vertex is specified.
- If all specified vertices are directly connected, the function will return the count of those vertices.

## Performance

The application is designed to handle large inputs efficiently, with `N` being able to go up to 200,000 vertices.

## Conclusion

This application provides a robust solution for determining the minimum vertices in a tree structure based on specified vertices. Feel free to modify and extend the functionality as needed for your specific use cases.
```