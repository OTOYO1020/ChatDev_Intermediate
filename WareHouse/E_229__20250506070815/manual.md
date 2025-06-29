Here's the `manual.md` file for the Graph application, detailing the main functions, installation instructions, and usage guidelines.

```markdown
# Graph Application

A simple application to analyze undirected graphs by counting connected components after vertex deletions.

## Main Functions

The Graph Application provides the following key functionalities:

1. **Graph Construction**: 
   - Reads the number of vertices (N) and edges (M) from user input.
   - Constructs an undirected graph using an adjacency list representation based on the provided edges.

2. **Vertex Deletion**: 
   - Allows the user to delete a specified vertex and its incident edges from the graph.

3. **Connected Components Counting**: 
   - After each vertex deletion, counts the number of connected components in the remaining graph using Depth-First Search (DFS).

4. **Output**: 
   - Displays the number of connected components after each vertex deletion in a single line.

## Installation Instructions

To run the Graph Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   This application does not require any additional packages to run. However, if you want to prepare for future extensibility or potential use of libraries, you can include commonly used libraries like NumPy or Pandas. For now, you can simply run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   After setting up the environment, you can run the application using:
   ```bash
   python main.py
   ```

## How to Use the Application

1. **Input the Number of Vertices and Edges**:
   - When prompted, enter the total number of vertices (N) in the graph.
   - Next, enter the total number of edges (M).

2. **Input the Edges**:
   - Provide the edges in the format "A B", where A and B are the vertices connected by an edge. You can input multiple edges separated by spaces.

3. **View the Results**:
   - The application will process the graph and output the number of connected components after deleting each vertex from 1 to N.

### Example Usage

```plaintext
Enter the number of vertices (N): 5
Enter the number of edges (M): 4
Enter the edges (A B): 1 2 2 3 3 4 4 5
Connected Components: 2 1 1 1 5
```

In this example, after deleting vertex 1, there are 2 connected components left. After deleting vertex 2, there is 1 connected component, and so on.

## Conclusion

This Graph Application is a powerful tool for analyzing undirected graphs and understanding the impact of vertex deletions on connectivity. For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive overview of the Graph Application, ensuring users can easily understand how to install and use it effectively.