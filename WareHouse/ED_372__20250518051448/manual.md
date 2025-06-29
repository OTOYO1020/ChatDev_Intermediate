Here's a detailed user manual for the graph query application, formatted in Markdown:

```markdown
# Graph Query Application

A powerful tool for managing and querying undirected graphs through a user-friendly interface.

## Main Functions

The Graph Query Application allows users to:

- **Add Edges**: Create connections between vertices in the graph.
- **Query Connected Vertices**: Retrieve and sort vertices connected to a specified vertex, and find the k-th largest vertex among them.
- **Error Handling**: Receive informative error messages for invalid operations, such as adding edges between non-existent vertices or querying non-existent vertices.

## Installation

To run the Graph Query Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: Open your terminal or command prompt and run the following command to install the required libraries:
   ```bash
   pip install tkinter
   ```

## How to Use the Application

### Running the Application

1. **Clone the Repository**: Download or clone the repository containing the application files (`main.py`, `graph.py`, `query_processor.py`, and `app.py`).

2. **Navigate to the Directory**: Open your terminal and navigate to the directory where the application files are located.

3. **Run the Application**: Execute the following command to start the application:
   ```bash
   python app.py
   ```

### Using the Graph Query Application

1. **Enter Number of Vertices**: In the GUI, input the number of vertices in the graph. This will initialize the graph structure.

2. **Input Queries**: 
   - Type 1 queries should be formatted as: `1 u v` (where `u` and `v` are the vertices you want to connect).
   - Type 2 queries should be formatted as: `2 v k` (where `v` is the vertex you want to query, and `k` is the rank of the largest vertex you want to retrieve).

   Example input:
   ```
   1 1 2
   1 2 3
   2 2 1
   2 1 2
   ```

3. **Submit Queries**: Click the "Submit Queries" button to process the input queries.

4. **View Results**: The results of Type 2 queries will be displayed in a pop-up window. If there are no results or if an error occurs, appropriate messages will be shown.

### Example Usage

- To create edges between vertices 1 and 2, and 2 and 3, and then query the largest connected vertex to vertex 2:
   ```
   1 1 2
   1 2 3
   2 2 1
   ```

- The application will output the largest connected vertex to vertex 2.

## Error Handling

The application includes error handling for the following scenarios:

- Attempting to add an edge between non-existent vertices.
- Querying a vertex that does not exist.
- Requesting the k-th largest vertex when there are not enough connected vertices.

In such cases, informative error messages will be displayed.

## Conclusion

The Graph Query Application is a versatile tool for managing and querying undirected graphs. With its intuitive GUI and robust functionality, users can easily manipulate graph structures and retrieve valuable information.

For further assistance or feature requests, please contact the development team.
```

This user manual provides a comprehensive overview of the application, including its main functions, installation instructions, usage guidelines, and error handling.