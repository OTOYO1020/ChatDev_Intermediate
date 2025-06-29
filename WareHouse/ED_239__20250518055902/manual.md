Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Find K-th Largest in Subtree

This software provides a function to find the K-th largest value in the subtree of a given vertex in a tree structure. It is designed to handle queries efficiently using depth-first search (DFS) and a min-heap.

## Main Functions

- **find_kth_largest_in_subtree(N: int, edges: List[Tuple[int, int]], values: List[int], queries: List[Tuple[int, int]]) -> List[int]**
  - This is the main function that processes the input parameters and returns a list of K-th largest values for each query.
  - **Parameters:**
    - `N`: The number of vertices in the tree.
    - `edges`: A list of tuples representing the edges of the tree.
    - `values`: A list of integers representing the values at each vertex.
    - `queries`: A list of tuples where each tuple contains a vertex and the K value for the query.
  - **Returns:** A list of integers, where each integer is the K-th largest value found for the respective query.

## Installation

To run this software, you need to have Python installed on your machine. You can install the required dependencies using pip. 

### Step 1: Install Python

Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Required Dependencies

Open your terminal or command prompt and run the following command:

```bash
pip install typing
```

## How to Use

1. **Prepare Your Input Data:**
   - Define the number of vertices `N`.
   - Create a list of edges that represent the tree structure.
   - Create a list of values corresponding to each vertex.
   - Prepare a list of queries where each query consists of a vertex and the K value.

2. **Run the Software:**
   - You can run the software by executing the `main.py` file. 
   - Here is an example of how to use the function:

```python
from typing import List, Tuple

# Example input
N = 5
edges = [(0, 1), (0, 2), (1, 3), (1, 4)]
values = [5, 3, 8, 6, 2]
queries = [(0, 2), (1, 1), (3, 1)]

# Call the function
results = find_kth_largest_in_subtree(N, edges, values, queries)
print(results)  # Output: [5, 3, 6]
```

3. **Interpreting the Output:**
   - The output will be a list of integers, where each integer corresponds to the K-th largest value for each query in the order they were provided.

## Example Usage

To see the function in action, you can use the provided example in `main.py`. Just run the script, and it will print the results of the queries based on the defined tree structure and values.

## Conclusion

This software is a powerful tool for efficiently querying tree structures to find specific values. With its simple interface and efficient algorithms, it can be easily integrated into larger applications or used for standalone purposes.
```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, and usage examples, ensuring that users can effectively utilize the provided functionality.