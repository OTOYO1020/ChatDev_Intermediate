Here's a detailed user manual for the Amoeba Generation Calculator software, formatted in Markdown as requested:

```markdown
# Amoeba Generation Calculator

A simple Python application to calculate the generation distances of amoebae based on their disappearance records.

## Main Functions

The Amoeba Generation Calculator provides the following main functionalities:

- **Calculate Generations**: Given a number of amoebae and their disappearance records, the application calculates the generation distance of each amoeba from the root amoeba (amoeba 1).
- **Input Validation**: Ensures that the records provided are valid and within the expected range.
- **Output Generation**: Returns a list of integers representing the generation distances for amoebae from 1 to `2N + 1`.

## Installation

To run the Amoeba Generation Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: Open your terminal or command prompt and run the following command to install any necessary dependencies:
   ```bash
   pip install typing
   ```

## How to Use

1. **Clone the Repository**: If you haven't already, clone the repository containing the Amoeba Generation Calculator code:
   ```bash
   git clone <repository-url>
   cd amoeba-generation-calculator
   ```

2. **Run the Application**: Execute the main application file to start the calculator:
   ```bash
   python main.py
   ```

3. **Input Data**: When prompted, enter the number of amoebae (N) and their disappearance records as a comma-separated list. For example:
   ```
   Enter number of amoebae: 3
   Enter amoebae records (comma-separated): 1, 1, 2
   ```

4. **View Results**: After entering the data, the application will process the records and display the generation distances:
   ```
   Generations: [0, 1, 1, 2, 2, -1]
   ```

## Example Usage

Here’s an example of how the application works:

- **Input**: 
  - Number of amoebae: `3`
  - Records: `1, 1, 2`
  
- **Output**: 
  - Generations: `[0, 1, 1, 2, 2, -1]`
  
This output indicates that:
- Amoeba 1 is the root (generation 0).
- Amoebae 2 and 3 are one generation away from amoeba 1.
- Amoebae 4 and 5 are two generations away from amoeba 2.

## Error Handling

The application includes basic error handling to manage invalid inputs. If the input does not match the expected format or contains out-of-bounds indices, an appropriate error message will be displayed.

## Conclusion

The Amoeba Generation Calculator is a straightforward tool for calculating the generation distances of amoebae based on their disappearance records. By following the installation and usage instructions, you can easily set up and run the application to analyze amoeba generations.

For further assistance or support, please contact the development team.
```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, usage guidelines, and error handling. Let me know if you need any further modifications or additional information!