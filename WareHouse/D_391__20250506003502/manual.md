```markdown
# Block Simulation Application

Welcome to the Block Simulation Application! This software allows users to simulate the downward movement of blocks in a defined space and query their positions at specific times. 

## Main Functions

- **Input Handling**: Read integers N (number of blocks), W (simulation width), and Q (number of queries) from standard input.
- **Block Management**: Store initial positions of blocks and track their final positions after simulating downward movement.
- **Query Processing**: Check if a block exists at a specified time and return results.
- **Graphical User Interface (GUI)**: Provides an interactive way to input data and view results.

## Installation

To run the Block Simulation Application, you need to have Python installed on your machine. Follow the steps below to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: Use pip to install the required libraries. Open your terminal or command prompt and run:

   ```bash
   pip install tkinter
   ```

   Note: `tkinter` is included with standard Python installations on Windows and macOS. If you're using Linux, you may need to install it separately.

## How to Use the Application

### Running the Application

1. **Command Line Interface (CLI)**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the `main.py` file is located.
   - Run the application using the command:

     ```bash
     python main.py
     ```

   - Follow the prompts to enter the number of blocks, simulation width, and queries.

2. **Graphical User Interface (GUI)**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the `app.py` file is located.
   - Run the application using the command:

     ```bash
     python app.py
     ```

   - Use the GUI to input the number of blocks, their positions, and run simulations or queries.

### Input Format

- **For Blocks**: Enter the position of each block as pairs of integers (X, Y) where:
  - `X` is the horizontal position (0 to W-1).
  - `Y` is the vertical position (0 or greater).
  
- **For Queries**: Enter the block ID and time as pairs of integers (A, T) where:
  - `A` is the block ID (1 to N).
  - `T` is the time (0 or greater).

### Example Usage

1. **CLI Example**:
   ```
   Enter N, W, Q: 3 5 2
   Enter position for block 1 (X Y): 1 0
   Enter position for block 2 (X Y): 2 1
   Enter position for block 3 (X Y): 3 0
   Enter query 1 (A T): 1 1
   Enter query 2 (A T): 2 2
   ```

2. **GUI Example**:
   - Enter `3` for the number of blocks.
   - Enter `5` for the simulation height.
   - Add block positions (e.g., `1 0`, `2 1`, `3 0`).
   - Click "Simulate" to run the simulation.
   - Enter queries like `1 1` and `2 2` to check block positions.

## Conclusion

The Block Simulation Application provides a powerful way to visualize and simulate block movements in a defined space. Whether using the command line or the GUI, users can easily input data and receive results for their queries. Enjoy exploring the world of block simulations!
```