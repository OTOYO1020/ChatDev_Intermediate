Here's a detailed user manual for the Distance Calculator software, formatted in Markdown:

```markdown
# Distance Calculator

A Python application for calculating walking distances based on roadworks and people's starting times.

## Main Functions

The Distance Calculator provides the following main functionalities:

- **Input Handling**: Accepts the number of roadworks and people, along with their respective details.
- **Distance Calculation**: Computes the distance each person can walk before encountering a blocked point due to roadworks.
- **Binary Search Mechanism**: Efficiently finds the nearest blocked point for each person based on their starting time.
- **Output**: Returns a list of distances walked by each person, corresponding to their input order.

## Quick Install

To run the Distance Calculator, ensure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install typing
```

## How to Use

1. **Clone the Repository**: Download the Distance Calculator code from the repository.

2. **Navigate to the Directory**: Open your terminal and navigate to the directory where the `main.py` and `distance_calculator.py` files are located.

3. **Run the Application**: Execute the main application file using Python:

   ```bash
   python main.py
   ```

4. **Input Data**: Follow the prompts to enter the number of roadworks and people. For each roadwork, input the coordinates and time intervals, and for each person, input their starting time. The format for input is as follows:
   - For roadworks: `X S T` (where `X` is the coordinate, `S` is the start time, and `T` is the end time).
   - For people: `D` (where `D` is the starting time for the person).

5. **View Results**: After entering all the data, the application will calculate and display the distances each person can walk before encountering a blocked point.

## Example Usage

```plaintext
Enter number of roadworks and people (N Q): 3 2
Enter roadwork (X, S, T): 5 2 6
Enter roadwork (X, S, T): 10 3 8
Enter roadwork (X, S, T): 15 5 10
Enter starting time for person 1 (D): 1
Enter starting time for person 2 (D): 4
Distances: 1 4
```

In this example, the application calculates that the first person can walk 1 unit before encountering a blocked point, while the second person can walk 4 units.

## Additional Information

For more details on the implementation, refer to the source code in `distance_calculator.py`. The code is structured to facilitate easy modifications and enhancements.

If you encounter any issues or have questions, please reach out for support.
```

This manual provides a comprehensive overview of the Distance Calculator software, including its main functions, installation instructions, usage guidelines, and an example to help users understand how to interact with the application.