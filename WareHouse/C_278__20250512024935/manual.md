Here's a detailed user manual for the Twidai application, formatted in Markdown as requested:

```markdown
# Twidai

A simple user management application for managing follow/unfollow relationships between users.

## Overview

Twidai allows users to follow and unfollow each other, as well as check mutual following relationships. This application is designed to efficiently handle user operations and provide quick responses to queries about user relationships.

## Main Functions

The main function of the Twidai application is `process_twidai_operations(N: int, Q: int, operations: List[Tuple[int, int, int]]) -> List[str]`. This function processes a series of operations related to user relationships, including:

1. **Follow Operation (T_i = 1)**: Allows one user to follow another.
2. **Unfollow Operation (T_i = 2)**: Allows one user to unfollow another.
3. **Check Mutual Following (T_i = 3)**: Checks if two users are following each other and returns "Yes" or "No".

## Installation

To run the Twidai application, you need to have Python installed on your system. You can install the required dependencies using pip. Follow these steps:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the Twidai repository to your local machine.
   ```bash
   git clone <repository-url>
   cd twidai
   ```

3. **Install Dependencies**: Install the required dependencies using pip.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the Twidai application, you can run the `main.py` file, which serves as the entry point for the application. Here’s how to do it:

1. **Run the Application**: Execute the following command in your terminal:
   ```bash
   python main.py
   ```

2. **Input Parameters**: The application will process a predefined set of operations. You can modify the `operations` list in `main.py` to test different scenarios.

3. **Example Operations**:
   ```python
   operations = [
       (1, 1, 2),  # User 1 follows User 2
       (1, 2, 1),  # User 2 follows User 1
       (3, 1, 2),  # Check mutual following between User 1 and User 2
       (2, 1, 2),  # User 1 unfollows User 2
       (3, 1, 2)   # Check mutual following between User 1 and User 2
   ]
   ```

4. **Output**: The results of the mutual following checks will be printed to the console in the order they were requested.

## Example Output

For the example operations provided, the output will be:
```
Yes
No
```

## Notes

- Ensure that the user IDs provided in the operations are within the range of 1 to N (the total number of users).
- The application is designed to handle a large number of users and operations efficiently.

## Support

If you encounter any issues or have questions regarding the Twidai application, please reach out to our support team at [support@twidai.com](mailto:support@twidai.com).

```

This manual provides a comprehensive guide for users to understand the functionality of the Twidai application, how to set it up, and how to use it effectively.