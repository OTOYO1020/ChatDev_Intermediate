```markdown
# Graph Edge Remover

## Introduction

The Graph Edge Remover application is designed to help users analyze and clean up graph data by identifying and removing unnecessary edges. This software allows users to input the number of vertices and edges in a graph, along with the edges themselves, and calculates the minimum number of edges that need to be removed to eliminate self-loops and multi-edges.

## Main Functions

- **Calculate Minimum Edges to Remove**: The core functionality of the application is to determine how many edges need to be removed to ensure that there are no self-loops (edges that connect a vertex to itself) and no multi-edges (multiple edges connecting the same pair of vertices).

- **User Interface**: The application provides a simple graphical user interface (GUI) that allows users to input their data easily and view the results.

## Installation

To run the Graph Edge Remover application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: Open your terminal or command prompt and run the following command to install the required libraries:

   ```bash
   pip install tkinter
   ```

   Note: `tkinter` is usually included with Python installations, but if you encounter issues, ensure it is installed.

3. **Download the Application**: Clone or download the repository containing the application files (`main.py`, `edge_calculator.py`, and `gui.py`).

## How to Use the Application

### Running the Application

1. Navigate to the directory where the application files are located using your terminal or command prompt.

2. Run the application by executing the following command:

   ```bash
   python gui.py
   ```

### Using the GUI

1. **Input Number of Vertices (N)**: Enter the total number of vertices in your graph.

2. **Input Number of Edges (M)**: Enter the total number of edges you expect in your graph.

3. **Input Edges**: Enter the edges in the format `u,v;u,v;...`, where `u` and `v` are integers representing the vertices connected by an edge. For example, to input edges connecting vertex 0 to 1 and vertex 1 to 2, you would enter `0,1;1,2`.

4. **Calculate**: Click the "Calculate" button to process the input and determine the minimum number of edges to remove.

5. **View Results**: The result will be displayed below the input fields, showing the number of edges that need to be removed.

### Handling Errors

- If you input an invalid edge format or if the edges are out of bounds for the specified number of vertices, an error message will be displayed.

- If the number of unique edges exceeds the specified number of edges (M), a warning will be shown, indicating that duplicates were removed.

## Conclusion

The Graph Edge Remover application is a powerful tool for anyone working with graph data. By following the instructions above, users can easily install and utilize the software to clean up their graph data efficiently. For any further questions or support, please feel free to reach out.
```