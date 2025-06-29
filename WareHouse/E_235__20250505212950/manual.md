```markdown
# Graph MST Application

A software application designed to compute the Minimum Spanning Tree (MST) of a graph and answer queries regarding the inclusion of edges in the MST.

## Main Functions

1. **Graph Input**: Users can input the number of vertices and edges in the graph, as well as the edges themselves in the format `(a, b, weight)`.

2. **MST Calculation**: The application computes the Minimum Spanning Tree using Kruskal's algorithm.

3. **Query Processing**: Users can submit queries to check if a specific edge `(u, v, weight)` is part of the MST.

4. **Results Display**: The application displays results for each query, indicating whether the edge is included in the MST.

## Installation

To run the application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/graph-mst-app.git
   cd graph-mst-app
   ```

2. **Install Dependencies**:
   You can install the required dependencies using pip. Run the following command in your terminal:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, you can manually install the required packages:
   ```bash
   pip install tkinter
   ```

## How to Use the Application

1. **Run the Application**:
   Execute the following command in your terminal:
   ```bash
   python app.py
   ```

2. **Input Graph Data**:
   - Enter the number of vertices in the first input field.
   - Enter the number of edges in the second input field.
   - In the text area for edges, input each edge in the format `a b weight`, where `a` and `b` are the vertices connected by the edge and `weight` is the edge's weight. Each edge should be on a new line.

3. **Submit Graph**:
   Click the "Submit Graph" button to process the input and compute the MST.

4. **Input Queries**:
   - In the text area for queries, input each query in the format `u v w`, where `u` and `v` are the vertices and `w` is the weight of the edge you want to check. Each query should be on a new line.

5. **Submit Queries**:
   Click the "Submit Queries" button to check if the specified edges are part of the MST.

6. **View Results**:
   The results will be displayed in the results text area, with "Yes" indicating the edge is in the MST and "No" indicating it is not.

## Example Usage

1. **Graph Input**:
   ```
   Number of vertices: 5
   Number of edges: 7
   Edges:
   1 2 3
   1 3 1
   2 3 1
   2 4 6
   3 4 5
   3 5 4
   4 5 2
   ```

2. **Query Input**:
   ```
   1 2 3
   1 3 1
   4 5 2
   2 5 5
   ```

3. **Results**:
   ```
   Yes
   Yes
   Yes
   No
   ```

## Additional Information

For further details on the algorithms used and the structure of the application, please refer to the source code in the `main.py`, `graph.py`, and `app.py` files.

For any issues or feature requests, please contact the development team or submit an issue on the repository.
```