Here's a detailed user manual for the Graph Edge Counter application, formatted in Markdown as requested:

```markdown
# Graph Edge Counter

A simple application to count the number of edges that need to be removed from a graph to make it simple (i.e., no multi-edges or self-loops).

## Main Functions

The Graph Edge Counter application performs the following main functions:

1. **Input Handling**: Reads the number of vertices (N) and edges (M) from the user.
2. **Edge Validation**: Validates the edges to ensure they do not contain self-loops and that vertices are within the valid range.
3. **Edge Counting**: Counts the number of multi-edges (duplicate edges) and provides the minimum number of edges to be removed to simplify the graph.
4. **Output**: Displays the count of edges that need to be removed.

## Installation

To run the Graph Edge Counter application, you need to have Python installed on your machine. You can install the required dependencies using the following steps:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Create a `requirements.txt` file with the following content (if not already present):
   ```
   # Future dependencies can be added here
   ```

   Then, run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. **Run the Application**:
   Execute the main script to start the application:
   ```bash
   python main.py
   ```

2. **Input the Number of Vertices and Edges**:
   - When prompted, enter the number of vertices (N) and edges (M).
   - Ensure that N is a positive integer and M is a non-negative integer.

3. **Input Edges**:
   - For each edge, enter the vertices in the format `u v` (e.g., `1 2`).
   - Ensure that:
     - Vertices are between 1 and N.
     - Self-loops (e.g., `1 1`) are not allowed.

4. **View Results**:
   - After entering all edges, the application will output the number of edges that need to be removed to make the graph simple.

## Example Usage

```plaintext
Enter the number of vertices (N): 5
Enter the number of edges (M): 4
Enter edge 1 (format: u v): 1 2
Enter edge 2 (format: u v): 2 3
Enter edge 3 (format: u v): 1 2
Enter edge 4 (format: u v): 3 4
2
```

In this example, the application indicates that 2 edges need to be removed to eliminate the multi-edge between vertices 1 and 2.

## Additional Information

For any issues or feature requests, please contact the development team at [support@chatdev.com](mailto:support@chatdev.com).

Thank you for using the Graph Edge Counter application!
```

This manual provides a comprehensive overview of the application, including its functionality, installation instructions, and usage guidelines. Let me know if you need any further modifications or additional information!