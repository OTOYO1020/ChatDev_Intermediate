```markdown
# Graph Painter Application

The Graph Painter application allows users to determine if a graph can be painted according to specific distance conditions. This software utilizes a breadth-first search (BFS) algorithm to analyze the graph and validate painting conditions based on user-defined parameters.

## Main Functions

- **Input Handling**: The application reads input parameters including the number of vertices, edges, conditions, and distance requirements.
- **Graph Construction**: It constructs a graph using an adjacency list based on the provided edges.
- **Distance Calculation**: Implements BFS to calculate minimum distances from each vertex to all other vertices in the graph.
- **Painting Logic**: Checks if at least one vertex can be painted black while satisfying the distance conditions for specified vertices.
- **Output**: Returns a boolean indicating whether the painting is possible and displays the colors of the vertices.

## Installation

To run the Graph Painter application, ensure you have Python installed on your machine. You can install the required dependencies using pip. Open your terminal or command prompt and run:

```bash
pip install -r requirements.txt
```

**Note**: Ensure you have the following dependencies in your `requirements.txt` file:

```
# requirements.txt
# Add any additional dependencies here if needed
```

## How to Use the Application

### Command-Line Interface (CLI)

1. **Run the Application**: 
   Execute the `main.py` script from your terminal:

   ```bash
   python main.py
   ```

2. **Input Format**: 
   The application expects input in the following format:
   - First line: Number of vertices (N)
   - Second line: Number of edges (M)
   - Next M lines: Each line contains an edge in the format `u v`
   - Next line: Number of conditions (K)
   - Next line: List of vertices (p) in the format `p1,p2,...`
   - Last line: List of distances (d) in the format `d1,d2,...`

   **Example Input**:
   ```
   5
   4
   0 1
   1 2
   1 3
   3 4
   2
   1,3
   1,2
   ```

3. **Output**: 
   The application will print whether painting is possible and the colors of the vertices.

### Graphical User Interface (GUI)

1. **Run the Application**: 
   Execute the `app.py` script from your terminal:

   ```bash
   python app.py
   ```

2. **Input Fields**: 
   Fill in the fields as follows:
   - **Number of vertices (N)**: Enter the total number of vertices in the graph.
   - **Number of edges (M)**: Enter the total number of edges.
   - **Edges**: Enter the edges in the format `u v`, separated by commas (e.g., `0 1, 1 2`).
   - **Number of conditions (K)**: Enter the number of distance conditions.
   - **Vertices (p)**: Enter the list of vertices for conditions, separated by commas (e.g., `1,3`).
   - **Distances (d)**: Enter the corresponding distances, separated by commas (e.g., `1,2`).

3. **Submit**: 
   Click the "Submit" button to process the input. A message box will display whether painting is possible and the colors of the vertices.

## Conclusion

The Graph Painter application provides a robust solution for analyzing graph painting conditions based on user-defined parameters. Whether using the command-line interface or the graphical user interface, users can easily input their data and receive immediate feedback on the painting possibilities.

For any issues or further assistance, please reach out to our support team.
```