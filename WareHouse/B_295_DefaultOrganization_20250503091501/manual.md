Here's a detailed user manual for the Bomb Explosion application, formatted in Markdown:

```markdown
# Bomb Explosion Application

Simulate bomb explosions on a grid-based board.

## Overview

The Bomb Explosion application allows users to simulate the effects of bombs placed on a grid. Each bomb has a specific power that determines how far its explosion will reach. The application reads a grid configuration from the user, processes the bomb explosions, and outputs the final state of the board.

## Main Functions

- **Input Handling**: Read the dimensions of the board and the initial state from the user.
- **Board Population**: Populate the board with characters representing bombs, walls, and empty spaces.
- **Explosion Simulation**: Calculate the effects of bomb explosions based on their power and update the board accordingly.
- **Output**: Display the final state of the board after all explosions have occurred.

## Installation

To run the Bomb Explosion application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: If there are any additional dependencies required, install them using pip. For this application, no external libraries are needed beyond Python's standard library.

## Usage

To use the Bomb Explosion application, follow these steps:

1. **Run the Application**: Execute the main script.
   ```bash
   python main.py
   ```

2. **Input the Board Dimensions**: When prompted, enter the number of rows (R) and columns (C) of the board, separated by a space. For example:
   ```
   5 5
   ```

3. **Input the Board State**: Enter R lines of input, each containing C characters. Use:
   - `.` for empty spaces,
   - `#` for walls,
   - `1` to `9` for bombs with corresponding power levels.
   
   Example input:
   ```
   .....
   ..#..
   .1#..
   ..#..
   .....
   ```

4. **View the Result**: After entering the board state, the application will process the explosions and print the final state of the board, showing which cells are empty and which remain unchanged.

## Example

### Input
```
5 5
.....
..#..
.1#..
..#..
.....
```

### Output
```
.....
.....
.....
..#..
.....
```

## Error Handling

If the input dimensions do not match the specified R and C, or if any other error occurs during execution, an error message will be displayed in the standard error output.

## Conclusion

The Bomb Explosion application provides a simple yet effective way to visualize the effects of bomb explosions on a grid. By following the instructions above, users can easily set up and run the application to simulate various scenarios.
```

This manual provides a comprehensive guide for users to understand the application, its functionality, and how to use it effectively.