Here's a detailed user manual for the graph simulator application, formatted in Markdown as requested:

```markdown
# Graph Simulator

A simple application to calculate the expected number of operations until a graph becomes connected.

## Introduction

The Graph Simulator allows users to input the number of vertices in a graph and calculates the expected number of operations required to connect all vertices. This application is useful for understanding the dynamics of graph connectivity and the probabilistic nature of connecting vertices.

## Main Functions

- **expected_operations(N: int) -> float**: This function calculates the expected number of operations until the graph becomes connected based on the number of vertices (N) provided by the user.

## Installation

To run the Graph Simulator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the Graph Simulator code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: If there are any additional dependencies required, you can install them using pip. For this application, no external libraries are needed, but ensure you have the latest version of Python.
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**: Open your terminal or command prompt, navigate to the directory where the `main.py` file is located, and run the following command:
   ```bash
   python main.py
   ```

2. **Input the Number of Vertices**: When prompted, enter a positive integer value for N (the number of vertices in the graph). For example:
   ```
   Enter number of vertices (N): 5
   ```

3. **View the Result**: The application will calculate the expected number of operations required to connect all vertices and display the result formatted to two decimal places. For example:
   ```
   Expected Operations: 8.00
   ```

## Example Usage

Here’s a quick example of how to use the Graph Simulator:

1. Start the application:
   ```bash
   python main.py
   ```

2. Input the number of vertices:
   ```
   Enter number of vertices (N): 4
   ```

3. Output:
   ```
   Expected Operations: 5.33
   ```

## Conclusion

The Graph Simulator provides a straightforward way to explore the expected number of operations needed to connect a graph. By adjusting the number of vertices, users can gain insights into the connectivity dynamics of graphs.

For any questions or support, please contact the development team.
```

This manual provides a comprehensive overview of the Graph Simulator application, including installation instructions, usage guidelines, and examples to help users effectively utilize the software.