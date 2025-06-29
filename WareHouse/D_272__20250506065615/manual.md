Here's a detailed user manual for the grid reachability application, formatted in Markdown as requested:

```markdown
# Grid Reachability Application

This application allows users to determine the reachability of squares in a grid based on a specified distance squared for movement. It provides a graphical user interface (GUI) for easy interaction and visualization of results.

## Main Functions

- **Grid Initialization**: Users can input the size of the grid (N) and the distance squared (M) for movement.
- **Reachability Calculation**: The application calculates which squares in the grid can be reached from the starting position (1, 1) based on the movement constraints defined by M.
- **Minimum Operations Count**: It tracks the minimum number of operations required to reach each square from the starting position.
- **Visualization**: The results are displayed in a user-friendly format, showing both the reachable grid and the minimum operations grid.

## Installation

To run the Grid Reachability application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have the code in a repository, clone it using:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: Use pip to install the required dependencies. Open your terminal or command prompt and run:
   ```bash
   pip install tkinter
   ```

   Note: `tkinter` is included with standard Python installations, but if you encounter issues, ensure it is installed.

## How to Use the Application

1. **Run the Application**: Navigate to the directory where the application files are located and run the main application file:
   ```bash
   python main.py
   ```

2. **Input Values**:
   - Enter the grid size (N) in the provided input field.
   - Enter the distance squared (M) in the corresponding input field.

3. **Calculate Reachability**: Click the "Calculate" button to process the input values. The application will compute the reachable squares and the minimum operations required.

4. **View Results**: The results will be displayed in the application window:
   - **Reachable Grid**: Indicates which squares can be reached from the starting position.
   - **Minimum Operations**: Shows the minimum number of moves required to reach each square.

5. **Close the Application**: Once you are done, you can close the application window.

## Example Usage

- **Grid Size (N)**: 5
- **Distance Squared (M)**: 2

After entering these values and clicking "Calculate", the application will display the reachable grid and the minimum operations grid based on the specified parameters.

## Additional Information

For any issues or questions, please refer to the documentation or contact support for assistance.

```

This manual provides a comprehensive overview of the application, including its functionality, installation instructions, and usage guidelines. Let me know if you need any further modifications or additional information!