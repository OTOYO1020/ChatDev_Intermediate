Here's a detailed user manual for the Guarded Vertices application, formatted in Markdown as requested:

```markdown
# Guarded Vertices Application

A Python application designed to identify guarded vertices in a graph based on the positions and stamina of guards.

## Overview

The Guarded Vertices application allows users to input a graph defined by vertices and edges, along with the positions and stamina of guards. The application will then calculate which vertices are guarded based on the guards' abilities to reach them within their stamina limits.

## Main Functions

- **Input Handling**: The application prompts users to input the number of vertices, edges, and guards, as well as the specific edges and guard details.
- **Graph Representation**: It constructs an adjacency list representation of the graph to facilitate efficient traversal.
- **Guarded Vertex Calculation**: Using a breadth-first search (BFS) algorithm, the application determines which vertices are guarded based on the guards' stamina.
- **Output**: The application outputs a sorted list of unique guarded vertices.

## Installation

To run the Guarded Vertices application, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

The application requires the following Python packages:

- `collections`
- `typing`

These packages are part of the Python standard library, so no additional installation is necessary.

## How to Use the Application

1. **Clone the Repository**: If you haven't already, clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the `main.py` file to start the application.

   ```bash
   python main.py
   ```

3. **Input Parameters**: Follow the prompts to input the required parameters:
   - **Number of Vertices (N)**: Enter the total number of vertices in the graph.
   - **Number of Edges (M)**: Enter the total number of edges.
   - **Edges**: Input the edges in the format `u,v;u,v;...`, where `u` and `v` are vertex indices.
   - **Number of Guards (K)**: Enter the total number of guards.
   - **Guards**: Input the guards in the format `position,stamina;...`, where `position` is the guard's vertex index and `stamina` is the guard's stamina.

4. **View Output**: After entering the parameters, the application will display the guarded vertices. If no vertices are guarded, it will inform you accordingly.

## Example Usage

Here is an example of how to input data when prompted:

```
Enter the number of vertices (N): 5
Enter the number of edges (M): 4
Enter edges (format: u,v;u,v;...): 0,1;1,2;2,3;3,4
Enter the number of guards (K): 2
Enter guards (format: position,stamina;...): 0,2;3,1
```

### Expected Output

```
Guarded Vertices: 0, 1, 2, 3, 4
```

## Error Handling

The application includes input validation to ensure that:
- The number of edges matches the specified count.
- Edge vertices are within the valid range.
- Guard positions and stamina are valid.

If any input errors occur, the application will display an appropriate error message.

## Conclusion

The Guarded Vertices application is a powerful tool for analyzing graph structures with respect to guard placements. By following the instructions above, users can easily set up and utilize the application to determine guarded vertices in their graphs.
```

This manual provides a comprehensive guide for users to understand the functionality of the Guarded Vertices application, how to install it, and how to use it effectively.