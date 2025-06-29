Here's a detailed user manual for the maze application, formatted in Markdown:

```markdown
# Maze Max Moves Calculator

A simple application to calculate the maximum number of moves between road squares in a maze represented by a grid of characters.

## Main Functions

The Maze Max Moves Calculator provides the following functionalities:

- **Input Maze Dimensions**: Users can input the height (H) and width (W) of the maze.
- **Input Maze Representation**: Users can enter the maze layout, where `.` represents a road square and `#` represents a wall.
- **Calculate Maximum Moves**: The application calculates the maximum number of moves required to travel between any two road squares in the maze.
- **Error Handling**: The application includes error handling for invalid inputs, ensuring the maze is correctly formatted.

## Installation

To run the Maze Max Moves Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: Open your terminal or command prompt and run the following command to install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file, you can manually install the necessary packages (if any) using:

   ```bash
   pip install collections
   ```

## How to Use the Application

1. **Run the Application**: Execute the main script to start the application.

   ```bash
   python main.py
   ```

2. **Input Maze Dimensions**: When prompted, enter the maze dimensions in the format `H W`, where `H` is the number of rows and `W` is the number of columns. For example:

   ```
   Enter maze dimensions (H W): 5 5
   ```

3. **Input Maze Representation**: Enter the maze rows one by one. Each row should contain exactly `W` characters, consisting of `.` (road) and `#` (wall). For example:

   ```
   Enter maze rows (one per line):
   ....#
   #..#.
   ..#..
   #..#.
   ....#
   ```

4. **Calculate Max Moves**: After entering the maze representation, the application will calculate and display the maximum number of moves between any two road squares.

5. **Error Handling**: If there are any errors in the input (e.g., invalid dimensions, incorrect characters), the application will display an error message.

## GUI Version

For users who prefer a graphical interface, a GUI version of the application is available. To run the GUI version, execute the following command:

```bash
python gui.py
```

In the GUI:

- Enter the maze dimensions in the provided text box.
- Input the maze layout in the text area.
- Click the "Calculate Max Moves" button to see the result.

## Conclusion

The Maze Max Moves Calculator is a straightforward tool for analyzing maze structures and determining the maximum distance between road squares. Whether using the command line or the GUI, users can easily interact with the application and receive accurate results.

For any issues or feature requests, please reach out to the development team.
```

This manual provides a comprehensive overview of the maze application, including its main functions, installation instructions, and usage guidelines.