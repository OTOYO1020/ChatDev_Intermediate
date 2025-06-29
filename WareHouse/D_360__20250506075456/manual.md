Here's a detailed user manual for the Ant Simulation software, formatted in Markdown:

```markdown
# Ant Simulation

Simulate the movement of ants based on their initial positions and directions over a specified time.

## Main Functions

The Ant Simulation software consists of two main functions:

1. **calculate_final_positions(N, T, S, X)**:
   - Calculates the final positions of the ants based on their initial positions and directions.
   - Parameters:
     - `N` (int): The number of ants.
     - `T` (float): The time duration.
     - `S` (str): The binary string representing the direction of each ant ('0' for left, '1' for right).
     - `X` (list): The list of initial coordinates for each ant.
   - Returns:
     - A sorted list of final positions of the ants.

2. **count_passes(final_positions)**:
   - Counts the number of pairs of ants that pass each other based on their final positions.
   - Parameters:
     - `final_positions` (list): A sorted list of final positions of the ants.
   - Returns:
     - An integer representing the count of pairs of ants that pass each other.

## Installation

To run the Ant Simulation software, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

The software does not require any external libraries beyond the standard Python library. Ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**:
   If you haven't already, clone the repository containing the Ant Simulation code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**:
   Execute the main application file `main.py` using Python.
   ```bash
   python main.py
   ```

3. **Input Requirements**:
   - The program will prompt you to enter the following:
     - The number of ants (N).
     - The time duration (T).
     - A binary string (S) of length N, where each character is either '0' or '1'.
     - A list of initial coordinates (X) of length N, separated by spaces.

4. **Example Input**:
   ```
   Enter the number of ants (N):
   5
   Enter the time (T):
   2.0
   Enter the binary string S (length N, indexed from 0):
   10101
   Enter 5 space-separated coordinates for X (indexed from 0):
   0 1 2 3 4
   ```

5. **Output**:
   - The program will calculate the final positions of the ants and display the number of pairs of ants that pass each other.
   ```
   The number of passes is: 4
   ```

## Conclusion

The Ant Simulation software provides a simple yet effective way to simulate and analyze the movement of ants based on their initial positions and directions. By following the steps outlined in this manual, users can easily set up and run the simulation to explore various scenarios.

For any issues or further assistance, please refer to the code comments or reach out for support.
```

This manual provides a comprehensive overview of the Ant Simulation software, including its main functions, installation instructions, and usage guidelines.