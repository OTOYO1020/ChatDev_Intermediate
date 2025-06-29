Here's a detailed user manual for the graph simulation software, formatted in Markdown as requested:

```markdown
# Graph Simulation Software

## Overview

The Graph Simulation Software is designed to simulate operations on an undirected graph based on user-defined parameters. It allows users to perform a series of operations on a graph, updating vertex values based on the arithmetic mean of connected vertices. This software is particularly useful for analyzing graph-based data and understanding the dynamics of value propagation across connected nodes.

## Main Functions

1. **Input Parsing**: The software parses input to extract the number of vertices (N), the number of edges to select in each operation (M), the number of operations to perform (K), the list of edges, and the initial values for each vertex.

2. **Graph Representation**: The graph is represented using a data structure that ensures it is undirected, allowing for bidirectional connections between vertices.

3. **Simulation of Operations**: The core functionality is encapsulated in the `perform_operations` method, which simulates K operations on the graph. It randomly selects edges, calculates the mean of connected vertices, and updates their values accordingly.

4. **Expected Value Calculation**: After performing the operations, the software calculates the expected value for each vertex based on the final values, ensuring the results are represented as fractions.

5. **Output**: The final expected values for each vertex are outputted in a specified format, ensuring they are within the range [0, 10^9 + 6].

## Installation

To run the Graph Simulation Software, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   The software requires no additional dependencies beyond the standard Python library. However, if you want to ensure compatibility with fractions, you can install the `fractions` module (if not already included in your Python installation):
   ```bash
   pip install fractions
   ```

3. **Run the Software**:
   You can run the software using the following command:
   ```bash
   python main.py
   ```

## Usage

1. **Input Format**:
   The input should be provided in the following format:
   - The first line contains three integers: N (number of vertices), M (number of edges to select), K (number of operations).
   - The next N lines contain the edges in the format `X_i Y_i` (1-based indexing).
   - The final line contains the initial values for each vertex in the format `A_1 A_2 ... A_N`.

   **Example Input**:
   ```
   5, 3, 10
   1 2
   1 3
   2 4
   3 5
   10 20 30 40 50
   ```

2. **Running the Simulation**:
   After providing the input, the software will parse the data, initialize the graph, and perform the specified operations. The final expected values will be printed to the console.

3. **Output Format**:
   The output will display the final expected values for each vertex in the format:
   ```
   Final Values: [value1, value2, value3, value4, value5]
   ```

## Example

To run a complete simulation, you can provide the following input:

```
5, 3, 10
1 2
1 3
2 4
3 5
10 20 30 40 50
```

After executing the program, you will see the output similar to:

```
Final Values: [expected_value1, expected_value2, expected_value3, expected_value4, expected_value5]
```

## Conclusion

The Graph Simulation Software provides a powerful tool for simulating and analyzing graph-based operations. By following the installation and usage instructions, users can easily set up the environment and run simulations to explore the dynamics of their graphs.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.