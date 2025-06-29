```markdown
# Path Counting Application

This application allows users to count the number of distinct shortest paths between cities connected by roads. It utilizes a breadth-first search (BFS) algorithm to efficiently compute the result while handling large numbers through modular arithmetic.

## Main Functions

- **count_paths(N: int, M: int, roads: List[Tuple[int, int]]) -> int**: 
  - This function takes the number of cities (N), the number of roads (M), and a list of roads as input, and returns the number of distinct shortest paths from City 1 to City N.

## Installation

To run the Path Counting Application, you need to have Python installed on your machine. Follow the steps below to set up the environment:

1. **Install Python**: Make sure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: Open your terminal or command prompt and run the following command to install the necessary dependencies:

   ```bash
   pip install tkinter
   ```

## How to Use the Application

### Running the Application

1. **Clone the Repository**: If you haven't already, clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file to start the GUI.

   ```bash
   python main.py
   ```

### Using the GUI

1. **Input Number of Cities (N)**: Enter the total number of cities in the first input field.

2. **Input Number of Roads (M)**: Enter the total number of roads in the second input field.

3. **Input Roads**: In the third input field, enter the roads in the format `u v; u v; ...`, where `u` and `v` are city numbers connected by a road. For example, if there are roads between city 1 and city 2, and city 2 and city 3, you would enter `1 2; 2 3`.

4. **Count Paths**: Click the "Count Paths" button to calculate the number of distinct shortest paths from City 1 to City N.

5. **View Results**: The result will be displayed in a pop-up message box showing the number of distinct shortest paths.

### Edge Cases

- If there are no roads (M = 0), the application will return 0 paths.
- If the input values for cities or roads are invalid, appropriate error messages will be displayed.

## Testing the Function

To ensure the correctness and performance of the function, you can test it with various inputs directly in the GUI or by modifying the `main.py` file to include specific test cases.

## Documentation

For further details on the implementation and usage of the application, refer to the code comments in `main.py`, `graph.py`, and `gui.py`.

For any issues or feature requests, please reach out through the support channels provided in the repository.

Happy path counting!
```