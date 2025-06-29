```markdown
# Graph Painter

A Python application for counting valid painting configurations of a graph based on vertex coloring.

## Quick Install

To run the Graph Painter application, ensure you have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

The Graph Painter application allows users to determine the number of ways to paint a graph's vertices in two colors (red and blue) under specific conditions. The primary goal is to count the configurations where the number of edges connecting differently colored vertices is even.

### Main Functions

1. **count_painting_ways(N: int, M: int, K: int, edges: List[Tuple[int, int]]) -> int**
   - This is the main function that takes the number of vertices (N), the number of edges (M), the number of vertices to be painted red (K), and a list of edges connecting the vertices.
   - It validates the input, constructs the graph, and counts the valid painting configurations.

2. **Graph Class**
   - Represents the graph structure and contains methods for creating an adjacency list, calculating vertex degrees, and counting edges between differently colored vertices.

3. **Utility Functions**
   - `nCr(n, r)`: Calculates the number of combinations (n choose r).
   - `validate_input(N, M, K, edges)`: Validates the input parameters to ensure they meet specified constraints.

## 📖 How to Use

1. **Input Format**
   - The input should be provided in the following format:
     ```
     N
     M
     K
     U_1 V_1
     U_2 V_2
     ...
     U_M V_M
     ```
   - Where:
     - `N` is the number of vertices.
     - `M` is the number of edges.
     - `K` is the number of vertices to be painted red.
     - Each subsequent line contains two integers representing an edge between vertices `U_i` and `V_i`.

2. **Running the Application**
   - Save your input in a text file, for example, `input.txt`.
   - Run the application using the command line:
     ```bash
     python main.py < input.txt
     ```
   - The output will be the total number of valid painting configurations printed to the console.

3. **Example Input**
   ```
   5
   4
   2
   1 2
   2 3
   3 4
   4 5
   ```

4. **Expected Output**
   - The application will output an integer representing the count of valid configurations.

## Dependencies

Ensure you have the following Python packages installed:
- `itertools` (part of the standard library, no installation needed)
- Any other dependencies specified in `requirements.txt`.

## Support

For any issues or questions regarding the Graph Painter application, please reach out to our support team or check our documentation for further assistance.
```
