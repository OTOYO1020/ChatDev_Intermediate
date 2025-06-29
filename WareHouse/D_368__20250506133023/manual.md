Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Minimum Subtree Finder

A Python application to find the minimum subtree containing specified vertices in a graph.

## Overview

The Minimum Subtree Finder allows users to input a graph defined by its vertices and edges, and then specify certain vertices of interest. The application utilizes Depth-First Search (DFS) to determine the smallest subtree that includes all specified vertices.

## Main Functions

- **Input Graph**: Users can input the number of vertices and edges to define the graph structure.
- **Specify Required Vertices**: Users can specify which vertices are required to be included in the subtree.
- **Run DFS**: The application performs a DFS to find the minimum subtree and displays the result.
- **User Interface**: A simple GUI built with Tkinter for easy interaction.

## Installation

To run the Minimum Subtree Finder, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

1. **Python**: Version 3.6 or higher.
2. **Tkinter**: This is included with standard Python installations. If you encounter issues, refer to the Tkinter documentation for installation instructions.

### Install Required Packages

You may need to install additional packages using pip. Open your terminal or command prompt and run:

```bash
pip install tkinter
```

## How to Use the Application

1. **Run the Application**: 
   - Open your terminal or command prompt.
   - Navigate to the directory where the application files (`main.py`, `graph.py`, `app.py`) are located.
   - Run the application using the command:
     ```bash
     python app.py
     ```

2. **Input Data**:
   - Enter the number of vertices (N) in the first input field.
   - Enter the number of required vertices (K) in the second input field.
   - Input the edges of the graph in the text area, with each edge represented as two integers (A B) on a new line.
   - Enter the required vertices in the last input field, separated by spaces.

3. **Run DFS**:
   - Click the "Run DFS" button to execute the algorithm.
   - The application will display a message box with the result, indicating the minimum number of vertices needed to include all specified vertices in the subtree.

4. **Error Handling**:
   - If any input is invalid or if required vertices are not provided, an error message will be displayed.

## Example Usage

1. **Input Example**:
   - Number of vertices (N): `5`
   - Number of required vertices (K): `2`
   - Edges:
     ```
     1 2
     1 3
     2 4
     2 5
     ```
   - Required vertices: `4 5`

2. **Output**:
   - The application will calculate and display the minimum vertices needed to include vertices 4 and 5 in the subtree.

## Conclusion

The Minimum Subtree Finder is a powerful tool for analyzing graph structures and finding specific subtrees based on user-defined criteria. With its intuitive interface and efficient algorithm, users can easily explore and manipulate graph data.

For any issues or feature requests, please contact our support team.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.