Here's a detailed user manual for the Hat Color application in Markdown format:

```markdown
# Hat Color Application

A simple application to determine if the desired hat colors for Takahashis can be achieved through exchanges.

## Overview

The Hat Color application allows users to input the current and desired hat colors of three Takahashis, represented by the characters 'R', 'G', and 'B'. The application checks if the desired configuration can be achieved through any number of exchanges, concluding that it is always possible if the input conditions are met.

## Main Functions

- **Input Handling**: The application reads two input strings representing the current and desired hat colors.
- **Validation**: It verifies that both input strings are permutations of the characters 'R', 'G', and 'B'.
- **Hat Color Checking**: It determines if the desired configuration can be achieved from the current configuration.
- **Output**: The application returns "YES" if the desired configuration can be achieved, otherwise "NO".

## Installation

To run the Hat Color application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not require any external dependencies beyond Python itself. Ensure you have Python 3.x installed.

## How to Use the Application

1. **Run the Application**: Navigate to the directory containing the `main.py` file and run the application using the following command:

   ```bash
   python main.py
   ```

2. **Input Current Hat Colors**: When prompted, enter the current hat colors for Takahashis 1, 2, and 3. The input should be a string of exactly 3 characters consisting of 'R', 'G', and 'B'. For example:

   ```
   RGB
   ```

3. **Input Desired Hat Colors**: Next, enter the desired hat colors for Takahashis 1, 2, and 3 in the same format. For example:

   ```
   RBG
   ```

4. **View the Result**: The application will output "YES" if the desired configuration can be achieved or "NO" otherwise.

## Example Usage

```plaintext
Enter current hat colors (RGB): RGB
Enter desired hat colors (RGB): RBG
YES
```

## Conclusion

The Hat Color application is a straightforward tool for checking hat color configurations among Takahashis. With its simple input and validation process, it ensures that users can easily determine the possibility of achieving their desired configurations.

For any issues or further inquiries, please contact support.
```

This manual provides a comprehensive guide for users to understand the application, its installation process, and how to effectively use it.