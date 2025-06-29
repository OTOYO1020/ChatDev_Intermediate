Here's a detailed user manual for the Safe Squares application, formatted in Markdown:

```markdown
# Safe Squares Application

The Safe Squares application allows users to calculate the number of safe squares on a grid where new pieces can be placed without being captured by existing pieces. This application is particularly useful for games involving grid-based strategies.

## Main Functions

The primary function of the Safe Squares application is `count_safe_squares(N: int, M: int, pieces: List[Tuple[int, int]])`. This function takes the following parameters:

- **N**: The size of the grid (N x N).
- **M**: The number of pieces currently on the grid.
- **pieces**: A list of tuples representing the coordinates of the pieces on the grid.

The function calculates the number of squares that are not attacked by any of the existing pieces, allowing users to determine safe placements for new pieces.

## Installation

To run the Safe Squares application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Create a virtual environment (optional but recommended) and install the required dependencies. You can use `pip` to install any future dependencies as needed.

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file yet, you can create one with the following content:
   ```
   # Placeholder for future dependencies
   ```

## How to Use the Application

1. **Run the Application**:
   Execute the `main.py` file to start the application.

   ```bash
   python main.py
   ```

2. **Input Parameters**:
   - When prompted, enter the grid size (N). For example, if you want a 5x5 grid, enter `5`.
   - Next, input the coordinates of the pieces in the format `x1,y1 x2,y2 ...`. For example, if you have pieces at (1, 2) and (3, 4), you would enter `1,2 3,4`.

3. **View Results**:
   After entering the parameters, the application will calculate and display the number of safe squares where a new piece can be placed.

## Example Usage

```
Enter Grid Size (N): 5
Enter Pieces (format: x1,y1 x2,y2 ...): 1,2 3,4
Safe Squares: 16
```

In this example, a 5x5 grid with pieces at (1, 2) and (3, 4) results in 16 safe squares.

## Error Handling

The application includes basic error handling for input validation. If you enter invalid coordinates (outside the grid size), the application will raise a `ValueError` and inform you of the issue.

## Conclusion

The Safe Squares application is a straightforward tool for determining safe placements on a grid. It can be utilized in various grid-based strategy games and can be extended for additional functionalities in the future.
```

This manual provides a comprehensive overview of the Safe Squares application, including its main functions, installation instructions, usage guidelines, and error handling. It serves as a helpful resource for users to effectively utilize the software.