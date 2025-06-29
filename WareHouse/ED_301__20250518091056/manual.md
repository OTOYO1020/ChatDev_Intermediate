Here is the `manual.md` file for the Candy Collector game, detailing the main functions, installation instructions, and usage guidelines:

```markdown
# Candy Collector Game

A fun and engaging game where players navigate a grid to collect candies while reaching a goal.

## Main Functions

The Candy Collector game includes the following key functionalities:

- **Grid Navigation**: Players can move through a grid represented by a 2D list, where each cell can be a start point ('S'), goal ('G'), candy ('o'), or a wall ('#').
- **Candy Collection**: Players can collect candies as they navigate the grid, with a maximum limit of 18 unique candies.
- **Pathfinding**: The game uses a breadth-first search (BFS) algorithm to explore all possible paths from the start square to the goal square, ensuring that the player can reach the goal within a specified number of moves.
- **Move Limitation**: Players can only make a limited number of moves (T) to reach the goal, adding a strategic element to the gameplay.

## Installation

To run the Candy Collector game, you need to set up your Python environment and install the necessary dependencies. Follow these steps:

1. **Install Python**: Ensure you have Python 3.6 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the game files to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: Use pip to install any required dependencies. The game currently does not have external dependencies, but ensure you have the standard library available.
   ```bash
   pip install -r requirements.txt
   ```

## How to Use/Play

1. **Prepare the Input**: The game requires input in a specific format. Create a text file or provide input through standard input with the following structure:
   - The first line contains the maximum number of moves (T).
   - The subsequent lines represent the grid, where:
     - 'S' is the start square.
     - 'G' is the goal square.
     - 'o' represents candy squares.
     - '#' represents walls.
     - '.' represents empty squares.

   Example input:
   ```
   10
   S.......
   .#..#..G
   ..o#o...
   ..o#....
   ```

2. **Run the Game**: Execute the main application file to start the game.
   ```bash
   python main.py < input.txt
   ```
   Alternatively, you can run the script and provide input directly in the terminal.

3. **View the Output**: After running the game, you will see output indicating whether the goal is reachable and the number of candies collected.
   - If the goal is reachable: `Goal is reachable! Candies collected: X`
   - If the goal is not reachable: `Goal is not reachable.`

## Conclusion

The Candy Collector game is an exciting way to challenge your pathfinding skills while collecting candies. Enjoy navigating the grid and strategizing your moves to reach the goal!

For any issues or further assistance, please contact our support team.
```

This manual provides a comprehensive overview of the Candy Collector game, ensuring users can easily understand how to install and play the game effectively.