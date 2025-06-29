Here's a detailed user manual for the meeting participant calculator software, formatted in Markdown as requested:

```markdown
# Meeting Participant Calculator

A software tool designed to calculate the maximum number of employees that can participate in a meeting across multiple bases, taking into account their local times and working hours.

## Main Functions

The Meeting Participant Calculator performs the following key functions:

1. **Input Gathering**: Reads the number of bases, the number of employees at each base, and their respective local times.
2. **UTC Conversion**: Converts local times to UTC to standardize the meeting time across different bases.
3. **Time Slot Calculation**: Determines valid meeting time slots based on the working hours of 9 AM to 6 PM in UTC.
4. **Maximum Participants Calculation**: Iterates through all possible meeting start times to find the maximum number of employees that can participate in a meeting.

## Installation

To run the Meeting Participant Calculator, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

No additional dependencies are required beyond Python itself. Ensure you have Python 3.x installed.

## How to Use

1. **Run the Application**: Open your terminal or command prompt and navigate to the directory where `main.py` is located. Run the application using the following command:

   ```bash
   python main.py
   ```

2. **Input Data**: The program will prompt you to enter the number of bases. Enter an integer value (N) representing the number of bases.

   ```
   Enter number of bases: 
   ```

3. **Enter Employee and Time Data**: For each base, you will be prompted to enter the number of employees and the local time (in hours, from 0 to 23) in a space-separated format. For example:

   ```
   Enter number of employees and local time for base 1 (space-separated): 10 14
   ```

   Repeat this step for all bases.

4. **View Results**: After entering the data, the program will calculate and display the maximum number of employees that can participate in a meeting based on the provided inputs.

   ```
   Maximum number of participants: X
   ```

## Example Usage

Here’s an example of how to use the Meeting Participant Calculator:

1. Start the program:

   ```bash
   python main.py
   ```

2. Input the number of bases:

   ```
   Enter number of bases: 2
   ```

3. Input the employee and local time data for each base:

   ```
   Enter number of employees and local time for base 1 (space-separated): 10 14
   Enter number of employees and local time for base 2 (space-separated): 5 10
   ```

4. The output will show the maximum number of participants:

   ```
   Maximum number of participants: 10
   ```

## Conclusion

The Meeting Participant Calculator is a straightforward tool that helps organizations optimize meeting participation across different time zones. By following the steps outlined in this manual, users can easily set up and utilize the software to enhance their meeting planning processes.
```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, usage guidelines, and an example to help users understand how to operate the application effectively.