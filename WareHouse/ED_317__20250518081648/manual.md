Here's a detailed user manual for the grid navigation software, formatted in Markdown as requested:

```markdown
# Grid Navigation Software

A Python application for navigating a grid-based field to determine if a goal can be reached from a starting point while avoiding obstacles and the line of sight of persons.

## Main Functions

The Grid Navigation Software provides the following key functionalities:

- **Input Handling**: Accepts a grid input where:
  - 'S' represents the starting point.
  - 'G' represents the goal.
  - '>', '<', 'v', '^' represent persons with specific line of sight.
  - '#' represents obstacles.

- **Line of Sight Calculation**: Automatically marks squares that are in the line of sight of any person in the grid.

- **Breadth-First Search (BFS)**: Implements a BFS algorithm to explore possible moves from the starting point 'S' to determine if the goal 'G' is reachable.

- **Output**: Returns whether the goal is reachable and the minimum number of moves required to reach it.

## Installation

To run the Grid Navigation Software, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

You may need to install the following dependencies:

```bash
pip install typing
```

This will ensure that the necessary type hinting features are available for the application.

## How to Use

1. **Clone the Repository**: If you have the source code, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file to start the grid navigation program.

   ```bash
   python main.py
   ```

3. **Input the Grid**: When prompted, enter the grid line by line. Use the following characters:
   - `S` for the starting point
   - `G` for the goal
   - `>`, `<`, `v`, `^` for persons
   - `#` for obstacles

   Example input:
   ```
   #######
   #S....#
   #.###.#
   #.....G
   #######
   ```

   To finish inputting the grid, simply press Enter on an empty line.

4. **View the Output**: After processing the grid, the application will output whether the goal is reachable and the minimum number of moves required.

   Example output:
   ```
   Goal is reachable in 5 moves.
   ```

## Example

Here’s a quick example of how to use the software:

1. Start the application.
2. Input the following grid:
   ```
   #######
   #S....#
   #.###.#
   #.....G
   #######
   ```
3. The output will indicate:
   ```
   Goal is reachable in 5 moves.
   ```

## Error Handling

- If the grid does not contain both 'S' and 'G', the application will raise an error.
- If the input grid is invalid or empty, the application will prompt you to enter a valid grid.

## Conclusion

This Grid Navigation Software is a powerful tool for exploring grid-based environments. By following the instructions above, you can easily determine the reachability of goals within various grid configurations. For any issues or further inquiries, please refer to the documentation or contact support.

```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, usage guidelines, and error handling. It should serve as a helpful resource for users looking to utilize the grid navigation application effectively.