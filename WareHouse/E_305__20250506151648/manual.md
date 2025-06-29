Here's the `manual.md` file that provides a detailed user manual for the software, including an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# Guarded Vertices Application

This application is designed to manage and analyze an undirected graph, allowing users to determine which vertices are "guarded" based on the positions and stamina of guards placed at specific vertices.

## Main Functions

- **Graph Representation**: The application uses an adjacency list to represent the undirected graph, allowing efficient edge storage and traversal.
- **Input Handling**: Users can input the number of vertices (N), edges (M), and guards (K), followed by the edges and guard details.
- **Breadth-First Search (BFS)**: The application performs BFS to find all vertices that can be reached from a guard's position within a specified stamina (number of edges).
- **Guarded Vertices Output**: The application outputs a sorted list of all guarded vertices in ascending order.

## Installation Instructions

To run the application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment (Optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```plaintext
   # If you want to keep the option open for future enhancements that might require external libraries, you could also include commented-out lines for commonly used libraries.
   # Example: 
   # numpy
   # pandas
   ```
   Then install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**:
   Execute the main application file:
   ```bash
   python main.py
   ```

2. **Input Format**:
   - First, input three integers: `N` (number of vertices), `M` (number of edges), and `K` (number of guards).
   - Next, input `M` pairs of integers representing the edges of the graph (each pair `a_i, b_i`).
   - Finally, input `K` pairs of integers representing the guards' positions and their stamina (each pair `p_i, h_i`).

   **Example Input**:
   ```
   5 4 2
   1 2
   1 3
   2 4
   3 5
   1 2
   3 1
   ```

3. **Output**:
   The application will output a sorted list of all guarded vertices based on the input provided.

   **Example Output**:
   ```
   1 2 3 4 5
   ```

## Conclusion

This application provides a robust framework for managing undirected graphs and determining guarded vertices based on guard positions and stamina. For any further enhancements or support, please reach out to the development team.
```

This manual provides a comprehensive overview of the application, ensuring that users can easily understand how to install and use it effectively.