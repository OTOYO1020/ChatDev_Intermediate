Here's a detailed user manual for the `count_connected_red_paintings` software, formatted in Markdown:

```markdown
# Count Connected Red Paintings

A Python application to count the number of valid combinations of squares that can be painted red in a grid while ensuring they form a connected component.

## Quick Install

To run this application, you need to have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install itertools
```

## 🤔 What is this?

This application allows users to define a grid of squares, where each square can either be white (represented by '.') or another color (represented by '#'). The main functionality is to count how many ways you can paint a specified number of white squares red such that they are all connected.

### Main Functions

1. **Input Parameters**:
   - `N`: The size of the grid (N x N).
   - `K`: The number of squares to paint red.
   - `S`: A list of strings representing the grid.

2. **Functionality**:
   - Parse the input to extract the grid size, number of squares to paint, and the grid itself.
   - Identify all white squares in the grid and store their coordinates.
   - Generate all combinations of K white squares from the identified list.
   - Check if each combination forms a connected component using BFS.
   - Count and return the number of valid combinations.

3. **Error Handling**:
   - Handles cases where K is greater than the number of available white squares.
   - Validates grid size and content.

## How to Use

1. **Run the Application**:
   - Execute the main application file `main.py` in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input the Grid**:
   - When prompted, enter the grid size (N).
   - Enter the number of squares to paint (K).
   - Input the grid row by row, using '.' for white squares and '#' for others.

   Example Input:
   ```
   Enter grid size (N): 4
   Enter number of squares to paint (K): 2
   Enter the grid (use '.' for white squares and '#' for others, one row per line):
   ....
   .##.
   .#..
   ....
   ```

3. **View Results**:
   - The application will output the number of valid combinations of squares that can be painted red.

## Example Usage

```bash
Enter grid size (N): 4
Enter number of squares to paint (K): 2
Enter the grid (use '.' for white squares and '#' for others, one row per line):
....
.##.
.#..
....
Valid combinations: 3
```

## 📖 Documentation

For more detailed information about the code structure and functions, refer to the source files:

- **main.py**: The entry point of the application.
- **grid.py**: Contains the `Grid` class for managing grid operations and connectivity checks.
- **utils.py**: Contains the `count_connected_red_paintings` function for counting combinations and checking connectivity.

## Support

If you encounter any issues or have questions, please reach out to our support team for assistance.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and examples to help users effectively utilize the application.