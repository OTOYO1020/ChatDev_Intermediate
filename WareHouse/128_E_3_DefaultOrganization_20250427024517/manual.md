```markdown
# Roadworks Simulation Software

This software simulates the impact of roadworks on pedestrian movement, allowing users to determine how far individuals can walk before encountering blocked points due to roadworks.

## Main Functions

1. **Input Handling**: The software reads integers \( N \) (number of roadworks) and \( Q \) (number of queries) from standard input, followed by \( N \) triplets \((X_i, S_i, T_i)\) representing the coordinates and time intervals of roadworks, and \( Q \) integers \( D_i \) representing the starting times for each query.

2. **Data Structure Initialization**: It initializes a dictionary `blocked_intervals` where each key is a coordinate \( X_i \) and the value is a list of tuples representing the blocked time intervals \((S_i, T_i)\).

3. **Populate Blocked Intervals**: The software populates the `blocked_intervals` dictionary with the corresponding time intervals for each coordinate \( X_i \).

4. **Sort and Merge Intervals**: It sorts the intervals by their start time \( S_i \) and merges overlapping or contiguous intervals to optimize the blocked intervals data.

5. **Simulate Walking**: For each person starting at time \( D_i \), the software determines the distance they can walk before encountering a blocked point.

6. **Binary Search for Blocked Point**: It uses binary search to efficiently find the first blocked point a person encounters after starting at time \( D_i \).

7. **Calculate Distance**: The software calculates the distance walked as the difference between the starting point (0) and the coordinate of the first blocked point encountered.

8. **Output Results**: Finally, it prints each calculated distance on a new line, representing how far each person walked before stopping.

## Installation

To run the software, ensure you have Python installed on your machine. You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, you can manually ensure that you have the following packages installed:

- Python 3.x
- Any additional libraries you may need (if specified in the requirements).

## How to Use

1. **Prepare Input Data**: Create a text file or prepare to input data directly in the console. The input format should be as follows:
   - The first line contains two integers \( N \) and \( Q \).
   - The next \( N \) lines each contain three integers \( X_i, S_i, T_i \).
   - The following \( Q \) lines each contain one integer \( D_i \).

   Example input:
   ```
   3 2
   1 2 5
   2 3 6
   3 1 4
   2
   5
   ```

2. **Run the Application**: Execute the main application file using Python. You can run it from the command line as follows:

   ```bash
   python main.py < input.txt
   ```

   Replace `input.txt` with the path to your input file. Alternatively, you can input data directly into the console.

3. **View Results**: After running the application, the output will display the distances each person can walk before encountering a blocked point, printed line by line.

## Example Output

For the example input provided above, the output might look like this:

```
1
3
```

This indicates that the first person starting at time 2 can walk 1 unit before encountering a block, and the second person starting at time 5 can walk 3 units.

## Conclusion

This software provides a robust simulation of pedestrian movement in the presence of roadworks, allowing for effective planning and analysis. For further assistance or inquiries, please contact our support team.
```