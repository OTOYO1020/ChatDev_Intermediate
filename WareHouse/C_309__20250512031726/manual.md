Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Pills Tracker

A software application designed to help users track their daily pill intake based on various medicine types and their prescribed dosages.

## Main Functions

The Pills Tracker application includes the following key functionalities:

1. **Input Handling**: Users can input the number of medicine types, a threshold for the maximum number of pills they want to take, and a list of medicine dosages for specific days.

2. **Pill Calculation**: The application calculates the first day where the total number of pills taken is less than or equal to the specified threshold.

3. **Input Validation**: The application ensures that all inputs are valid and within specified constraints, providing error messages for invalid entries.

4. **Graphical User Interface (GUI)**: Users can interact with the application through a simple GUI, making it user-friendly and accessible.

## Installation

To run the Pills Tracker application, you need to have Python installed on your machine. Follow the steps below to set up the environment:

1. **Install Python**: Ensure that you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: Open your terminal or command prompt and run the following command to install the necessary libraries:

   ```bash
   pip install tkinter
   ```

   Note: `tkinter` is included with most Python installations, but if you encounter issues, please refer to the [tkinter documentation](https://docs.python.org/3/library/tkinter.html) for installation instructions.

## How to Use the Application

### Running the Application

1. **Main Entry Point**: To start the application, run the `main.py` file. You can do this by navigating to the directory containing the file in your terminal and executing:

   ```bash
   python main.py
   ```

2. **Input Values**: The application will prompt you to enter:
   - The number of medicine types (N).
   - The threshold for the maximum number of pills (K).
   - The days and corresponding dosages in the format `a_i b_i`, separated by commas.

   Example input:
   ```
   Enter the number of medicine types (N): 3
   Enter the threshold (K): 5
   Enter the days (a_i, b_i) - comma separated: 2 3, 3 2, 1 1
   ```

3. **View Results**: After entering the inputs, the application will calculate and display the first day where the total pills taken is less than or equal to K. If no such day exists, it will inform you accordingly.

### Using the GUI

1. **Run the GUI**: To use the graphical interface, run the `gui.py` file:

   ```bash
   python gui.py
   ```

2. **Fill in the Fields**: Enter the number of medicine types, the threshold, and the days with dosages in the provided fields.

3. **Calculate**: Click the "Calculate" button to see the result displayed below.

4. **Error Handling**: If there are any input errors, the application will show an error message to guide you in correcting the input.

## Conclusion

The Pills Tracker application is designed to simplify the process of tracking daily pill intake based on user-defined parameters. With its input validation and user-friendly interface, it aims to provide a seamless experience for users managing their medication schedules.

For any issues or further assistance, please refer to the documentation or contact support.
```

This manual provides a comprehensive overview of the Pills Tracker application, including its main functions, installation instructions, and usage guidelines.