```markdown
# Connected Components Calculator

This software allows users to calculate the number of connected components in a graph after the deletion of each vertex. It is designed to handle graphs represented by vertices and edges, providing insights into the connectivity of the graph structure.

## Main Functions

- **count_connected_components(N: int, M: int, edges: List[Tuple[int, int]]) -> List[int]**: 
  - This is the main function that takes the number of vertices (N), the number of edges (M), and a list of edges. It returns a list of integers representing the number of connected components after each vertex deletion.

- **Graph Class**:
  - **__init__(self, N, edges)**: Initializes the graph with N vertices and the given edges.
  - **count_connected_components(self)**: Counts the number of connected components in the current state of the graph.
  - **delete_vertex(self, vertex)**: Deletes a specified vertex and its incident edges from the graph.
  - **restore_vertex(self, vertex, edges)**: Restores a deleted vertex and its edges back to the graph.

## Installation Instructions

This software does not require any external dependencies. To set up the environment, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install dependencies** (if any are added in the future):
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Software

1. **Run the application**:
   Execute the `main.py` script to start the application:
   ```bash
   python main.py
   ```

2. **Input the graph data**:
   - When prompted, enter the number of vertices (N).
   - Enter the number of edges (M).
   - Provide the edges in the format `u v`, separated by commas (e.g., `1 2, 2 3`).

3. **View the results**:
   After entering the data, the application will calculate and display the number of connected components after each vertex deletion.

## Example Usage

```plaintext
Enter number of vertices (N): 5
Enter number of edges (M): 4
Enter edges (e.g., 1 2, 2 3): 1 2, 2 3, 3 4, 4 5
Connected components after deletion: [2, 2, 2, 2, 1]
```

## Edge Cases

- If there are no vertices (N=0) or no edges (M=0), the application will return a list of zeros.
- The application handles the deletion of all vertices gracefully, returning the appropriate counts.

## Support

For any issues or feature requests, please contact our support team or refer to the documentation for further assistance.
```
