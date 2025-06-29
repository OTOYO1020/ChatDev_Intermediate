Here's a detailed user manual for the directed cycle detection application, formatted in Markdown as requested:

```markdown
# Directed Cycle Detection Application

Detecting cycles in directed graphs made easy.

## Overview

The Directed Cycle Detection Application is designed to identify cycles in directed graphs based on user-defined vertices and edges. This application utilizes depth-first search (DFS) to traverse the graph and detect cycles efficiently.

## Main Functions

- **Cycle Detection**: The core functionality of the application is to detect cycles in a directed graph. The user can input the number of vertices and the edges of the graph, and the application will return any detected cycles.
- **Input Validation**: The application validates the input to ensure that edges are provided in pairs and that all vertices are within the specified range.
- **User-Friendly Interface**: The application prompts the user for input and provides clear output messages regarding the detection of cycles.

## Installation

To run the Directed Cycle Detection Application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not require any external libraries beyond Python's standard library. You can run the application directly after cloning.

## How to Use the Application

1. **Run the Application**: Open a terminal and navigate to the directory where the application files are located. Run the main application file:

   ```bash
   python main.py
   ```

2. **Input the Number of Vertices**: When prompted, enter the number of vertices (N) in the directed graph.

   ```
   Enter number of vertices (N): 5
   ```

3. **Input the Edges**: Enter the edges of the graph as comma-separated values. Each edge should be represented as a pair (u, v), where u is the starting vertex and v is the ending vertex.

   ```
   Enter edges (comma-separated): 1,2,2,3,3,1
   ```

   **Note**: Ensure that edges are provided in pairs. For example, if you have edges from vertex 1 to 2 and from vertex 2 to 3, you should input them as `1,2,2,3`.

4. **View the Results**: After entering the inputs, the application will process the data and output whether a cycle was detected. If a cycle is found, it will display the vertices that form the cycle.

   ```
   Cycle detected: [1, 2, 3]
   ```

   If no cycle is detected, it will display:

   ```
   No cycle detected.
   ```

## Example Usage

Here’s an example of how to use the application:

1. Run the application:

   ```bash
   python main.py
   ```

2. Input:

   ```
   Enter number of vertices (N): 4
   Enter edges (comma-separated): 1,2,2,3,3,1,3,4
   ```

3. Output:

   ```
   Cycle detected: [1, 2, 3]
   ```

## Conclusion

The Directed Cycle Detection Application provides a straightforward way to detect cycles in directed graphs. By following the installation and usage instructions, users can easily identify cycles in their graphs. For any issues or questions, please refer to the documentation or contact support.
```

This manual provides a comprehensive guide for users to understand the application, its functions, installation steps, and usage instructions.