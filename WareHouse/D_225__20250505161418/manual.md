Here's a detailed user manual for the toy train car application, formatted in Markdown as requested:

```markdown
# Toy Train Car Application

Manage and manipulate a series of toy train cars with ease. This application allows you to connect, disconnect, and print the connected components of toy train cars through a simple command-line interface.

## Main Functions

The application provides the following main functionalities:

1. **Connect Cars**: Connect the front of one car to the rear of another.
2. **Disconnect Cars**: Disconnect the front of one car from the rear of another.
3. **Print Connected Component**: Print all cars connected to a specified car in order from front to back.

## Installation

To run the Toy Train Car Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: If there are any additional dependencies, install them using pip. For this application, no external libraries are required beyond Python's standard library.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Toy Train Car Application, follow these steps:

1. **Run the Application**: Execute the main script to start the application.
   ```bash
   python main.py
   ```

2. **Input Format**: The application expects input in the following format:
   - First line: Two integers, N (number of toy train cars) and Q (number of queries).
   - Next Q lines: Each line represents a query in one of the following formats:
     - `1 x y`: Connect the front of Car y to the rear of Car x.
     - `2 x y`: Disconnect the front of Car y from the rear of Car x.
     - `3 x`: Print the connected component containing Car x.

3. **Example Input**:
   ```
   5 3
   1 1 2
   1 2 3
   3 1
   ```

4. **Output**: The output for the `3 x` query will be a space-separated list of car numbers in the connected component from front to back.

## Example Usage

Here’s an example of how to use the application:

1. Start the application:
   ```bash
   python main.py
   ```

2. Input the number of cars and queries:
   ```
   5 4
   ```

3. Execute commands:
   ```
   1 1 2
   1 2 3
   3 1
   2 1 2
   3 1
   ```

4. Expected Output:
   ```
   1 2 3
   1
   ```

## Notes

- Ensure that the input values for N and Q are valid (N, Q ≥ 1).
- The application can handle up to 100,000 queries and will print at most 1,000,000 car numbers in total for connected component queries.
- Invalid queries will prompt an error message indicating the issue.

## Conclusion

The Toy Train Car Application is a simple yet powerful tool for managing toy train cars. With its straightforward command-line interface, you can easily connect, disconnect, and visualize the connections between cars. Enjoy playing with your toy train cars!
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and examples to help users understand how to interact with the software effectively.