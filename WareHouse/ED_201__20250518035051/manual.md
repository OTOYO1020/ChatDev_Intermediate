```markdown
# XOR Distance Calculator

Calculating the total XOR distance between pairs of vertices in a tree structure.

## Overview

The XOR Distance Calculator is a Python application designed to compute the XOR distance between pairs of vertices in a tree. The application takes the number of vertices and a list of edges as input and calculates the total XOR distance for all pairs of vertices.

## Main Functions

- **calculate_xor_distances(N: int, edges: List[Tuple[int, int, int]]) -> int**: This function computes the total XOR distance for all pairs of vertices in a tree. It constructs the tree using an adjacency list representation and performs a Depth-First Search (DFS) to calculate the XOR distances.

## Installation

To run the XOR Distance Calculator, you need to have Python installed on your system. You can install the required dependencies using pip. 

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt`, ensure you have the following libraries:
   - `collections` (part of the Python standard library, no installation needed)

## How to Use

1. **Run the application**:
   Execute the main application file `main.py`:
   ```bash
   python main.py
   ```

2. **Input the number of vertices**:
   When prompted, enter the number of vertices (N) in the tree.

3. **Input the edges**:
   Enter the edges in the format `(u, v, w)` separated by semicolons. For example:
   ```
   1,2,3;1,3,4;2,4,5
   ```
   This represents edges between vertex 1 and 2 with weight 3, vertex 1 and 3 with weight 4, and vertex 2 and 4 with weight 5.

4. **View the result**:
   The application will calculate and display the total XOR distance for all pairs of vertices.

## Error Handling

The application includes error handling for various scenarios:
- If the number of edges is less than `N - 1`, it will raise an error indicating that there are not enough edges to form a connected tree.
- If any edge does not contain exactly three integers, it will raise an error.
- If any vertex is out of the valid range (1 to N), it will raise an error.
- If the graph is not connected, it will raise an error.

## Example Usage

```plaintext
Enter number of vertices (N): 4
Enter edges (u, v, w) separated by semicolons: 1,2,3;1,3,4;2,4,5
Total XOR Distance: 12
```

## Conclusion

The XOR Distance Calculator is a powerful tool for computing distances in tree structures. By following the installation and usage instructions, users can easily calculate the total XOR distance for any given tree.

For further assistance or inquiries, please reach out to our support team.
```