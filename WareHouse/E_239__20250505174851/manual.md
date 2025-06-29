Here's a detailed user manual for the tree query application, formatted in Markdown as requested:

```markdown
# Tree Query Application

A Python application for querying a tree structure based on vertex values and subtree queries.

## Overview

This application allows users to create a tree structure, input values for each vertex, and perform queries to find the K-th largest value in the subtree rooted at a specified vertex. It utilizes Depth-First Search (DFS) to traverse the tree and efficiently gather values.

## Main Functions

1. **Input Vertices and Values**: Users can input the number of vertices and their corresponding values.
2. **Define Tree Structure**: Users can define the tree structure by inputting edges between vertices.
3. **Query Subtrees**: Users can query the tree to find the K-th largest value in the subtree of a specified vertex.

## Installation

To run the Tree Query Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not have external dependencies beyond the standard library, so no additional installations are required.

## How to Use the Application

1. **Run the Application**: Navigate to the directory containing `main.py` and run the application using the following command:

   ```bash
   python main.py
   ```

2. **Input Number of Vertices and Queries**: When prompted, enter the number of vertices (N) and the number of queries (Q). For example:

   ```
   Enter number of vertices (N) and number of queries (Q): 5 3
   ```

3. **Input Vertex Values**: Enter the values for each vertex in a space-separated format. For example:

   ```
   Enter 5 vertex values (space-separated): 10 20 30 40 50
   ```

4. **Define Tree Edges**: Input the edges of the tree in the format `parent child`. For example:

   ```
   Enter 4 edges (parent child) for the tree (1-indexed):
   1 2
   1 3
   2 4
   2 5
   ```

5. **Input Queries**: For each query, input the vertex and the value of K. For example:

   ```
   Enter 3 queries (vertex k):
   2 2
   1 1
   3 1
   ```

6. **View Results**: The application will output the results for each query, displaying the K-th largest value from the respective subtree.

## Example Usage

Here’s a complete example of how to use the application:

```
Enter number of vertices (N) and number of queries (Q): 5 3
Enter 5 vertex values (space-separated): 10 20 30 40 50
Enter 4 edges (parent child) for the tree (1-indexed):
1 2
1 3
2 4
2 5
Enter 3 queries (vertex k):
2 2
1 1
3 1
```

**Output:**
```
20
50
30
```

## Notes

- Ensure that the vertex indices are 1-indexed.
- The application handles invalid inputs gracefully, prompting the user to re-enter values when necessary.
- The application is designed to handle large values of N and Q efficiently.

## Support

For any issues or questions, please contact support at [support@example.com](mailto:support@example.com).
```

This manual provides a comprehensive guide for users to understand the application, install it, and use its features effectively.