```markdown
# Travel Cost Calculator

A software application designed to calculate maximum travel costs between towns based on road tolls and sightseeing costs.

## Main Functions

The Travel Cost Calculator provides the following key functionalities:

1. **Input Handling**: Accepts user input for the number of towns, roads connecting the towns with toll costs, and sightseeing costs for each town.
2. **Graph Representation**: Constructs a graph using an adjacency list to represent the towns and roads.
3. **Shortest Path Calculation**: Utilizes Dijkstra's algorithm to compute the shortest path between towns, accounting for toll costs.
4. **Maximum Travel Cost Calculation**: For each town, calculates the maximum travel cost to all other towns, including sightseeing costs.
5. **Error Handling**: Provides feedback for invalid inputs and edge cases, such as isolated towns.

## Installation

To run the Travel Cost Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: Open your terminal or command prompt and run the following command to install the required libraries:

   ```bash
   pip install tkinter
   ```

   Note: Tkinter is included with most Python installations, but if you encounter issues, ensure it is installed.

## How to Use the Application

1. **Launch the Application**: Run the `main.py` file to start the Travel Cost Calculator. You can do this by navigating to the directory containing `main.py` in your terminal and executing:

   ```bash
   python main.py
   ```

2. **Input Format**: In the application window, you will see a text box where you can enter the input data. The input should be formatted as follows:

   ```
   N
   A1 B1 C1
   A2 B2 C2
   ...
   D1 D2 ... DN
   ```

   - `N`: The number of towns (an integer).
   - `Ai Bi Ci`: Each line represents a road connecting town `Ai` to town `Bi` with a toll cost `Ci`.
   - `D1 D2 ... DN`: The last line contains the sightseeing costs for each town.

   Example input for 3 towns:
   ```
   3
   1 2 10
   2 3 20
   3 1 15
   5 10 7
   ```

3. **Calculate Travel Costs**: After entering the data, click the "Calculate Travel Costs" button. The application will process the input and display the maximum travel costs for each town in the results text box.

4. **View Results**: The results will indicate the maximum travel costs for each town. If a town is isolated (no roads), it will display "Isolated".

## Error Handling

The application includes error handling for various input issues, such as:

- Insufficient input data.
- Invalid town indices.
- Mismatched number of sightseeing costs.

If an error occurs, an appropriate message will be displayed in the results text box.

## Conclusion

The Travel Cost Calculator is a powerful tool for analyzing travel costs between towns, taking into account both road tolls and sightseeing expenses. With its user-friendly interface and robust functionality, it simplifies the process of calculating travel costs effectively.
```