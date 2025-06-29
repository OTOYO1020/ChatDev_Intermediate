Here's a detailed user manual for the subordinate counting application, formatted in Markdown:

```markdown
# Subordinate Counting Application

This application is designed to efficiently count the immediate subordinates for each member of a company based on their boss relationships. It allows users to input the number of members and their respective bosses, and outputs the count of immediate subordinates for each member.

## Main Functions

- **Input Handling**: The application prompts the user to enter the number of members and their bosses, ensuring that the input is valid.
- **Subordinate Counting**: It calculates the number of immediate subordinates for each member based on the provided boss relationships.
- **Output**: The application prints the subordinate counts for each member from 1 to N.

## Installation

To run the subordinate counting application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application code to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: This application does not require any external libraries, but ensure you have the standard Python environment set up.

## How to Use

1. **Run the Application**: Navigate to the directory where the `main.py` file is located and run the following command:
   ```bash
   python main.py
   ```

2. **Input the Number of Members**: When prompted, enter the total number of members in the company (N). Note that N must be at least 2.

3. **Input Bosses**: Enter the bosses for members 2 to N as a space-separated list. Each boss must be a unique integer between 1 and N.

4. **View Results**: After entering the data, the application will output the count of immediate subordinates for each member from 1 to N, each on a new line.

## Example Usage

```
Enter number of members (N): 5
Enter 4 unique bosses (space-separated, each between 1 and 5): 1 1 2 2
1
2
0
0
```

In this example:
- Member 1 has 2 immediate subordinates (members 2 and 3).
- Member 2 has 2 immediate subordinates (members 4 and 5).
- Members 3, 4, and 5 have no subordinates.

## Error Handling

The application includes error handling for the following scenarios:
- If the number of members (N) is less than 2, an error message will be displayed.
- If the number of bosses entered does not match N-1, an error message will be displayed.
- If any boss is not within the valid range (1 to N), an error message will be displayed.
- If the bosses are not unique, an error message will be displayed.

## Conclusion

This subordinate counting application is a straightforward tool for managing and analyzing hierarchical relationships within a company. By following the instructions above, users can easily install and utilize the software to gain insights into their organizational structure.
```

This manual provides a comprehensive overview of the application, including its functionality, installation instructions, and usage guidelines, ensuring that users can effectively utilize the software.