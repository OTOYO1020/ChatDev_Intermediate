Here is the `manual.md` file for the Name Sorter application, detailing its main functions, installation instructions, and usage guidelines:

```markdown
# Name Sorter

A simple application to sort names based on a custom alphabetical order defined by the user.

## Overview

The Name Sorter allows users to input a custom alphabetical order for lowercase English letters and a list of names. The application then sorts the names according to the specified order and outputs the sorted list. This is particularly useful for applications where traditional alphabetical sorting does not meet specific requirements.

## Main Functions

- **Custom Alphabetical Order**: Users can define a unique order for the lowercase English letters.
- **Input Validation**: The application ensures that the custom order contains 26 unique lowercase letters and that names consist only of lowercase letters.
- **Sorting Mechanism**: Names are sorted based on the custom order using a defined sorting function.
- **Output**: The sorted names are printed, each on a new line.

## Installation

To run the Name Sorter application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Create a virtual environment (optional but recommended) and install the required dependencies. You can use `pip` to install the necessary packages.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

   If you anticipate using libraries like `numpy` or `pandas` in future enhancements, you can specify them in the `requirements.txt` file.

## Usage

1. **Run the Application**:
   Execute the main application file to start the Name Sorter.

   ```bash
   python main.py
   ```

2. **Input the Custom Alphabetical Order**:
   When prompted, enter a permutation string of 26 unique lowercase letters (e.g., `zyxwvutsrqponmlkjihgfedcba`). Ensure there are no duplicates and all characters are lowercase.

3. **Input the Number of Citizens**:
   Enter a positive integer indicating the number of names you wish to input.

4. **Input Names**:
   For each citizen, input their name. The name must consist only of lowercase letters and cannot be empty. The application will prompt you to re-enter the name if it does not meet these criteria.

5. **View Sorted Names**:
   After all names have been entered, the application will output the sorted names according to the custom alphabetical order, with each name appearing on a new line.

## Example

```
Enter the custom alphabetical order (26 unique lowercase letters): zyxwvutsrqponmlkjihgfedcba
Enter the number of citizens (positive integer): 3
Enter the name of the citizen (must contain only lowercase letters and cannot be empty): alice
Enter the name of the citizen (must contain only lowercase letters and cannot be empty): bob
Enter the name of the citizen (must contain only lowercase letters and cannot be empty): charlie
```

Output:
```
charlie
bob
alice
```

## Support

For any issues or feature requests, please contact our support team or open an issue in the repository.

Happy sorting!
```

This manual provides a comprehensive guide for users to understand and effectively utilize the Name Sorter application.