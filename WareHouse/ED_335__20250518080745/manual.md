```markdown
# Max Score Path Finder

A Python application designed to find the maximum score path in a graph based on user-defined vertices, edges, and values associated with each vertex. The application utilizes depth-first search (DFS) to explore all simple paths from vertex 1 to vertex N, calculating scores based on the distinct integers in the path.

## Main Functions

- **Input Parsing**: The application reads the number of vertices (N), number of edges (M), edges (U, V), and values (A) for each vertex from user input.
- **Graph Representation**: Constructs a graph using an adjacency list based on the provided edges.
- **Path Exploration**: Implements a depth-first search (DFS) to explore all paths from vertex 1 to vertex N.
- **Score Calculation**: Checks if the path is non-decreasing and calculates the score as the number of distinct integers in the path.
- **Maximum Score Output**: Outputs the maximum score found after exploring all paths.

## Installation

To run the application, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This application requires the following Python libraries:
- `tkinter` (for GUI)
- `setuptools` (for packaging)

You can install the required dependencies using pip:

```bash
pip install setuptools
```

## How to Use

1. **Run the Application**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the application files are located.
   - Run the main application file:
     ```bash
     python main.py
     ```
   - Alternatively, if you want to use the GUI version, run:
     ```bash
     python app.py
     ```

2. **Input Data**:
   - For the command-line version:
     - Enter the number of vertices (N).
     - Enter the number of edges (M).
     - Input the edges in the format `U,V;U,V;...` (e.g., `1,2;2,3`).
     - Input the values for each vertex in the format `A1,A2,A3,...` (e.g., `1,2,3`).
   - For the GUI version:
     - Fill in the fields for the number of vertices, number of edges, edges, and values.
     - Click the "Calculate Max Score" button to compute the maximum score.

3. **View Results**:
   - The application will display the maximum score found based on the paths explored from vertex 1 to vertex N.
   - If there are any errors in the input, appropriate error messages will be shown.

## Example Usage

- **Command-Line Example**:
  ```
  Enter number of vertices (N): 4
  Enter number of edges (M): 4
  Enter edges (U, V) separated by semicolons (e.g., '1,2;2,3'): 1,2;2,3;3,4;1,4
  Enter values (A) for each vertex separated by commas (e.g., '1,2,3'): 1,2,3,4
  Maximum Score: 3
  ```

- **GUI Example**:
  - Input N: `4`
  - Input M: `4`
  - Input Edges: `1,2;2,3;3,4;1,4`
  - Input Values: `1,2,3,4`
  - Click "Calculate Max Score" to see the result.

## Conclusion

The Max Score Path Finder is a powerful tool for exploring graph paths and calculating scores based on user-defined criteria. It provides both command-line and graphical user interfaces for ease of use. Enjoy exploring your graphs!
```