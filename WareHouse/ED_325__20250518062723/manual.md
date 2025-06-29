Here is the `manual.md` file that provides a detailed user manual for the software developed to calculate the minimum travel time between cities using Dijkstra's algorithm.

```markdown
# Minimum Travel Time Calculator

A Python application for calculating the minimum travel time between cities using Dijkstra's algorithm. This tool allows users to input the number of cities, speed factors for transportation, and a distance matrix to determine the optimal travel time from city 1 to city N.

## Main Functions

- **Input Parameters**:
  - `N`: Number of cities.
  - `A`: Speed factor for the company car.
  - `B`: Speed factor for the train.
  - `C`: A constant that is not used in the current logic.
  - `D`: A distance matrix representing the distances between cities.

- **Output**:
  - Returns the minimum travel time from city 1 to city N as an integer.

## Quick Install

To run this application, you need to have Python installed on your machine. You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## How to Use

1. **Run the Application**:
   Execute the main application file `main.py` in your terminal or command prompt:

   ```bash
   python main.py
   ```

2. **Input the Parameters**:
   - When prompted, enter the number of cities (N).
   - Enter the speed factor for the company car (A).
   - Enter the speed factor for the train (B).
   - Enter a constant (C) that is not currently used in the logic.
   - Input the distance matrix row by row. Each row should be comma-separated, and you can end the input by pressing Enter on an empty line.

   Example input for a distance matrix with 3 cities:
   ```
   0,10,15
   10,0,20
   15,20,0
   ```

3. **View the Result**:
   After entering all the required data, the application will calculate and display the minimum travel time from city 1 to city N.

## Example Usage

```plaintext
Enter number of cities (N): 3
Enter A (car speed factor): 1
Enter B (train speed factor): 2
Enter C (not used in current logic): 0
Enter distance matrix (comma-separated rows, end with an empty line):
0,10,15
10,0,20
15,20,0

Minimum Travel Time: 15
```

## Error Handling

The application includes basic error handling for input validation. If the input is incorrect (e.g., non-numeric values, invalid matrix dimensions), an error message will be displayed.

## Future Extensions

This application can be extended to include additional features such as:
- Support for more transportation options.
- Enhanced user interface for easier input.
- Visualization of the travel routes.

For any questions or support, please contact our development team.

```

This manual provides a comprehensive guide for users to understand the application's functionality, installation process, and usage instructions.