Here's a detailed user manual for the tree distance calculator software, formatted in Markdown as requested.

```markdown
# Tree Distance Calculator

A Python application for calculating the minimum distance sum in a tree structure based on vertex weights.

## Overview

This software allows users to input a tree structure defined by vertices and edges, along with a sequence of positive integers representing weights for each vertex. The application computes the minimum distance sum across all vertices efficiently, even for large trees with up to 100,000 vertices.

## Main Functions

- **Input Tree Structure**: Users can define the number of vertices and the edges connecting them.
- **Input Weights**: Users can provide a sequence of positive integers corresponding to each vertex.
- **Calculate Minimum Distance Sum**: The application computes the minimum value of the distance sum function across all vertices and identifies the vertex where this minimum occurs.

## Installation

To run the Tree Distance Calculator, you need to have Python installed on your system. Follow the steps below to set up the environment:

1. **Install Python**: Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: Open your terminal or command prompt and run the following command to install any necessary dependencies (if applicable). This application does not require any external libraries, but ensure you have Python's standard library available.

   ```bash
   pip install -r requirements.txt
   ```

   *(Note: If there are no additional dependencies, you can skip this step.)*

## Usage

To use the Tree Distance Calculator, follow these steps:

1. **Run the Application**: Execute the main application file in your terminal:

   ```bash
   python main.py
   ```

2. **Input the Number of Vertices**: When prompted, enter the number of vertices (N) in the tree.

   ```
   Enter the number of vertices (N):
   ```

3. **Input the Edges**: Enter the edges of the tree in the format `A B`, where A and B are the connected vertices. Input each edge on a new line. To finish entering edges, simply press Enter on an empty line.

   ```
   Enter edges (A B) one per line (end with an empty line):
   ```

4. **Input the Weights**: After entering the edges, input the sequence of weights (C) for each vertex, separated by spaces.

   ```
   Enter sequence of C (space-separated):
   ```

5. **View Results**: The application will compute and display the minimum distance sum and the corresponding vertex.

   ```
   Minimum f(v): {min_value} at vertex {min_vertex}
   ```

## Example

Here’s an example of how to use the application:

```
Enter the number of vertices (N): 5
Enter edges (A B) one per line (end with an empty line):
1 2
1 3
2 4
2 5

Enter sequence of C (space-separated): 1 2 3 4 5
```

Output:
```
Minimum f(v): 14 at vertex 2
```

## Conclusion

The Tree Distance Calculator is a powerful tool for efficiently computing distance sums in tree structures. By following the installation and usage instructions, users can easily set up and run the application to analyze their tree data.

For any issues or further assistance, please contact support.
```

This manual provides a comprehensive guide for users to understand and utilize the Tree Distance Calculator effectively.