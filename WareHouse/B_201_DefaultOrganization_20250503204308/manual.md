Here's the `manual.md` file for the Mountain application, detailing its main functions, installation instructions, and usage guidelines.

```markdown
# Mountain Application

A simple command-line application to determine the second highest mountain from a list of mountains based on user input.

## Main Functions

The Mountain application allows users to:

- Input the number of mountains.
- Enter the name and height of each mountain.
- Automatically determine and display the name of the second highest mountain.

### Key Components

1. **Input Validation**: Ensures that the number of mountains is at least two and that mountain names and heights are valid.
2. **Sorting Logic**: Sorts mountains based on height to identify the second highest.
3. **Error Handling**: Provides user-friendly error messages for invalid inputs.

## Quick Install

To run the Mountain application, you need to have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Install Dependencies

The Mountain application does not require any external libraries, but ensure you have Python 3.x installed. You can check your Python version by running:

```bash
python --version
```

## How to Use the Mountain Application

1. **Clone the Repository**: If you haven't already, clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file.

   ```bash
   python main.py
   ```

3. **Follow the Prompts**: 
   - Enter the number of mountains when prompted (must be at least 2).
   - For each mountain, enter the name and height when prompted.
   - The application will display the name of the second highest mountain.

### Example Usage

```plaintext
Enter the number of mountains: 3
Enter the name of mountain 1: Everest
Enter the height of mountain 1: 8848
Enter the name of mountain 2: K2
Enter the height of mountain 2: 8611
Enter the name of mountain 3: Kangchenjunga
Enter the height of mountain 3: 8586
The second highest mountain is: K2
```

## Error Handling

- If you enter a number less than 2 for the mountains, you will receive an error message prompting you to enter a valid number.
- If you enter an empty name for a mountain or a negative height, the application will notify you of the invalid input and prompt you to try again.

## Conclusion

The Mountain application is a straightforward tool for determining the second highest mountain based on user input. It emphasizes input validation and user-friendly error handling to ensure a smooth experience.

For any issues or feature requests, please reach out to the development team.
```

This manual provides a comprehensive overview of the Mountain application, ensuring users can easily understand how to install and use it effectively.