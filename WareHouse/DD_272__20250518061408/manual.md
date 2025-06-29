Here is the user manual for the grid reachability program using BFS, formatted in Markdown:

```markdown
# Grid Reachability Program

This software allows users to determine the reachability of squares in a grid using a breadth-first search (BFS) algorithm. The program calculates the minimum number of operations required to reach each square from the starting position (1, 1) based on a specified distance squared.

## Main Functions

- **canReach(N: int, M: int) -> List[Tuple[int, int, bool, int]]**: This function takes the size of the grid (N) and the distance squared (M) as input parameters. It returns a list of tuples for each square in the grid, indicating whether it can be reached and the minimum number of operations required.

## Installation

To run the Grid Reachability Program, you need to have Python installed on your machine. You can install the required dependencies using pip. 

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   *(Note: If there are no specific dependencies listed, you can skip this step.)*

## How to Use

1. **Run the main application**:
   Execute the `main.py` file to start the program:
   ```bash
   python main.py
   ```

2. **Input Parameters**:
   - When prompted, enter the grid size (N) as a positive integer.
   - Enter the distance squared (M) as a non-negative integer.

3. **Output**:
   The program will display the reachability status and minimum operations for each square in the grid in the following format:
   ```
   (i, j): Reachable: <True/False>, Min Operations: <number>
   ```

   Where:
   - `(i, j)` represents the coordinates of the square.
   - `Reachable` indicates if the square can be reached from the starting position.
   - `Min Operations` shows the minimum number of operations required to reach the square, or `-1` if it is not reachable.

## Example Usage

```plaintext
Enter grid size (N): 5
Enter distance squared (M): 2
(1, 1): Reachable: True, Min Operations: 0
(1, 2): Reachable: True, Min Operations: 1
(1, 3): Reachable: False, Min Operations: -1
...
```

## Additional Information

- The BFS algorithm ensures that all reachable squares are processed efficiently.
- The program handles edge cases, such as when M is zero or negative, providing appropriate outputs.

For any further questions or support, please contact the development team.
```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, usage guidelines, and example outputs. Let me know if you need any modifications or additional information!