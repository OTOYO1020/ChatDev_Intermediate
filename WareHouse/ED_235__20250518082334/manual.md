Here's a detailed user manual for the MST Queries application, formatted in Markdown:

```markdown
# MST Queries

A Python application for handling Minimum Spanning Tree (MST) queries on a graph.

## Overview

The MST Queries application allows users to define a graph and perform queries to determine if a new edge can be included in the minimum spanning tree of that graph. The application utilizes Kruskal's algorithm to compute the MST and efficiently handles multiple queries.

## Main Functions

- **Graph Representation**: The graph is represented using an adjacency list and an edge list.
- **MST Calculation**: Computes the minimum spanning tree using Kruskal's algorithm.
- **Query Handling**: For each query, checks if adding a new edge would still allow the graph to maintain its minimum spanning tree properties.

## Installation

To run the MST Queries application, you need to have Python installed on your machine. You can install the required dependencies using pip. 

### Step 1: Install Python

Make sure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Dependencies

Open your terminal or command prompt and run the following command:

```bash
pip install typing
```

## How to Use the Application

### Step 1: Prepare Input Data

The application expects input data in a specific format. You can provide the input through standard input (stdin). The input format is as follows:

1. The first line contains two integers, `N` (number of vertices) and `M` (number of edges).
2. The next `M` lines each contain three integers `a_i`, `b_i`, and `c_i`, representing an edge between vertices `a_i` and `b_i` with weight `c_i`.
3. The following line contains an integer `Q`, the number of queries.
4. The next `Q` lines each contain three integers `u_i`, `v_i`, and `w_i`, representing a query for a new edge between vertices `u_i` and `v_i` with weight `w_i`.

### Example Input

```
5 6
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4
1 2 5
3
0 4 7
1 4 10
2 4 5
```

### Step 2: Run the Application

You can run the application by executing the `main.py` script. Use the following command in your terminal:

```bash
python main.py < input.txt
```

Where `input.txt` is a file containing your input data in the specified format.

### Step 3: View Results

The application will output the results of each query as either "Yes" or "No", indicating whether the new edge can be included in the minimum spanning tree.

### Example Output

```
Yes
No
Yes
```

## Conclusion

The MST Queries application is a powerful tool for graph analysis, particularly for determining the properties of minimum spanning trees in response to dynamic edge additions. For further assistance or inquiries, please reach out to our support team.

```

This manual provides a comprehensive guide for users to understand the functionality of the MST Queries application, how to install it, and how to use it effectively.