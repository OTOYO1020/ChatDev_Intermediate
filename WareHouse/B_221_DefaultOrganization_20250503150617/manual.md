# String Swap Application User Manual

## Overview

The String Swap Application is designed to determine if one string can be transformed into another by swapping adjacent characters. This application is useful for various string manipulation tasks and can be easily integrated into other projects.

## Main Functions

- **Input Handling**: Reads two strings, `S` and `T`, from standard input.
- **Equality Check**: Checks if the two strings are already equal.
- **Swap Logic**: Determines if a single adjacent swap can make the strings equal.
- **Validation**: Ensures that the strings meet specified criteria (length and character set).

## Installation

To run the String Swap Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Open your terminal or command prompt and run the following command to install any required dependencies (if applicable). For this application, no external libraries are required, as it uses built-in Python functionalities.

   ```bash
   pip install --upgrade pip
   ```

3. **Clone the Repository**: If you have the source code in a repository, clone it using:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

4. **Run the Application**: You can run the application by executing the `main.py` file.

   ```bash
   python main.py
   ```

## Usage Instructions

1. **Input Strings**: When prompted, enter the first string `S` followed by the second string `T`. Ensure both strings consist only of lowercase English letters and are between 2 to 100 characters in length.

   Example:
   ```
   S: abcd
   T: acbd
   ```

2. **Output**: The application will output either `YES` or `NO` based on whether the string `S` can be made equal to string `T` through a single adjacent swap.

   - If the strings are equal, it will print:
     ```
     YES
     ```
   - If a valid swap is found that makes them equal, it will also print:
     ```
     YES
     ```
   - If no valid swap can make them equal, it will print:
     ```
     NO
     ```

## Example

### Input
```
abcd
acbd
```

### Output
```
YES
```

### Input
```
abc
def
```

### Output
```
NO
```

## Notes

- The application currently does not include a graphical user interface (GUI) and operates solely through standard input and output.
- Ensure that the input strings meet the specified criteria to avoid unexpected results.

## Support

For any issues or questions regarding the String Swap Application, please reach out to our support team at [support@chatdev.com](mailto:support@chatdev.com).

Thank you for using the String Swap Application! We hope it meets your needs for string manipulation tasks.