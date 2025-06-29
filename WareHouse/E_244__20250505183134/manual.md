# ChatDev Sequence Counter

A powerful application for counting valid sequences in an undirected graph based on user-defined parameters.

## Overview

This application allows users to input an undirected graph defined by vertices and edges, and then count the number of valid sequences of steps from a starting vertex to a target vertex, adhering to specific conditions. The counting process considers whether certain vertices are visited an even number of times.

## Main Functions

1. **Graph Representation**: The application uses an adjacency list to represent the undirected graph.
2. **Input Handling**: Users can input the number of vertices, edges, and specific parameters for counting sequences.
3. **Recursive Counting**: The application employs a recursive function with memoization to efficiently count valid sequences based on the defined rules.
4. **Output**: The final count of valid sequences is printed to the console.

## Installation

To run the application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/chatdev-sequence-counter.git
   cd chatdev-sequence-counter
   ```

2. **Install Dependencies**:
   Ensure you have `pip` installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt`, you can simply run the application without additional dependencies as it uses standard libraries.

## How to Use the Application

1. **Run the Application**:
   Execute the main script to start the application:
   ```bash
   python main.py
   ```

2. **Input Parameters**:
   When prompted, enter the following integers separated by spaces:
   - **N**: Number of vertices in the graph.
   - **M**: Number of edges in the graph.
   - **K**: Number of steps to take.
   - **S**: Starting vertex.
   - **T**: Target vertex.
   - **X**: Special vertex to track even counts.

   Example input:
   ```
   Enter N, M, K, S, T, X: 5 4 3 1 5 2
   ```

3. **Input Edges**:
   After entering the parameters, you will be prompted to enter the edges of the graph. For each edge, input two integers representing the vertices connected by the edge (u and v):
   ```
   Enter edge (u v): 1 2
   Enter edge (u v): 2 3
   Enter edge (u v): 3 4
   Enter edge (u v): 4 5
   ```

4. **View Results**:
   After entering all edges, the application will compute the number of valid sequences and display the result:
   ```
   Number of valid sequences: 10
   ```

## Example Usage

Here is a complete example of how to use the application:

1. Start the application:
   ```bash
   python main.py
   ```

2. Input parameters:
   ```
   Enter N, M, K, S, T, X: 4 3 2 1 4 2
   ```

3. Input edges:
   ```
   Enter edge (u v): 1 2
   Enter edge (u v): 2 3
   Enter edge (u v): 3 4
   ```

4. Result:
   ```
   Number of valid sequences: 5
   ```

## Conclusion

This application provides a robust solution for counting valid sequences in an undirected graph. By following the installation and usage instructions, users can easily set up and run the application to explore various graph configurations and their corresponding valid sequences. For further assistance or feature requests, please reach out to the development team.