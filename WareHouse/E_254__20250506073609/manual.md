Here is the `manual.md` file that provides a detailed user manual for the graph query application developed by ChatDev:

```markdown
# Graph Query Application

A Python application for managing and querying an undirected graph using breadth-first search (BFS) to compute the sum of indices of vertices within a specified distance.

## Main Functions

- **Graph Creation**: Users can create a graph by specifying the number of vertices and edges. The application supports a maximum degree of 3 for each vertex.
- **Edge Addition**: Users can add edges between vertices, ensuring that the maximum degree constraint is adhered to.
- **Distance Queries**: Users can query the sum of indices of vertices within a specified distance from a given vertex using BFS.

## Installation

To run the Graph Query Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: Open your terminal or command prompt and run the following command to install the required libraries:

   ```bash
   pip install tkinter
   ```

   Note: `tkinter` is usually included with Python installations, but if you encounter issues, ensure it is installed.

## How to Use the Application

### Running the Application

1. **Clone the Repository**: If you haven't already, clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Main Application**: Execute the following command to start the application:

   ```bash
   python main.py
   ```

### Creating a Graph

1. **Input Number of Vertices**: Enter the total number of vertices in the graph. This must be a positive integer.

2. **Input Edges**: Enter the edges in the format `a b`, where `a` and `b` are the vertex indices. Separate multiple edges with commas (e.g., `1 2, 2 3`).

3. **Submit Graph**: Click the "Submit Graph" button to create the graph. If successful, a confirmation message will appear.

### Querying the Graph

1. **Input Query Vertex**: Enter the vertex index from which you want to calculate the sum of indices.

2. **Input Distance**: Enter the distance `k` within which you want to sum the indices of reachable vertices.

3. **Submit Query**: Click the "Submit Query" button to execute the query. The result will be displayed in a message box.

### Handling Errors

- If you enter invalid input (e.g., a vertex index out of range or an invalid edge), an error message will be displayed.
- Ensure that the number of edges does not exceed the maximum degree of 3 for any vertex.

## Conclusion

The Graph Query Application provides a user-friendly interface for managing and querying graphs. With its BFS implementation, users can efficiently compute the sum of indices of vertices within a specified distance. For any issues or feature requests, please contact our support team.

```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and error handling. It aims to help users effectively utilize the graph query application.