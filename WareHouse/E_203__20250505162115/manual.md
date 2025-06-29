Here's a detailed user manual for the software that implements the pawn position calculator. This manual includes an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# Pawn Position Calculator

A simple application to calculate the reachable positions for a white pawn on a grid, considering the positions of black pawns.

## Main Functions

The Pawn Position Calculator allows users to:

- Input the size of the grid (N) and the number of black pawns (M).
- Enter the positions of the black pawns on the grid.
- Calculate the number of valid Y positions for a white pawn located at (2N, Y) that are reachable based on the movement rules and the positions of the black pawns.
- Output the total count of reachable Y positions.

## Quick Install

To run the Pawn Position Calculator, you need to have Python installed on your system. You can install the required dependencies using pip. 

```bash
pip install -r requirements.txt
```

Make sure to create a `requirements.txt` file with the necessary dependencies if you haven't already.

## 🤔 What is this?

The Pawn Position Calculator is designed to help users determine how many positions a white pawn can move to on a grid while avoiding black pawns. The application uses a grid-based approach to check for reachable positions based on the rules of pawn movement in chess.

## 📖 Usage Instructions

### Step 1: Run the Application

To start the application, run the following command in your terminal:

```bash
python main.py
```

### Step 2: Input the Grid Size and Black Pawns

The application will prompt you to enter the grid size (N) and the number of black pawns (M):

```
Enter grid size (N): 
Enter number of black pawns (M): 
```

### Step 3: Enter Black Pawn Positions

For each black pawn, you will be prompted to enter its position in the format `X,Y`. Ensure that the input follows this format, where X and Y are integers representing the coordinates on the grid.

```
Enter black pawn position (X,Y): 
```

If you enter an invalid format or a duplicate position, the application will notify you and prompt you to enter the position again.

### Step 4: View the Results

After entering all the black pawn positions, the application will calculate and display the number of reachable Y positions for the white pawn:

```
Reachable Y positions: [count]
```

## Error Handling

The application includes error handling for various input scenarios, including:

- Invalid input format for pawn positions.
- Duplicate black pawn positions.
- Out-of-bounds positions for black pawns.
- Negative values for grid size or number of black pawns.

## Conclusion

The Pawn Position Calculator is a straightforward tool for calculating reachable positions for a white pawn on a chess-like grid. By following the instructions above, users can easily set up and use the application to explore different configurations of black pawns and their impact on the white pawn's movement.

For any issues or further inquiries, please contact the support team.
```

This manual provides a comprehensive guide for users to understand and effectively utilize the Pawn Position Calculator software.