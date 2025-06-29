Here's a detailed user manual for the pathfinding application based on the provided code and requirements.

```markdown
# Pathfinding Application

A Python application designed to calculate the minimum path weight in a graph based on user-defined parameters.

## Quick Install

To set up the environment and install the necessary dependencies, you can use pip:

```bash
pip install -r requirements.txt
```

Make sure you have Python 3.6 or higher installed on your system.

## 🤔 What is this?

This application allows users to define a graph using vertices and weighted edges, and then compute the minimum path weight between specified sequences of vertices. The application utilizes Dijkstra's algorithm for efficient pathfinding and supports permutations of vertex sequences to find the optimal path configuration.

### Main Functions

1. **`min_path_weight(N: int, M: int, edges: List[Tuple[int, int, int]], K: int, A: List[int], B: List[int]) -> int`**
   - This is the main function that calculates the minimum total path weight based on the input parameters.
   - **Parameters:**
     - `N`: Number of vertices in the graph.
     - `M`: Number of edges in the graph.
     - `edges`: A list of tuples representing the edges and their weights.
     - `K`: Length of the sequences A and B.
     - `A`: A list of starting vertices.
     - `B`: A list of ending vertices.
   - **Returns:** The minimum total path weight found after evaluating all permutations of sequence B.

2. **`Graph` Class**
   - Represents the graph structure and contains methods for adding edges and calculating path weights.
   - **Methods:**
     - `add_edge(u: int, v: int, weight: int)`: Adds an edge between vertices `u` and `v` with the specified weight.
     - `f(x: int, y: int) -> int`: Calculates the minimum path weight from vertex `x` to vertex `y` using Dijkstra's algorithm.

### How to Use

1. **Input Format**
   - The application expects input in the following format:
     ```
     N
     M
     u1 v1 w1
     u2 v2 w2
     ...
     uM vM wM
     K
     A1 A2 ... AK
     B1 B2 ... BK
     ```
   - Where:
     - `N` is the number of vertices.
     - `M` is the number of edges.
     - Each edge is defined by two vertices `u` and `v` and a weight `w`.
     - `K` is the number of elements in sequences A and B.
     - `A` is the list of starting vertices.
     - `B` is the list of ending vertices.

2. **Running the Application**
   - To run the application, execute the `main.py` file:
   ```bash
   python main.py < input.txt
   ```
   - Here, `input.txt` is a text file containing the input data in the specified format.

3. **Example Input**
   ```
   5
   6
   0 1 2
   0 2 4
   1 2 1
   1 3 7
   2 3 3
   3 4 1
   3
   0 1 2
   4 3 2
   ```

4. **Output**
   - The application will output the minimum total path weight based on the provided sequences.

### Error Handling

- The application includes error handling for various scenarios:
  - Invalid vertex references.
  - Duplicate vertices in sequences A and B.
  - Invalid lengths for sequences A and B.
  - Handling cases where no valid paths exist.

## 📖 Documentation

For further details on the implementation and usage, please refer to the code comments and structure. The application is designed to be modular, allowing for easy updates and enhancements in the future.

Feel free to reach out for support or contributions to improve the application!
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and error handling, ensuring that users can effectively utilize the software.