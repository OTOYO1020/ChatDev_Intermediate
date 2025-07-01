Here's a detailed user manual for the toy train car management software, formatted in Markdown:

```markdown
# Toy Train Car Management Software

Manage your toy train cars with ease! This software allows you to connect, disconnect, and print connected components of toy train cars using a simple command-line interface.

## Main Functions

The software provides the following main functionalities:

1. **Connect Cars**: Connect the front of one car to the rear of another.
   - Command: `1 x y`
   - Example: `1 2 3` connects Car 3 to the rear of Car 2.

2. **Disconnect Cars**: Disconnect the front of one car from the rear of another.
   - Command: `2 x y`
   - Example: `2 2 3` disconnects Car 3 from the rear of Car 2.

3. **Print Connected Component**: Print all car numbers in the connected component containing a specified car from front to back.
   - Command: `3 x`
   - Example: `3 2` prints the connected component containing Car 2.

## Installation

To run the software, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. **Run the Program**:
   You can run the program by executing the following command in your terminal:
   ```bash
   python main.py
   ```

2. **Input Format**:
   - The first line of input should contain two integers, `N` (number of toy train cars) and `Q` (number of queries).
   - The following `Q` lines should contain the queries in the specified format.

   Example Input:
   ```
   5 3
   1 1 2
   1 2 3
   3 1
   ```

3. **Output**:
   - The output for the `3 x` queries will be printed directly to the console, showing the car numbers in the connected component.

## Example Usage

Here’s a quick example to illustrate how to use the software:

1. Start the program:
   ```bash
   python main.py
   ```

2. Input the following:
   ```
   5 5
   1 1 2
   1 2 3
   3 1
   2 1 2
   3 1
   ```

3. Expected Output:
   ```
   1 2 3
   ```
   This output shows the connected component containing Car 1 before it was disconnected from Car 2.

## Notes

- Ensure that the car numbers used in the commands are within the range of `1` to `N`.
- The software efficiently handles up to 100,000 queries and prints at most 1,000,000 car numbers in total for connected component queries.

## Support

For any issues or questions, please reach out to our support team via the contact information provided in the repository.

Happy train managing!
```

This manual provides a comprehensive overview of the software, including its main functions, installation steps, usage instructions, and example scenarios to help users get started quickly.