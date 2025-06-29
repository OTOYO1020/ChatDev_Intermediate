```markdown
# Pigeon Management System

A simple command-line application for managing pigeons and nests, allowing users to move pigeons between nests and count nests with multiple pigeons.

## Main Functions

1. **Move Pigeon**: Move a specified pigeon to a designated nest.
   - Input format: `1 P H` where `P` is the pigeon ID and `H` is the nest ID.
   
2. **Count Nests with Multiple Pigeons**: Count and return the number of nests that contain more than one pigeon.
   - Input format: `2`

## Installation

To run the Pigeon Management System, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd pigeon-management-system
   ```

2. **Install Dependencies**:
   You may need to install any required dependencies. For this application, there are no external dependencies, but ensure you have Python 3.x installed.

## How to Use

1. **Run the Application**:
   Open your terminal and navigate to the directory where the application files are located. Then run the following command:
   ```bash
   python main.py
   ```

2. **Input Format**:
   - First, input the number of pigeons and nests, followed by the number of queries:
     ```
     N Q
     ```
     Where `N` is the number of pigeons (and nests) and `Q` is the number of queries.

   - Next, input the queries:
     - To move a pigeon:
       ```
       1 P H
       ```
       Replace `P` with the pigeon ID and `H` with the nest ID.
     - To count nests with multiple pigeons:
       ```
       2
       ```

3. **Example Input**:
   ```
   3 5
   1 1 2
   1 2 3
   2
   1 3 1
   2
   ```

4. **Output**:
   The application will print the results of all count queries sequentially.

## Example Usage

Here’s how the application works in practice:

1. Start the application.
2. Input the number of pigeons and nests, e.g., `3 5`.
3. Enter the queries as needed.
4. The application will process the queries and output the results for count queries.

## Conclusion

The Pigeon Management System is a straightforward tool for managing pigeon movements between nests. It is designed to be efficient and easy to use through standard input and output, making it suitable for command-line environments.

For any issues or feature requests, please reach out to the development team.
```