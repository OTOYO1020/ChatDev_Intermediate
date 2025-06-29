Here's a detailed user manual for the Pigeon Management application, formatted in Markdown:

```markdown
# Pigeon Management Application

The Pigeon Management application is designed to efficiently manage the movement of pigeons between nests and track the number of nests containing multiple pigeons. This application operates entirely through standard input and output, ensuring a streamlined experience without any graphical user interface (GUI).

## Main Functions

1. **Move Pigeon**: Move a specified pigeon to a designated nest.
   - Input format: `1 P H` where `P` is the pigeon number and `H` is the nest number.
   - Example: `1 2 3` moves pigeon 2 to nest 3.

2. **Count Nests with Multiple Pigeons**: Retrieve the count of nests that contain more than one pigeon.
   - Input format: `2`
   - Example: `2` returns the number of nests with multiple pigeons.

## Installation

To run the Pigeon Management application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   # Add any additional libraries here if needed
   ```

   Then, install the dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:
   To start the application, execute the `main.py` script. You can provide input directly through the terminal or redirect from a file.
   ```bash
   python main.py
   ```

2. **Input Format**:
   - First line: Two integers `N` and `Q`, where `N` is the number of pigeons (and nests) and `Q` is the number of queries.
   - Next `Q` lines: Each line contains either a move command (`1 P H`) or a count command (`2`).

   Example input:
   ```
   5 3
   1 1 3
   2
   1 2 4
   2
   ```

3. **Output**:
   The application will output the results of all count queries sequentially. For the above example, the output will show the number of nests containing multiple pigeons after each count query.

## Example

Here’s a complete example of how to use the application:

### Input
```
5 4
1 1 3
2
1 2 4
2
```

### Output
```
0
1
```

In this example:
- Initially, each pigeon is in its own nest.
- After moving pigeon 1 to nest 3, there are still no nests with multiple pigeons.
- After moving pigeon 2 to nest 4, there is still only one nest (nest 3) with multiple pigeons.

## Conclusion

The Pigeon Management application provides a simple yet effective way to manage pigeon movements and track nests. By following the installation and usage instructions, users can efficiently interact with the application through standard input and output.
```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, usage guidelines, and examples to help users understand how to operate the software effectively.