Here's a detailed user manual for the graph application, formatted in Markdown as requested:

```markdown
# Graph Application

A simple application to manage an undirected graph, allowing users to add edges between vertices and find the k-th largest vertex connected to a specified vertex.

## Main Functions

1. **Add Edge**: Connect two vertices in the graph. The graph is undirected, meaning that adding an edge between vertex `u` and vertex `v` also creates an edge from `v` to `u`.

2. **Find k-th Largest**: Given a vertex `v`, retrieve the k-th largest vertex connected to `v`. If there are fewer than `k` connected vertices, the function returns -1.

## Installation

To run the Graph Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   While there are no immediate external dependencies, you can create a `requirements.txt` file for future enhancements. For now, you can run the application without any additional libraries.

   If you prefer to keep it completely empty, you can use the following:
   ```plaintext
   # requirements.txt
   ```

3. **Run the Application**:
   You can run the application by executing the following command in your terminal:
   ```bash
   python main.py
   ```

## How to Use the Application

1. **Set the Number of Vertices**:
   - When the application starts, you will be prompted to enter the number of vertices in the graph.
   - Enter a valid integer and click "Set Vertices".

2. **Add Edges**:
   - To add an edge between two vertices, enter the vertex numbers `u` and `v` in the "Add Edge (u, v):" section.
   - Click "Add Edge". If the edge is successfully added, you will receive a confirmation message.

3. **Find k-th Largest Vertex**:
   - To find the k-th largest vertex connected to a specific vertex, enter the vertex number `v` and the integer `k` in the "Find k-th Largest (v, k):" section.
   - Click "Find". The application will display the result in a message box. If there are not enough connected vertices or if `k` is invalid, you will be notified accordingly.

## Example Usage

- **Setting Vertices**: If you set the number of vertices to `5`, you can add edges like `1 2`, `2 3`, etc.
- **Finding k-th Largest**: If you want to find the 2nd largest vertex connected to vertex `2`, enter `2` for `v` and `2` for `k`.

## Troubleshooting

- If you encounter any errors while adding edges, ensure that the vertices are within the valid range (1 to N).
- Self-loops are not allowed; attempting to connect a vertex to itself will result in an error message.
- If you receive a message indicating that there are not enough vertices connected to the specified vertex, check the edges you have added.

## Conclusion

This Graph Application provides a straightforward interface for managing an undirected graph. You can easily add edges and query for connected vertices. For any further enhancements or support, please feel free to reach out.

```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, usage guidelines, and troubleshooting tips. Let me know if you need any further modifications or additional sections!