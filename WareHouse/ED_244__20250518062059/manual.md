Here's a detailed user manual for the software, following the structure you provided. This manual will help users understand how to use the `count_sequences` function and the overall application.

```markdown
# Sequence Counter

A Python application for counting valid sequences in a graph based on specific criteria.

## Overview

The `count_sequences` function is designed to count the number of valid sequences of a specified length that start at a given vertex, end at another vertex, and include a specific vertex an even number of times. This application is useful in various graph-related problems, such as pathfinding and sequence analysis.

## Main Functions

- **count_sequences(N, M, K, S, T, X, edges)**: 
  - Counts valid sequences of length `K` starting at vertex `S` and ending at vertex `T`, ensuring that vertex `X` is included an even number of times.
  - Constructs an adjacency list from the provided edges and uses dynamic programming to calculate the number of valid sequences.

## Installation

To run this application, you need to have Python installed on your system. You can install the required dependencies using the following steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   # Required dependencies for the sequence counter application
   ```

   Then, run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the application, follow these steps:

1. **Run the main application**:
   Execute the `main.py` file in your terminal:
   ```bash
   python main.py
   ```

2. **Input values**:
   The application will prompt you to enter the following values:
   - **N**: Number of vertices in the graph.
   - **M**: Number of edges in the graph.
   - **K**: Length of the sequence to count.
   - **S**: Starting vertex.
   - **T**: Ending vertex.
   - **X**: Vertex that must be included an even number of times.

3. **Enter edges**:
   You will be prompted to enter the edges in the format `U,V` (space-separated for multiple edges). For example:
   ```
   1,2 2,3 3,1
   ```

4. **View results**:
   After entering the required information, the application will output the number of valid sequences based on the criteria specified.

## Edge Cases

- If `K` is 0, the function will return 1 if `S` equals `T`, otherwise it will return 0.
- If `S` equals `T` and `K` is odd, the function will return 0.
- If the vertex `X` is not present in the graph, the function will return 0.

## Example

Here’s an example of how to use the application:

1. Run the application:
   ```bash
   python main.py
   ```

2. Input the following when prompted:
   ```
   Enter N (Number of vertices): 3
   Enter M (Number of edges): 3
   Enter K (Length of sequence): 2
   Enter S (Start vertex): 1
   Enter T (End vertex): 3
   Enter X (Vertex to include): 2
   Enter edges in the format 'U,V' (space-separated for multiple edges): 
   1,2 2,3 3,1
   ```

3. The output will display the number of valid sequences:
   ```
   Valid Sequences: <number>
   ```

## Conclusion

This application provides a robust solution for counting valid sequences in a graph based on specific criteria. For any issues or feature requests, please reach out to the development team.

```

This manual provides a comprehensive guide for users to understand and effectively use the software. It covers installation, usage, edge cases, and examples to ensure clarity.