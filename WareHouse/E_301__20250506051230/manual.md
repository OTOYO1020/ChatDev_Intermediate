Here's a detailed user manual for the grid candy collection game software, formatted in Markdown:

```markdown
# Grid Candy Collection Game

Welcome to the Grid Candy Collection Game! This application allows users to navigate a grid, collect candies, and reach a goal within a specified number of moves.

## Main Functions

1. **Grid Initialization**: The application initializes a grid of size H x W, where H is the height and W is the width. The grid is populated with characters representing different squares:
   - `S`: Start square
   - `G`: Goal square
   - `o`: Candy square
   - `.`: Empty square
   - `#`: Wall square

2. **Pathfinding**: The application implements a pathfinding algorithm (BFS) to determine if the goal can be reached from the start square within T moves while counting the number of candies collected along the way.

3. **Candy Collection**: As the player navigates the grid, the application tracks the number of candies collected during the pathfinding process.

4. **Output**: The application returns the maximum number of candies collected if the goal is reachable within T moves; otherwise, it returns -1.

## Installation

To set up the environment for the Grid Candy Collection Game, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   This project does not require any additional packages beyond the standard Python library. However, if you want to keep it open for future scalability, you can create a `requirements.txt` file with common libraries that might be used later.

   To create a virtual environment and install dependencies, you can use:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Run the Application**:
   After setting up the environment, you can run the application using:
   ```bash
   python main.py
   ```

## How to Use/Play

1. **Input Format**:
   - The first line of input should contain three integers: H (height), W (width), and T (maximum moves).
   - The next H lines should contain W characters each, representing the grid.

   Example Input:
   ```
   5 5 10
   S....
   .#...
   ..o..
   .#o..
   ...G.
   ```

2. **Understanding the Grid**:
   - The grid will be displayed in the console as you input it.
   - Ensure that the start (S) and goal (G) squares are not placed on walls (#).

3. **Output**:
   - After inputting the grid, the application will process the data and output the maximum number of candies collected if the goal is reachable within T moves, or -1 if it is not.

## Example Usage

To run the application, follow these steps:

1. Start the application:
   ```bash
   python main.py
   ```

2. Input the grid dimensions and the grid itself:
   ```
   5 5 10
   S....
   .#...
   ..o..
   .#o..
   ...G.
   ```

3. The application will output the result:
   ```
   2
   ```

This indicates that the maximum number of candies collected while reaching the goal is 2.

## Conclusion

The Grid Candy Collection Game is a fun and engaging way to explore pathfinding algorithms while collecting candies. Feel free to modify the grid and experiment with different configurations to see how many candies you can collect!

For any further questions or support, please reach out to our development team.
```

This manual provides a comprehensive overview of the software, including its functionality, installation instructions, and usage guidelines.