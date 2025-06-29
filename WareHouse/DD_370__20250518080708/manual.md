Here's a detailed user manual for the Wall Destroyer application, formatted in Markdown:

```markdown
# Wall Destroyer

A simple application to manage and destroy walls in a grid based on user queries.

## Quick Install

To run the Wall Destroyer application, ensure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

The Wall Destroyer application allows users to interact with a grid filled with walls. Users can issue queries to destroy walls at specified coordinates. If a wall is not present at the queried coordinates, the application will search in the four cardinal directions (up, down, left, right) for the first wall to destroy.

### Main Functions

1. **Initialize Grid**: The application initializes a grid of size H x W filled with walls, represented as a 2D list.

2. **Process Queries**: Users can input multiple queries, and the application will process each query to destroy walls based on the specified coordinates.

3. **Count Remaining Walls**: After processing all queries, the application counts and returns the number of remaining walls in the grid.

## 📖 How to Use

1. **Run the Application**: Execute the `main.py` file to start the application.

   ```bash
   python main.py
   ```

2. **Input Parameters**:
   - The application will prompt you to enter the number of queries you wish to make.
   - For each query, input the coordinates in the format `R_q C_q`, where:
     - `R_q` is the row index (1-based).
     - `C_q` is the column index (1-based).

3. **Example Usage**:
   - If you want to destroy walls at coordinates (2, 3) and (4, 1), you would enter:
     ```
     Enter the number of queries: 2
     Enter the query (R_q C_q): 2 3
     Enter the query (R_q C_q): 4 1
     ```

4. **Output**: After processing the queries, the application will display the number of remaining walls in the grid.

## 🛠️ Dependencies

Ensure you have the following dependencies installed:

- Python 3.x
- Any additional libraries specified in `requirements.txt` (if applicable).

## 📄 Additional Information

For further details on the implementation, you can refer to the source code in `grid_manager.py`, which contains the logic for managing the grid and processing wall destruction.

### Example Code Snippet

Here’s a brief overview of how the main functionality is implemented:

```python
def count_remaining_walls(H: int, W: int, Q: int, queries: List[Tuple[int, int]]) -> int:
    # Initialize the grid with walls
    grid = [[1 for _ in range(W)] for _ in range(H)]
    # Process each query
    for R_q, C_q in queries:
        # Logic to destroy walls...
    # Return count of remaining walls
```

## 📞 Support

If you encounter any issues or have questions regarding the Wall Destroyer application, please reach out to our support team for assistance.

```

This manual provides a comprehensive overview of the Wall Destroyer application, including installation instructions, usage guidelines, and additional information about the application's functionality.