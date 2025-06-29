Here's a detailed user manual for the Dango Level Finder software, formatted in Markdown as requested:

```markdown
# Dango Level Finder

A Python module to find the greatest level of dango strings in a given input string.

## Overview

The Dango Level Finder is designed to identify and evaluate dango patterns within strings. A dango pattern is defined as a substring that starts and ends with a hyphen ('-') and contains only 'o' characters in between. The function returns the maximum level of dango string found, where the level corresponds to the count of 'o' characters between the hyphens.

## Main Functions

- **find_greatest_dango_level(S: str) -> int**: This function takes a string `S` as input and returns an integer representing the greatest level of dango string found. If no valid dango string exists, it returns `-1`.

## Installation

To use the Dango Level Finder, you need to have Python installed on your machine. You can install the required dependencies using pip. Follow these steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the unit tests** (optional but recommended):
   ```bash
   python -m unittest discover
   ```

## Usage

To use the Dango Level Finder, you can import the `DangoLevelFinder` class from the `dango_level_finder` module and call the `find_greatest_dango_level` method. Here’s an example:

```python
from dango_level_finder import DangoLevelFinder

# Create an instance of DangoLevelFinder
finder = DangoLevelFinder()

# Example input strings
input_string1 = "---o---"
input_string2 = "----o---o----"
input_string3 = "----"

# Finding the greatest dango level
level1 = finder.find_greatest_dango_level(input_string1)
level2 = finder.find_greatest_dango_level(input_string2)
level3 = finder.find_greatest_dango_level(input_string3)

print(f"Greatest dango level in '{input_string1}': {level1}")  # Output: 1
print(f"Greatest dango level in '{input_string2}': {level2}")  # Output: 2
print(f"Greatest dango level in '{input_string3}': {level3}")  # Output: -1
```

## Edge Cases

The function handles various edge cases, including:

- Strings that are too short (less than 3 characters).
- Strings that contain no valid dango strings.
- Strings that only contain hyphens or 'o' characters.

## Unit Tests

Unit tests are provided to ensure the correctness of the function. You can run the tests using the following command:

```bash
python -m unittest discover
```

The tests cover valid cases, cases with no dango strings, and edge cases.

## Documentation

For more information on the implementation and usage, please refer to the source code comments in the `dango_level_finder.py` and `main.py` files.

## Conclusion

The Dango Level Finder is a simple yet powerful tool for identifying dango patterns in strings. With its easy-to-use interface and comprehensive testing, it is ready for integration into larger applications or for standalone use.
```

This manual provides a comprehensive guide for users to understand the functionality, installation, and usage of the Dango Level Finder software.