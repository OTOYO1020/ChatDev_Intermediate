Here's a detailed user manual for the card game application, formatted in Markdown as requested:

```markdown
# Card Game Application

Welcome to the Card Game Application! This software allows users to deduce the values of cards based on given constraints, simulating a fun and engaging card deduction game.

## Main Functions

- **Input Number of Cards and Constraints**: Users can specify how many cards (N) and constraints (M) they want to work with.
- **Define Constraints**: Users can input constraints in the format `X Y Z`, where `X` and `Y` are indices of the cards and `Z` is the parity condition.
- **Deduction Process**: The application will deduce the values of the cards based on the constraints until no further deductions can be made.
- **Cost Calculation**: The application calculates the total cost required to reveal all card values, simulating the revealing process.
- **Inconsistency Detection**: The application checks for inconsistencies in the constraints and notifies the user if any are found.

## Installation Instructions

To run the Card Game Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application files to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Required Dependencies**: The application does not have any external dependencies beyond Python itself. However, ensure you have the necessary permissions to run Python scripts.

## How to Use the Application

1. **Run the Application**: Navigate to the directory where the application files are located and run the main script.

   ```bash
   python main.py
   ```

2. **Input the Number of Cards**: When prompted, enter the number of cards (N) you want to use.

3. **Input the Number of Constraints**: Next, enter the number of constraints (M) that will be used to deduce the card values.

4. **Define Constraints**: For each constraint, input the values in the format `X Y Z`, where:
   - `X` is the index of the first card.
   - `Y` is the index of the second card.
   - `Z` is the parity condition (0 or 1).

   Repeat this step for all M constraints.

5. **View Results**: After entering all constraints, the application will deduce the values of the cards and display the total cost required to reveal all card values. If any inconsistencies are found during the deduction process, the application will notify you.

## Example Usage

```
Enter the number of Cards (N):
5
Enter the number of Constraints (M):
3
Enter constraints in the format 'X Y Z' for each constraint:
0 1 0
1 2 1
2 3 0
```

The application will process the input and provide the results based on the constraints defined.

## Conclusion

The Card Game Application is a powerful tool for deducing card values based on logical constraints. Enjoy playing and exploring the deductions!

For any issues or feedback, please reach out to our support team.
```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, and usage guidelines.