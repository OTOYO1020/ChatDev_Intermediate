Here's a detailed user manual for the Takahashi Punches Calculator software, formatted in Markdown:

```markdown
# Takahashi Punches Calculator

A tool to calculate the minimum number of punches needed for Takahashi to navigate through a grid to reach the fish market.

## Quick Install

To run the Takahashi Punches Calculator, you need to have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

Make sure to create a `requirements.txt` file with the following content:

```
collections
typing
```

## 🤔 What is this?

The Takahashi Punches Calculator is designed to help users determine the minimum number of punches needed for Takahashi to move from the top-left corner of a grid to the bottom-right corner. The grid consists of passable cells (represented by '.') and blocked cells (represented by '#'). Takahashi can clear blocked cells by punching 2x2 blocks of cells.

### Main Functions

1. **Input Parsing**: The program reads the height (H) and width (W) of the grid and the grid itself as a list of strings.
2. **Passability Check**: It checks if a cell is passable based on its current state in the grid.
3. **Punching Mechanism**: It simulates punching to clear 2x2 blocks of blocked cells.
4. **Movement Simulation**: It uses a breadth-first search (BFS) algorithm to explore all possible paths from the starting cell to the target cell while keeping track of the number of punches used.
5. **Output**: The program returns the minimum number of punches needed to reach the fish market.

## 📖 How to Use

1. **Run the Application**: Execute the `main.py` file in your terminal or command prompt:

   ```bash
   python main.py
   ```

2. **Input the Grid Dimensions**: When prompted, enter the height (H) and width (W) of the grid.

   ```
   Enter Height (H): 4
   Enter Width (W): 4
   ```

3. **Input the Grid**: Enter the grid configuration, with each row on a new line. For example:

   ```
   Enter Grid (each row on a new line):
   ....
   ..#.
   ..#.
   ....
   ```

4. **View the Result**: After entering the grid, the program will calculate and display the minimum number of punches needed.

   ```
   Minimum Punches Needed: 1
   ```

## 🛠️ Example

Here’s an example of how to use the application:

1. Start the application:

   ```bash
   python main.py
   ```

2. Input the following when prompted:

   ```
   Enter Height (H): 4
   Enter Width (W): 4
   Enter Grid (each row on a new line):
   ....
   ..#.
   ..#.
   ....
   ```

3. The output will show:

   ```
   Minimum Punches Needed: 1
   ```

## 📄 Additional Information

For more detailed information about the code structure and logic, refer to the `logic.py` file, which contains the core functionality of the application.

If you encounter any issues or have questions, please reach out for support.

```

This manual provides a comprehensive overview of the Takahashi Punches Calculator, including installation instructions, usage guidelines, and examples to help users effectively utilize the software.