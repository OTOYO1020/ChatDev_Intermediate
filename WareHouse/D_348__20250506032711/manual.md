```markdown
# Grid Exploration Application

This application allows users to explore a grid-based environment where they can navigate from a start point (S) to a goal point (T) while collecting medicines to replenish energy. The application uses a breadth-first search (BFS) algorithm to determine if reaching the goal is possible given the constraints of energy and obstacles.

## Main Functions

- **Grid Representation**: The application reads a grid of specified dimensions, identifying the start point (S), goal point (T), and obstacles (walls represented by `#`).
- **Medicine Collection**: Users can specify medicines located at certain grid positions that provide energy when collected.
- **Pathfinding**: The application implements a BFS algorithm to explore the grid and determine if the goal can be reached with the available energy and collected medicines.
- **User Input**: The application prompts users for grid dimensions, grid representation, initial energy, and medicine details.

## Installation

To run the application, ensure you have Python installed on your system. You can install the required dependencies using pip. 

1. Open your terminal or command prompt.
2. Run the following command to install any necessary dependencies (if applicable):

   ```bash
   pip install collections
   ```

## How to Use the Application

1. **Run the Application**: Execute the main script to start the application.

   ```bash
   python main.py
   ```

2. **Input Grid Dimensions**: When prompted, enter the height (H) and width (W) of the grid.

   ```
   Enter grid dimensions (H W): 5 5
   ```

3. **Input Grid Representation**: Enter the grid representation row by row. Use `S` for the start point, `T` for the goal point, and `#` for walls. For example:

   ```
   Enter the grid representation (use '#' for walls, 'S' for start, 'T' for goal):
   S....
   .#...
   ..#..
   ...#.
   ...T.
   ```

4. **Input Medicines**: Provide the positions and energy values of the medicines in the format `R C E`, separated by semicolons. For example:

   ```
   Enter medicines (format: R C E; R C E; ...): 1 1 5; 3 0 3
   ```

5. **Input Initial Energy**: Enter the initial energy level for the exploration.

   ```
   Enter initial energy level: 10
   ```

6. **View Results**: The application will output `YES` if reaching the goal is possible with the given energy and medicines; otherwise, it will output `NO`.

## Example Usage

Here is an example of how to use the application:

```
Enter grid dimensions (H W): 5 5
Enter the grid representation (use '#' for walls, 'S' for start, 'T' for goal):
S....
.#...
..#..
...#.
...T.
Enter medicines (format: R C E; R C E; ...): 1 1 5; 3 0 3
Enter initial energy level: 10
YES
```

In this example, the user successfully navigates from the start point to the goal point.

## Conclusion

This application provides a simple yet effective way to explore grid-based environments while managing energy levels and collecting resources. For any issues or further inquiries, please contact the support team.
```