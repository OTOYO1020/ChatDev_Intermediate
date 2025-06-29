Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Graph Depth-First Search Application

This application allows users to explore an undirected graph using depth-first search (DFS) and calculate a score based on the distinct integers found along non-decreasing paths from vertex 1 to vertex N.

## Main Functions

- **Graph Representation**: The application uses an adjacency list to represent the undirected graph.
- **Depth-First Search (DFS)**: The DFS algorithm explores all paths from vertex 1 to vertex N, checking for non-decreasing sequences and calculating scores based on distinct integers.
- **User Input**: The application prompts users to input the number of vertices, edges, and the edges themselves, as well as the values associated with each vertex.

## Installation

To run this application, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This application does not have any external dependencies beyond the standard Python library. However, it is recommended to use a virtual environment to manage your Python packages.

1. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```
2. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

## How to Use the Application

1. **Run the Application**:
   Execute the main script to start the application:
   ```bash
   python main.py
   ```

2. **Input the Number of Vertices and Edges**:
   When prompted, enter the number of vertices (N) and edges (M) in the format:
   ```
   N M
   ```
   Ensure that N is a positive integer and M is a non-negative integer.

3. **Input the Edges**:
   If M is greater than 0, you will be prompted to enter the edges of the graph. Input each edge in the format:
   ```
   u v
   ```
   where `u` and `v` are the vertices connected by the edge. Ensure that both vertices are within the range of 1 to N.

4. **Input the Values at Vertices**:
   After entering the edges, you will be prompted to enter the values associated with each vertex. Input the values in a space-separated format:
   ```
   value1 value2 value3 ... valueN
   ```
   Make sure to provide exactly N values.

5. **View the Result**:
   After all inputs are provided, the application will perform the DFS and calculate the maximum score based on the distinct integers found along non-decreasing paths. The result will be displayed as:
   ```
   Maximum Score: <score>
   ```

## Example Usage

```
Enter number of vertices and edges (N M): 5 4
Enter edges (u v) one per line:
1 2
1 3
2 4
3 5
Enter values at vertices (space-separated): 1 2 2 3 4
Maximum Score: 3
```

## Conclusion

This application provides a robust way to explore graphs and calculate scores based on specific criteria. For any issues or feature requests, please contact the development team at ChatDev.
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and example interactions to help users effectively utilize the software.