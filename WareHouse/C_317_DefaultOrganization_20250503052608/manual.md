Here's a detailed user manual for the Road Explorer application, formatted in Markdown as requested:

```markdown
# Road Explorer

Explore the maximum path length between towns connected by roads.

## Overview

The Road Explorer application allows users to input a number of towns and roads, representing a graph structure. It calculates the maximum possible total length of roads traversed using a depth-first search (DFS) algorithm. This application is useful for understanding the connectivity and distance between various towns in a given network.

## Main Functions

- **Set Parameters**: Input the number of towns and roads.
- **Add Roads**: Define the roads connecting the towns along with their lengths.
- **Calculate Maximum Length**: Determine the longest path that can be traversed without revisiting towns.

## Installation

To run the Road Explorer application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application files.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: Ensure you have the necessary dependencies. You can use pip to install any required packages. For this application, no external libraries are required beyond standard Python.
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**: Execute the main application file.
   ```bash
   python main.py
   ```

2. **Input the Number of Towns and Roads**: When prompted, enter two integers separated by a space. The first integer represents the number of towns (N), and the second integer represents the number of roads (M).
   ```
   5 7
   ```

3. **Add Roads**: For each road, input three integers separated by spaces. The first two integers represent the towns connected by the road, and the third integer represents the length of the road.
   ```
   1 2 10
   1 3 15
   2 3 5
   2 4 20
   3 4 10
   4 5 25
   3 5 30
   ```

4. **Calculate Maximum Length**: After entering all roads, the application will automatically calculate and display the maximum path length found.
   ```
   60
   ```

## Example Usage

Here’s a complete example of how to use the application:

```plaintext
$ python main.py
5 7
1 2 10
1 3 15
2 3 5
2 4 20
3 4 10
4 5 25
3 5 30
60
```

## Conclusion

The Road Explorer application is a powerful tool for analyzing the connectivity of towns through roads. By following the installation and usage instructions, users can easily determine the maximum path length in their town-road network.

For any issues or further assistance, please contact support.
```

This manual provides a comprehensive guide for users to understand and utilize the Road Explorer application effectively.