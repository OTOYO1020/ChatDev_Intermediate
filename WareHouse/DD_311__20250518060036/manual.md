Here's a detailed user manual for the Ice Square Game application, following the structure you provided:

```markdown
# Ice Square Game

Welcome to the Ice Square Game! This application allows players to navigate a grid, touching unique ice squares while avoiding rocks. 

## Main Functions

- **count_ice_squares(N: int, M: int, grid: List[str]) -> int**: This is the main function that counts the number of unique ice squares touched by the player. The player starts at a specified position and can move in four directions (up, down, left, right) until they hit a rock or go out of bounds.

- **move_player(direction: str, current_position: Tuple[int, int]) -> Tuple[int, int]**: This helper function determines the new position of the player based on the specified direction.

## How to Install Environment Dependencies

To run the Ice Square Game, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a Virtual Environment (Optional but recommended)**:
   ```bash
   python -m venv ice_square_env
   source ice_square_env/bin/activate  # On Windows use `ice_square_env\Scripts\activate`
   ```

3. **Install Required Packages**: Use pip to install any necessary packages. As of now, there are no specific external dependencies required for this application, but you can create a `requirements.txt` file for future needs:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use/Play the Game

1. **Run the Application**: Navigate to the directory where the `main.py` file is located and run the following command:
   ```bash
   python main.py
   ```

2. **Game Instructions**:
   - The game starts with a grid displayed in the console.
   - You will begin at the initial position of ice (marked as 'I').
   - You can enter one of the following commands to move:
     - `up`: Move one square up.
     - `down`: Move one square down.
     - `left`: Move one square left.
     - `right`: Move one square right.
   - If you hit a rock (marked as 'R'), the game will stop your movement in that direction.
   - You can type `exit` at any time to stop the game.

3. **Game Output**: After you finish moving, the game will display the total number of unique ice squares you have touched.

## Example Grid

Here is an example grid you might encounter when you run the game:

```
RRRRR
RIIII
RIIII
RIRRR
RRRRR
```

In this grid:
- 'R' represents rocks.
- 'I' represents ice squares.

## Conclusion

Enjoy navigating through the Ice Square Game! If you have any questions or need further assistance, feel free to reach out for support.
```

This manual provides a comprehensive overview of the Ice Square Game, including installation instructions, gameplay mechanics, and an example grid. Let me know if you need any modifications or additional information!