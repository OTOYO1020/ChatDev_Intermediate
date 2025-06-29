Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Minimum Actions Console Application

A Python application designed to calculate the minimum number of actions required to move between cells in a grid representation based on specified lower and upper bounds.

## Main Functions

The application provides the following main functionalities:

- **Input Parsing**: Accepts user input for the number of cells, lower and upper bounds, number of queries, and the queries themselves.
- **Grid Initialization**: Constructs a grid based on the provided lower and upper bounds, marking empty cells and wall cells.
- **Pathfinding**: Implements a breadth-first search (BFS) algorithm to determine the minimum number of actions required to move from a starting cell to a target cell.
- **Query Handling**: Processes multiple queries and returns the results indicating the minimum actions for each query.

## Quick Install

To run the application, ensure you have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can manually install the necessary libraries (if any) that are used in the code.

## How to Use the Application

1. **Run the Application**: Execute the main application file `main.py` in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Data**: Follow the prompts to enter the required data:
   - **Number of cells (N)**: Enter an integer representing the number of rows in the grid.
   - **Lower bounds (L)**: Enter a space-separated list of integers representing the lower bounds for each row.
   - **Upper bounds (U)**: Enter a space-separated list of integers representing the upper bounds for each row.
   - **Number of queries (Q)**: Enter an integer representing the number of queries you want to process.
   - **Queries**: For each query, enter the starting and target cell coordinates in the format `s_x s_y t_x t_y`.

3. **View Results**: After entering all the data, the application will process the queries and output the results, indicating the minimum number of actions required for each query.

## Example Usage

Here’s an example of how to use the application:

```plaintext
Number of cells (N): 3
Lower bounds (L): 1 0 2
Upper bounds (U): 3 2 4
Number of queries (Q): 2
Query (format: s_x s_y t_x t_y): 0 1 1 1
Query (format: s_x s_y t_x t_y): 0 2 2 3
```

### Expected Output

```plaintext
Results: 1, -1
```

In this example:
- The first query indicates that it takes 1 action to move from cell (0, 1) to (1, 1).
- The second query indicates that it is not possible to reach the target cell (2, 3) from the starting cell (0, 2).

## Edge Cases

- If the starting and target cells are the same, the application will return `0` as no actions are required.
- If either the starting or target cell is a wall or out of bounds, the application will return `-1`, indicating that the target is unreachable.

## Support

For any issues or questions regarding the application, please reach out to our support team through the provided contact channels.

```

This manual provides a comprehensive guide for users to understand how to install, run, and interact with the Minimum Actions Console Application.