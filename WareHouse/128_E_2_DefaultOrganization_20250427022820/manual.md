# Roadwork Distance Calculator

A user-friendly application designed to help users calculate the distance they can walk before encountering roadwork blockages based on input roadwork data and queries.

## Main Functions

- **Input Handling**: Read integers \( N \) (number of roadworks) and \( Q \) (number of queries) from user input, followed by \( N \) triplets \((X_i, S_i, T_i)\) representing roadworks and \( Q \) integers \( D_i \) representing start times.
  
- **Data Structure Initialization**: Initializes a dictionary `blocked_intervals` where each key is a coordinate \( X_i \) and the value is a list of tuples representing the blocked time intervals \((S_i, T_i)\).

- **Populate Blocked Intervals**: Iterates over the list of roadworks to populate the `blocked_intervals` dictionary with corresponding time intervals.

- **Sort and Merge Intervals**: Sorts the intervals by their start time \( S_i \) and merges overlapping or contiguous intervals.

- **Simulate Walking**: For each person starting at time \( D_i \), calculates the distance they can walk before encountering a blocked point.

- **Binary Search for Blocked Point**: Efficiently finds the first blocked point a person encounters after starting at time \( D_i \).

- **Output Results**: Displays the calculated distances for each query.

## Installation

To run the Roadwork Distance Calculator, ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

You will need the following Python packages:

- `tkinter`: For the graphical user interface (GUI).
- `bisect`: For efficient searching within sorted lists (included in the Python standard library).

You can install any additional dependencies using pip:

```bash
pip install tkinter
```

## How to Use the Application

1. **Run the Application**: Execute the `main.py` file to launch the Roadwork Distance Calculator GUI.

   ```bash
   python main.py
   ```

2. **Input Data**: In the text area provided, enter the number of roadworks \( N \) and the number of queries \( Q \) on the first line, followed by \( N \) lines of roadwork data in the format `(X_i, S_i, T_i)` and \( Q \) lines of query data \( D_i \). For example:

   ```
   3 2
   1 2 5
   2 3 6
   3 1 4
   2
   5
   ```

3. **Submit Data**: Click the "Submit" button to process the input data. The application will calculate the distances based on the provided roadwork and query data.

4. **View Results**: The results will be displayed in the results area below the input section. Each distance will be printed on a new line.

5. **Reset Data**: If you wish to clear the input and output areas, click the "Reset" button.

## Example Input and Output

### Input
```
3 2
1 2 5
2 3 6
3 1 4
2
5
```

### Output
```
1
3
```

This indicates that for the first query starting at time 2, the user can walk 1 unit before encountering a blockage, and for the second query starting at time 5, the user can walk 3 units.

## Conclusion

The Roadwork Distance Calculator is a powerful tool for simulating walking distances in the presence of roadwork blockages. By following the instructions above, users can easily input their data and receive accurate distance calculations. For any issues or feedback, please reach out to our support team.