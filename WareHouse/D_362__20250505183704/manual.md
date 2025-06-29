```markdown
# Dijkstra's Algorithm Application

This application implements Dijkstra's algorithm to find the minimum weight path in a graph. It allows users to input the number of vertices and edges, the weights of the vertices, and the edges themselves. The application can be run via a command-line interface or a graphical user interface (GUI).

## Main Functions

- **Input Handling**: Read the number of vertices (N) and edges (M), as well as the weights of the vertices and the edges connecting them.
- **Graph Representation**: Construct a graph using an adjacency list to represent the connections and weights between vertices.
- **Dijkstra's Algorithm**: Implement the Dijkstra algorithm to compute the minimum path weights from a starting vertex (vertex 1) to all other vertices.
- **Output**: Display the minimum path weights for vertices 2 through N.

## Installation

To run the application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

You will need the following Python packages:

- `heapq` (part of the Python standard library, no installation required)
- `tkinter` (part of the Python standard library, no installation required)

To ensure you have the necessary packages, you can create a virtual environment and install any additional dependencies if needed.

```bash
# Create a virtual environment
python -m venv dijkstra_env

# Activate the virtual environment
# On Windows
dijkstra_env\Scripts\activate
# On macOS/Linux
source dijkstra_env/bin/activate
```

## How to Use the Application

### Command-Line Interface

1. **Run the Application**:
   Execute the `main.py` script in your terminal.

   ```bash
   python main.py
   ```

2. **Input Data**:
   - Enter the number of vertices (N) and edges (M) separated by a space.
   - Input the weights of the vertices as space-separated integers.
   - For each edge, input the vertices (U, V) and the edge weight (B) on a new line.

3. **View Results**:
   The application will output the minimum path weights from vertex 1 to all other vertices (2 through N).

### Graphical User Interface (GUI)

1. **Run the Application**:
   Execute the `app.py` script in your terminal.

   ```bash
   python app.py
   ```

2. **Input Data**:
   - Fill in the number of vertices (N) and edges (M) in the respective fields.
   - Enter the vertex weights in the provided entry box.
   - Input the edges (U, V, B) one per line in the text area.

3. **Calculate Minimum Path**:
   Click the "Calculate Minimum Path" button to compute the results.

4. **View Results**:
   The results will be displayed in the results text area, showing the minimum path weights from vertex 1 to each vertex (2 through N).

## Example Usage

### Command-Line Example

```
Input:
5 6
1 2 3 4 5
1 2 1
1 3 4
2 3 2
2 4 7
3 4 3
3 5 1

Output:
Minimum path weight from 1 to 2: 1
Minimum path weight from 1 to 3: 3
Minimum path weight from 1 to 4: 10
Minimum path weight from 1 to 5: 4
```

### GUI Example

1. Enter `5` for the number of vertices and `6` for the number of edges.
2. Input `1 2 3 4 5` for the vertex weights.
3. Input the edges:
   ```
   1 2 1
   1 3 4
   2 3 2
   2 4 7
   3 4 3
   3 5 1
   ```
4. Click "Calculate Minimum Path" to see the results.

## Conclusion

This application provides a user-friendly way to explore Dijkstra's algorithm and understand how it computes the shortest paths in a weighted graph. Whether through the command line or GUI, users can easily input their graph data and receive immediate feedback on the minimum path weights.
```