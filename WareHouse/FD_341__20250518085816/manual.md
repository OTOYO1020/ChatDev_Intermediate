```markdown
# ChatDev Graph Operations Application

Welcome to the ChatDev Graph Operations Application! This software allows users to perform operations on a graph structure defined by vertices, edges, weights, and pieces. The main function of the application is to calculate the maximum number of operations that can be performed based on the provided graph parameters.

## Main Functions

- **Input Parameters**: Users can input the number of vertices, number of edges, edges themselves, weights for each vertex, and the number of pieces available at each vertex.
- **Graph Representation**: The application constructs an adjacency list representation of the graph based on the edges provided.
- **Operation Calculation**: The application calculates the maximum number of operations that can be performed by placing pieces on adjacent vertices according to specific rules.

## Installation

To run the application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: Open your terminal or command prompt and run the following command to install the required dependencies:

   ```bash
   pip install tkinter
   ```

   Note: `tkinter` is included with most Python installations, but if you encounter issues, please refer to the [tkinter documentation](https://docs.python.org/3/library/tkinter.html) for installation instructions.

## How to Use the Application

1. **Run the Application**: Navigate to the directory where the application files are located and run the `main.py` file:

   ```bash
   python main.py
   ```

2. **Input Graph Parameters**:
   - **Number of Vertices (N)**: Enter the total number of vertices in the graph.
   - **Number of Edges (M)**: Enter the total number of edges in the graph.
   - **Edges**: Input the edges in the format `u,v;u,v;...` where `u` and `v` are the vertex indices (0-indexed) connected by an edge.
   - **Weights**: Input the weights for each vertex in the format `w1,w2,...` where `wi` is the weight of vertex `i`.
   - **Pieces**: Input the initial number of pieces at each vertex in the format `p1,p2,...` where `pi` is the number of pieces at vertex `i`.

3. **Run the Calculation**: Click the "Run" button to execute the operation. The application will process the input and display the result, which is the maximum number of operations performed.

4. **View Results**: The result will be displayed in the output section of the application.

## Example Usage

- **Input**:
  - Number of Vertices (N): `5`
  - Number of Edges (M): `4`
  - Edges: `0,1;0,2;1,3;2,4`
  - Weights: `10,5,8,3,2`
  - Pieces: `3,0,0,0,0`

- **Output**: The application will display the maximum number of operations that can be performed based on the provided input.

## Support

If you encounter any issues or have questions about using the application, please reach out to our support team at support@chatdev.com.

Thank you for using the ChatDev Graph Operations Application! We hope you find it useful for your graph-related tasks.
```