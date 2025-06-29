Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Graph Distance Checker

A Python application to determine the minimum distances from vertices in an undirected graph to the nearest black-painted vertex based on specified conditions.

## Quick Install

To run the application, you need to have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install collections
```

## 🤔 What is this?

The Graph Distance Checker application allows you to input a graph defined by its vertices and edges, along with specific distance conditions for certain vertices. The application will determine if there exists a valid painting of the graph's vertices (black or white) such that the distance conditions are satisfied.

### Main Functions

1. **Graph Representation**: The application constructs an undirected graph using an adjacency list based on the input edges.
2. **Breadth-First Search (BFS)**: It implements a BFS algorithm to calculate the minimum distances from each vertex to the nearest black-painted vertex.
3. **Distance Validation**: The application checks if there exists at least one vertex that can be painted black while satisfying the distance conditions for all specified vertex-distance pairs.
4. **Output**: It prints the color of each vertex or "IMPOSSIBLE" if no valid painting exists.

## 📖 How to Use

1. **Input Format**:
   - First, input two integers `N` (number of vertices) and `M` (number of edges).
   - Next, input `M` pairs of integers `(u_i, v_i)` representing the edges of the graph.
   - Then, input an integer `K` (number of distance pairs).
   - Finally, input `K` pairs of integers `(p_i, d_i)` representing the vertices and their respective distances.

   Example Input:
   ```
   5 4
   1 2
   1 3
   2 4
   3 5
   3
   1 1
   2 2
   5 1
   ```

2. **Running the Application**:
   - Save the provided code files (`main.py`, `graph.py`, `distance_checker.py`, `app.py`) in the same directory.
   - Run the application using the command:
   ```bash
   python main.py
   ```

3. **Interpreting the Output**:
   - The application will output the colors of the vertices in the format:
   ```
   vertex: color, vertex: color, ...
   ```
   - If no valid painting exists, it will print:
   ```
   IMPOSSIBLE
   ```

## 🛠️ Example

Given the following input:
```
5 4
1 2
1 3
2 4
3 5
3
1 1
2 2
5 1
```

The output might look like:
```
1: black, 2: black, 3: black, 4: white, 5: white
```

## 📄 Additional Notes

- Ensure that the input adheres to the specified format to avoid errors during execution.
- The application is designed to handle undirected graphs and will not validate for directed edges or self-loops.

For further assistance or to report issues, please contact our support team.
```

This manual provides a comprehensive overview of the application, its installation, usage, and expected input/output formats.