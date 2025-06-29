Here's a detailed user manual for the graph coloring application, formatted in Markdown:

```markdown
# Graph Coloring Application

This application allows users to input a graph defined by its vertices and edges, and then colors the graph based on the weights of the edges. The coloring is determined by the evenness or oddness of the edge weights, providing a visual representation of the graph's structure.

## Main Functions

- **Input Reception**: Accepts the number of vertices and edges from the user.
- **Graph Construction**: Builds an undirected graph using an adjacency list representation.
- **Color Management**: Initializes and manages the colors of the vertices.
- **Graph Coloring**: Colors the graph using Depth-First Search (DFS) based on edge weights.
- **Output**: Displays the color of each vertex after the coloring process is complete.

## Installation

To run the Graph Coloring Application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

To install the required dependencies, create a `requirements.txt` file with the following content:

```
tkinter
```

Then, you can install the dependencies using pip:

```bash
pip install -r requirements.txt
```

## How to Use the Application

### Running the Application

1. **Clone the Repository**: Download or clone the repository containing the application files.
   
2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where the application files are located.

3. **Run the Application**: Execute the following command to start the application:

   ```bash
   python gui.py
   ```

### Inputting Data

1. **Enter the Number of Vertices**: In the GUI, input the total number of vertices in the graph. This number should be at least 1.

2. **Enter the Edges**: Below the vertices input field, you will find a text area to enter the edges. Each edge should be entered in the format `u v w`, where:
   - `u` is the starting vertex.
   - `v` is the ending vertex.
   - `w` is the weight of the edge connecting `u` and `v`.

   For example:
   ```
   0 1 2
   1 2 3
   0 2 4
   ```

   This input represents three edges with their respective weights.

3. **Submit the Data**: Click the "Submit" button to process the input data.

### Viewing Results

After submitting the graph data, the application will process the input and color the graph. A message box will appear displaying the color of each vertex (0 or 1), one per line, in ascending order of vertex number.

## Example Usage

1. Start the application.
2. Input `3` for the number of vertices.
3. Enter the edges:
   ```
   0 1 2
   1 2 3
   ```
4. Click "Submit".
5. View the resulting colors in the message box.

## Conclusion

The Graph Coloring Application provides a simple and effective way to visualize graph structures and their properties through coloring. For any issues or feature requests, please contact the development team.

```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and examples to help users effectively utilize the software.