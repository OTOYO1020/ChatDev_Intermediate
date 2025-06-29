Here's a detailed user manual for the insurance calculator software, formatted in Markdown as requested:

```markdown
# Insurance Calculator

A software tool for calculating the number of insured individuals based on family relationships and insurance purchases.

## Overview

The Insurance Calculator allows users to input family relationships and insurance purchases to determine how many unique individuals are covered by insurance. The software constructs a family tree from the provided parent-child relationships and efficiently counts the insured individuals across multiple generations.

## Main Functions

- **Input Handling**: Accepts the number of people, number of insurance purchases, a list of parents, and a list of insurance purchases.
- **Family Tree Construction**: Builds a tree structure representing family relationships based on the parents' list.
- **Insurance Coverage Calculation**: Traverses the family tree to count unique insured individuals based on the insurance purchases and the number of generations covered.

## Installation

To run the Insurance Calculator, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This software requires the following Python packages:

- `typing` (included in Python 3.5 and above)

You can install any additional dependencies using pip:

```bash
pip install -r requirements.txt
```

### Running the Application

1. Clone the repository or download the source code.
2. Navigate to the directory containing the `main.py` and `insurance_calculator.py` files.
3. Run the application using the following command:

```bash
python main.py
```

4. Follow the prompts to enter the required inputs:
   - **Number of People (N)**: Total number of individuals.
   - **Number of Insurances (M)**: Total number of insurance purchases.
   - **Parents List**: A comma-separated list of integers representing the parent of each person (use -1 for individuals without parents).
   - **Insurances**: A semicolon-separated list of tuples in the format `person, generations`, where `person` is the index of the individual who purchased the insurance and `generations` is the number of generations the insurance covers.

### Example Input

```
Enter number of people (N): 5
Enter number of insurances (M): 2
Enter parents list (comma-separated): -1,0,0,1,1
Enter insurances (format: person, generations; comma-separated): 0,1; 1,1
```

### Example Output

```
Total Insured: 4
```

## Error Handling

The application includes basic error handling for input validation. Common errors include:

- Invalid parent indices (must be -1 or between 0 and N-1).
- Invalid generations value (must be non-negative).
- Mismatched lengths of the parents list.

If an error occurs, the application will display an appropriate message.

## Conclusion

The Insurance Calculator is a powerful tool for analyzing insurance coverage based on family relationships. By following the installation and usage instructions, users can easily determine the total number of insured individuals in their dataset.

For further assistance, please refer to the code comments or reach out to the development team.
```

This user manual provides a comprehensive guide for users to understand the functionality, installation process, and usage of the Insurance Calculator software.