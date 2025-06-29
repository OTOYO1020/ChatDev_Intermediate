```markdown
# Pigeon Management System

The Pigeon Management System is a command-line application designed to efficiently manage the movement of pigeons between nests and track the number of nests containing multiple pigeons. This software is particularly useful for scenarios where you need to manage a fixed number of pigeons and nests dynamically.

## Main Functions

1. **Move Pigeon**: Move a specified pigeon to a different nest.
   - Input format: `1 P H` where `P` is the pigeon number and `H` is the nest number.
   
2. **Count Nests with Multiple Pigeons**: Retrieve the count of nests that contain more than one pigeon.
   - Input format: `2`

## Installation

To run the Pigeon Management System, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application files.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: If there are any additional dependencies, install them using pip. For this application, no external libraries are required beyond Python's standard library.

## How to Use the Application

1. **Run the Application**: Open your terminal and navigate to the directory containing the `main.py` file. Run the application using the following command:
   ```bash
   python main.py
   ```

2. **Input Format**: After running the application, you will be prompted to enter the number of pigeons (`N`) and the number of queries (`Q`). For example:
   ```
   5 3
   ```

3. **Executing Queries**:
   - To move a pigeon, enter a command in the format `1 P H`. For example, to move pigeon 1 to nest 3:
     ```
     1 1 3
     ```
   - To count the nests with multiple pigeons, simply enter:
     ```
     2
     ```

4. **Output**: The application will output the results of the count queries sequentially after processing all queries.

## Example Usage

Here’s an example of how to use the application:

```
Input:
5 5
1 1 3
1 2 3
2
1 3 4
2

Output:
1
1
```

In this example:
- Pigeon 1 is moved to nest 3.
- Pigeon 2 is also moved to nest 3, resulting in nest 3 having multiple pigeons.
- The first count query returns `1` (one nest with multiple pigeons).
- Pigeon 3 is then moved to nest 4, and the second count query again returns `1`.

## Conclusion

The Pigeon Management System provides a straightforward way to manage pigeon movements and track nests efficiently. For any issues or further assistance, please refer to the documentation or contact support.
```