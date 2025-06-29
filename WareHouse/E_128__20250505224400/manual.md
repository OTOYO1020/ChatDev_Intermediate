Here is the `manual.md` file for the Roadwork Distance Calculator software:

```markdown
# Roadwork Distance Calculator

A simple application to calculate the maximum distance a person can walk before reaching a blocked point due to roadworks.

## Quick Install

To run the Roadwork Distance Calculator, ensure you have Python installed on your system. You can install the necessary dependencies using pip:

```bash
pip install -r requirements.txt
```

Make sure to create a `requirements.txt` file with the necessary dependencies if you have any additional libraries.

## 🤔 What is this?

The Roadwork Distance Calculator is designed to help users determine how far they can walk before encountering roadworks that block their path. The application takes into account the coordinates and timings of various roadworks and the starting times of individuals.

### Main Functions

- **Input Roadworks**: Users can input multiple roadworks, each defined by a coordinate (X_i), a start time (S_i), and an end time (T_i).
- **Input People**: Users can input multiple starting times (D_i) for individuals.
- **Calculate Distances**: The application calculates the maximum distance each person can walk before being blocked by roadworks.

## 📖 How to Use

1. **Run the Application**: Execute the main application file `main.py` in your terminal.

   ```bash
   python main.py
   ```

2. **Input Data**:
   - When prompted, enter the number of roadworks (N) and the number of people (Q) separated by a space.
   - For each roadwork, input the coordinate (X_i), start time (S_i), and end time (T_i) separated by spaces.
   - For each person, input their starting time (D_i).

   Example Input:
   ```
   Enter the number of roadworks (N) and number of people (Q): 3 2
   Enter X_i (coordinate), S_i (start time), T_i (end time): 5 2 6
   Enter X_i (coordinate), S_i (start time), T_i (end time): 10 1 4
   Enter X_i (coordinate), S_i (start time), T_i (end time): 15 5 10
   Enter D_i (starting time): 3
   Enter D_i (starting time): 7
   ```

3. **View Results**: After entering the data, the application will calculate and display the maximum distances each person can walk before reaching a blocked point.

   Example Output:
   ```
   Distances: 5, 10
   ```

## 📄 Additional Information

- Ensure that the input values are integers. The application will terminate if invalid input is detected.
- The distances are calculated based on the sorted order of roadworks to optimize the search process.

For any issues or feature requests, please contact our support team.
```

This manual provides a comprehensive overview of the Roadwork Distance Calculator, including installation instructions, usage guidelines, and a brief description of its functionality.