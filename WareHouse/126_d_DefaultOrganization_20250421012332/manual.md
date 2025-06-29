Here's a detailed user manual for the Tree Coloring program, formatted in Markdown:

```markdown
# Tree Coloring Program

A Python application for coloring the vertices of a tree based on edge weights.

## Overview

The Tree Coloring Program allows users to input a tree structure defined by vertices and edges, and it colors the vertices based on the weights of the edges connecting them. The program uses Depth-First Search (DFS) to traverse the tree and assign colors according to specific rules based on edge weights.

## Main Functions

1. **Input Handling**: The program prompts the user to enter the number of vertices and the edges connecting them.
2. **Graph Construction**: It builds an adjacency list representation of the tree from the input edges.
3. **Coloring Logic**: The program colors the tree starting from the root vertex (vertex 1 or 0 in 0-indexed mode) and applies the coloring rules based on edge weights:
   - If the edge weight is even, the adjacent vertex retains the same color.
   - If the edge weight is odd, the adjacent vertex receives the opposite color.
4. **Output**: The program prints the color of each vertex in order, where 0 represents white and 1 represents black.

## Installation

To run the Tree Coloring Program, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Program**:
   Execute the main application file:
   ```bash
   python main.py
   ```

2. **Input Format**:
   - When prompted, enter the number of vertices (N) as a positive integer.
   - Enter the edges in the format `u v w`, separated by commas. Each edge connects two vertices `u` and `v` with a weight `w`. For example:
     ```
     Enter the number of vertices (N): 5
     Enter the edges (format: u v w, separated by commas): 1 2 3, 1 3 2, 2 4 1, 2 5 4
     ```

3. **Output**:
   After processing the input, the program will output the colors of the vertices in the order of their numbers:
   ```
   0
   1
   0
   1
   1
   ```

## Error Handling

The program includes input validation to ensure:
- The number of vertices is a positive integer.
- The number of edges is exactly N-1.
- Each edge is in the correct format and does not reference invalid vertices.
- No duplicate edges are present.

If any errors are detected, the program will prompt the user to re-enter the input.

## Conclusion

The Tree Coloring Program is a straightforward tool for visualizing and understanding tree structures and their properties through vertex coloring. It can be extended or modified for more complex applications involving graph theory and tree algorithms.
```

This manual provides a comprehensive guide for users to understand the functionality, installation, and usage of the Tree Coloring program.