Here's a detailed user manual for the Garbage Collection application, formatted in Markdown as requested:

```markdown
# Garbage Collection Application

Efficiently manage garbage collection schedules based on various types of garbage and their collection periods.

## Overview

The Garbage Collection Application allows users to input different types of garbage, their collection periods, and remainders. Users can then query the next collection day based on the type of garbage and the day it is put out. This application is designed to streamline the scheduling of garbage collection, ensuring that users are informed of the next collection dates.

## Main Functions

1. **Input Garbage Types**: Users can enter the number of garbage types and their respective collection periods and remainders.
2. **Query Next Collection Day**: Users can input queries to find out the next collection day for a specific type of garbage based on the day it is put out.
3. **Error Handling**: The application includes robust error handling to ensure valid inputs and guide users through the process.

## Installation

To run the Garbage Collection Application, you need to have Python installed on your system. Follow these steps to set up your environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **Clone the Repository**: Clone the repository containing the application code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
3. **Install Dependencies**: If there are any additional dependencies required, install them using pip. For this application, no external libraries are required beyond Python's standard library.

## How to Use the Application

1. **Run the Application**: Execute the main script to start the application.
   ```bash
   python main.py
   ```

2. **Input the Number of Garbage Types (N)**: 
   - The application will prompt you to enter the number of garbage types. Enter a positive integer or type 'exit' to quit.

3. **Input Collection Periods and Remainders**:
   - For each garbage type, you will be prompted to enter the collection period and remainder in the format: `period remainder`.
   - Ensure that the collection period is a positive integer and the remainder is non-negative and less than the collection period.

4. **Input the Number of Queries (Q)**:
   - After entering the garbage types, you will be prompted to enter the number of queries. Again, enter a positive integer or type 'exit' to quit.

5. **Input Queries**:
   - For each query, input the garbage type and the day it is put out in the format: `type day`.
   - Ensure that the type is between 1 and N, and the day is a positive integer.

6. **View Results**:
   - The application will display the next collection day for each query based on the input provided.

## Example Usage

```
Enter the number of garbage types (N) or type 'exit' to quit: 3
Enter collection period and remainder for garbage type 1 (format: period remainder) or type 'exit' to quit: 7 3
Enter collection period and remainder for garbage type 2 (format: period remainder) or type 'exit' to quit: 5 1
Enter collection period and remainder for garbage type 3 (format: period remainder) or type 'exit' to quit: 10 0
Enter the number of queries (Q) or type 'exit' to quit: 2
Enter query 1 (type day) or type 'exit' to quit: 1 10
Next collection for type 1 on day 10.
Enter query 2 (type day) or type 'exit' to quit: 2 3
Next collection for type 2 on day 6.
```

## Error Handling

The application includes error messages for invalid inputs, guiding users to provide correct data. Common errors include:
- Entering non-integer values.
- Providing negative or zero values for garbage types or days.
- Inputting remainders that do not meet the specified conditions.

## Conclusion

The Garbage Collection Application is a user-friendly tool designed to help manage garbage collection schedules effectively. By following the instructions in this manual, users can easily navigate the application and ensure timely garbage collection.
```

This manual provides a comprehensive guide for users to understand the application's functionality, installation steps, and usage instructions.