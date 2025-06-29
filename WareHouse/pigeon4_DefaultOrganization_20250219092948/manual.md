```markdown
# Pigeon Management System

The Pigeon Management System is a command-line application designed to manage the movement of pigeons between nests and track the number of nests containing multiple pigeons. This software is efficient and straightforward, allowing users to perform operations through simple text-based commands.

## Main Functions

1. **Move Pigeon**: Move a specified pigeon to a designated nest.
   - Command format: `1 P H`
   - Where `P` is the pigeon ID and `H` is the nest ID.

2. **Count Nests with Multiple Pigeons**: Retrieve the count of nests that contain more than one pigeon.
   - Command format: `2`

## Installation

To run the Pigeon Management System, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd pigeon-management-system
   ```

2. **Install Required Packages**: 
   The application does not have any external dependencies beyond Python's standard library. Ensure you have Python 3.x installed.

## How to Use

1. **Run the Application**:
   Open your terminal or command prompt, navigate to the directory where the application files are located, and run:
   ```bash
   python main.py
   ```

2. **Input Format**:
   - First, input two integers `N` and `Q`, where `N` is the number of pigeons (and nests) and `Q` is the number of queries.
   - Follow this with `Q` lines of queries, which can be either:
     - `1 P H` to move pigeon `P` to nest `H`.
     - `2` to count the nests with multiple pigeons.

### Example Usage

```plaintext
5 3
1 1 3
1 2 3
2
```

- In this example:
  - There are 5 pigeons and 3 queries.
  - The first query moves pigeon 1 to nest 3.
  - The second query moves pigeon 2 to nest 3.
  - The third query counts the nests with multiple pigeons, which would return `1` since nest 3 now contains both pigeon 1 and pigeon 2.

3. **Output**:
   - The results of all count queries (`2`) will be printed sequentially after processing all queries.

## Conclusion

The Pigeon Management System is a simple yet powerful tool for managing pigeon movements and nest occupancy. By following the installation and usage instructions, users can efficiently track and manage their pigeons through a command-line interface.
```