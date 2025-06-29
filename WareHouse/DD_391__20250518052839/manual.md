```markdown
# Block Simulation Application

Welcome to the Block Simulation Application! This software allows users to simulate the movement of blocks in a grid based on user-defined parameters and queries. 

## Main Functions

The Block Simulation Application consists of several key components:

1. **Block Movement Simulation**: The application simulates the movement of blocks over time, allowing users to see how blocks interact with each other and the grid boundaries.

2. **Query Handling**: Users can query the existence of specific blocks at given times, allowing for dynamic interaction with the simulation.

3. **Graphical User Interface (GUI)**: The application provides a user-friendly interface for inputting parameters and viewing results.

## Installation

To run the Block Simulation Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: Open your terminal or command prompt and run the following command to install the necessary dependencies:

   ```bash
   pip install tkinter
   ```

   Note: `tkinter` is included with most Python installations, but if you encounter issues, please refer to the [tkinter documentation](https://docs.python.org/3/library/tkinter.html) for installation instructions.

## How to Use the Application

1. **Run the Application**: Navigate to the directory where the application files are located and run the following command:

   ```bash
   python gui.py
   ```

2. **Input Parameters**: In the GUI, you will see several input fields:

   - **Number of Blocks (N)**: Enter the total number of blocks you want to simulate.
   - **Number of Columns (W)**: Enter the width of the grid.
   - **Blocks (x,y)**: Input the initial positions of the blocks as a list of tuples, e.g., `[(0, 0), (1, 1), (2, 2)]`.
   - **Number of Queries (Q)**: Enter the number of queries you want to perform.
   - **Queries (index,time)**: Input the queries as a list of tuples, e.g., `[(0, 1), (1, 2)]`.

3. **Run Simulation**: Click the "Run Simulation" button to execute the simulation based on the provided parameters.

4. **View Results**: The results of the queries will be displayed in the output text area. Each result will indicate whether the specified block exists at the queried time.

## Example Usage

- **Input**:
  - Number of Blocks (N): `5`
  - Number of Columns (W): `5`
  - Blocks (x,y): `[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]`
  - Number of Queries (Q): `3`
  - Queries (index,time): `[(0, 1), (1, 2), (2, 3)]`

- **Output**:
  - The application will simulate the movement of the blocks and return whether each queried block exists at the specified time.

## Error Handling

The application includes input validation to ensure that all parameters are within acceptable ranges. If any input is invalid, an error message will be displayed in the GUI.

## Conclusion

The Block Simulation Application is a powerful tool for visualizing block movements and interactions in a grid. We hope you enjoy using it and find it useful for your simulations!

For further assistance or feedback, please contact our support team.
```