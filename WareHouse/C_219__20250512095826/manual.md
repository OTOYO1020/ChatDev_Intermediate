Here’s a detailed user manual for the Name Sorter application, formatted in Markdown as requested:

```markdown
# Name Sorter

A simple application to sort names based on a custom alphabetical order.

## Overview

The Name Sorter application allows users to sort a list of names according to a specified alphabetical order. This is particularly useful when the default alphabetical order (A-Z) is not suitable for specific use cases. The application validates the custom order and ensures that all names consist of valid characters.

## Main Functions

- **sort_names(new_order: str, names: List[str]) -> List[str]**: This function sorts the provided list of names based on the custom alphabetical order defined by `new_order`. It validates the order and the names before performing the sort.

## Installation

To run the Name Sorter application, you need to have Python installed on your system. You can install the required dependencies using `pip`. 

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   # No external dependencies are required for this application
   ```

   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Name Sorter application, follow these steps:

1. **Open your terminal or command prompt**.

2. **Run the application** with the following command format:
   ```bash
   python main.py <new_order> <name1,name2,...>
   ```

   - `<new_order>`: A string representing the new alphabetical order (must be a permutation of the lowercase English letters 'a' to 'z').
   - `<name1,name2,...>`: A comma-separated list of names you want to sort.

   **Example**:
   ```bash
   python main.py "zyxwvutsrqponmlkjihgfedcba" "alice,bob,charlie"
   ```

3. **View the output**: The sorted names will be printed in the terminal.

## Error Handling

The application includes basic error handling:
- If the `new_order` is not a valid permutation of the lowercase English letters, an error message will be displayed.
- If any name contains invalid characters (i.e., characters not present in the `new_order`), an error message will be displayed.

## Conclusion

The Name Sorter application is a straightforward tool for sorting names based on custom alphabetical orders. It is designed to be efficient and user-friendly, making it easy to integrate into larger systems or use as a standalone tool.

For any further questions or support, please reach out to the development team.
```

This manual provides a comprehensive overview of the Name Sorter application, including installation instructions, usage examples, and error handling information, ensuring that users can effectively utilize the software.