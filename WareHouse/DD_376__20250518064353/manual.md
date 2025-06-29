```markdown
# Graph Cycle Detector

A Python application for detecting cycles in directed graphs, specifically focusing on cycles that include vertex '1'. This software allows users to input a graph's vertices and edges, and it efficiently determines the minimum number of edges in any cycle containing vertex '1'.

## Main Functions

- **Cycle Detection**: The core functionality of the application is to detect cycles in a directed graph using Depth-First Search (DFS).
- **Input Validation**: Ensures that the input parameters adhere to specified constraints, such as the number of vertices and edges.
- **Graph Representation**: Utilizes an adjacency list for efficient traversal of the graph.

## Installation

To run the application, ensure you have Python installed on your machine. You can install the necessary dependencies using pip. 

### Step 1: Install Python

Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Dependencies

Open your command line interface (CLI) and run the following command:

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, you can manually install any necessary libraries (if applicable).

## How to Use the Application

### Step 1: Run the Application

Navigate to the directory where the `main.py` file is located and run the following command:

```bash
python main.py
```

### Step 2: Input Parameters

You will be prompted to enter the following parameters:

1. **Number of Vertices (N)**: Enter the total number of vertices in the graph (1 ≤ N ≤ 100).
2. **Number of Edges (M)**: Enter the total number of directed edges in the graph (1 ≤ M ≤ 1000).
3. **Edges**: Enter the directed edges as comma-separated tuples. For example, to input edges from vertex 1 to 2 and from vertex 2 to 3, you would enter:
   ```
   (1,2),(2,3)
   ```

### Step 3: View Results

After entering the parameters, the application will process the input and display the result:

- If a cycle containing vertex '1' is found, it will display the minimum number of edges in that cycle.
- If no such cycle exists, it will inform you that no cycle was found containing vertex '1'.

## Example Usage

```plaintext
Enter number of vertices (N): 3
Enter number of edges (M): 3
Enter edges (comma-separated tuples, e.g., (1,2),(2,3)): (1,2),(2,3),(3,1)
Minimum edges in cycle containing vertex 1: 3
```

## Troubleshooting

- **Invalid Input Format**: Ensure that the edges are entered in the correct format as comma-separated tuples.
- **Edge Count Mismatch**: The number of edges provided must match the number specified for M.

## Conclusion

This application provides a straightforward way to detect cycles in directed graphs, focusing on cycles that include vertex '1'. By following the installation and usage instructions, users can efficiently utilize the cycle detection functionality.

For further inquiries or support, please contact the development team.
```