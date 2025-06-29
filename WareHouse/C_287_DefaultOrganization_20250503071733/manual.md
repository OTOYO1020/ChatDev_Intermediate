Here is the detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Path Graph Checker

A simple application to determine if a given undirected graph is a path graph based on user input.

## Main Functions

The Path Graph Checker allows users to:

- Input the number of vertices (N) and edges (M) of the graph.
- Enter the edges of the graph in the format `u,v` where `u` and `v` are the vertices connected by an edge.
- Validate if the graph is a path graph, which must meet the following conditions:
  - The number of edges must be exactly `N - 1`.
  - All vertices must be connected (i.e., reachable from vertex 1).
  - Each vertex must have either 1 or 2 neighbors.

The application will output either "YES" or "NO" based on the validation results.

## Installation

To run the Path Graph Checker, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: Create a virtual environment (optional but recommended) and install the required dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

   If you need to add any libraries in the future, you can specify them in the `requirements.txt` file.

## How to Use the Application

### Command-Line Interface

1. **Run the Application**: Navigate to the directory containing `main.py` and run the following command:

   ```bash
   python main.py
   ```

2. **Input Format**: When prompted, enter the number of vertices (N) and edges (M) separated by a space. Then, enter each edge on a new line in the format `u v`.

   Example Input:
   ```
   5 4
   1 2
   2 3
   3 4
   4 5
   ```

3. **Output**: The application will print "YES" if the graph is a path graph, or "NO" if it is not.

### Graphical User Interface (GUI)

1. **Run the GUI Application**: Navigate to the directory containing `app.py` and run the following command:

   ```bash
   python app.py
   ```

2. **Enter Graph Details**:
   - Input the number of vertices (N) in the first entry box.
   - Input the number of edges (M) in the second entry box.
   - Enter the edges in the third entry box, separated by commas (e.g., `1,2,2,3`).

3. **Check the Graph**: Click the "Check Graph" button to validate the graph.

4. **View Results**: A message box will display "YES" or "NO" based on the validation results.

## Conclusion

The Path Graph Checker is a straightforward tool for validating path graphs. It provides both a command-line interface and a graphical user interface for user convenience. For any issues or feature requests, please reach out to the development team.

```

This manual provides a comprehensive overview of the software, including its functions, installation instructions, and usage guidelines. Let me know if you need any modifications or additional information!