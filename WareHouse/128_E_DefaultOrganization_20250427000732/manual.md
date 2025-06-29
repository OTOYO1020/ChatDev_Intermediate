```markdown
# Roadwork Simulator

The Roadwork Simulator is a Python application designed to simulate walking distances in the presence of roadworks. It allows users to input roadwork data and starting times, and calculates how far a person can walk before encountering a blocked point.

## Main Functions

1. **Input Handling**: Reads integers \( N \) (number of roadworks) and \( Q \) (number of queries) from standard input, followed by \( N \) triplets \((X_i, S_i, T_i)\) representing the coordinates and time intervals of roadworks, and \( Q \) integers \( D_i \) representing the starting times of individuals.

2. **Data Structure Initialization**: Initializes a dictionary `blocked_intervals` where each key is a coordinate \( X_i \) and the value is a list of tuples representing the blocked time intervals \((S_i, T_i)\).

3. **Populate Blocked Intervals**: Iterates over the list of roadworks to populate the `blocked_intervals` dictionary with the corresponding time intervals.

4. **Sort and Merge Intervals**: Sorts the blocked intervals by their start time and merges overlapping or contiguous intervals.

5. **Simulate Walking**: For each person starting at time \( D_i \), determines the distance they can walk before encountering a blocked point.

6. **Binary Search for Blocked Point**: Efficiently finds the first blocked point a person encounters after starting at time \( D_i \).

7. **Calculate Distance**: Calculates the distance walked as the difference between the starting point (0) and the coordinate of the first blocked point encountered.

8. **Output Results**: Prints the calculated distances for each person, representing how far they walked before stopping.

## Installation

To run the Roadwork Simulator, ensure you have Python installed on your machine. You can install the required dependencies using pip. Open your terminal and run:

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, you can create one with the necessary dependencies or install any additional libraries you may need manually.

## Usage

1. **Prepare Input**: Create an input file or prepare to provide input via standard input. The input format should be as follows:

   ```
   N Q
   X1 S1 T1
   X2 S2 T2
   ...
   XN SN TN
   D1
   D2
   ...
   DQ
   ```

   Where:
   - \( N \) is the number of roadworks.
   - \( Q \) is the number of queries.
   - Each triplet \( (X_i, S_i, T_i) \) represents a roadwork at coordinate \( X_i \) starting at time \( S_i \) and ending at time \( T_i \).
   - Each \( D_i \) is the starting time for each person.

2. **Run the Application**: Execute the main script to start the simulation. You can run the application from the terminal as follows:

   ```bash
   python main.py < input.txt
   ```

   Replace `input.txt` with the path to your input file or provide input directly in the terminal.

3. **View Results**: The application will output the distances each person walked before encountering a blocked point, each on a new line.

## Example

Given the following input:

```
3 2
1 2 5
2 3 6
3 1 4
2
5
```

The output will be:

```
1
3
```

This indicates that the first person starting at time 2 can walk 1 unit before hitting a roadwork, and the second person starting at time 5 can walk 3 units.

## Conclusion

The Roadwork Simulator is a powerful tool for simulating walking distances in the presence of roadworks. By following the installation and usage instructions, users can easily set up and run the application to analyze walking distances based on roadwork data.
```