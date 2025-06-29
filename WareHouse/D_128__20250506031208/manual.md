Here's a detailed user manual for the Jewels Management System, formatted in Markdown:

```markdown
# Jewels Management System

A comprehensive application for managing jewel operations and maximizing the sum of jewel values.

## Main Functions

The Jewels Management System allows users to perform the following operations on a collection of jewels:

- **Add Jewels**: Take jewels from either end of the collection.
- **Remove Jewels**: Return jewels to either end of the collection.
- **Calculate Maximum Sum**: Keep track of the maximum possible sum of jewel values in hand after performing a series of operations.

## Quick Install

To get started with the Jewels Management System, ensure you have Python installed on your machine. Then, clone the repository and run the following commands:

```bash
# Clone the repository
git clone <repository-url>

# Navigate into the project directory
cd jewels_management_system

# Install required dependencies
pip install -r requirements.txt
```

## How to Use the Jewels Management System

1. **Run the Application**: Execute the main application file to start the program.

   ```bash
   python main.py
   ```

2. **Input Data**: When prompted, enter the following:
   - The number of jewels (N).
   - The maximum number of operations (K).
   - The jewel values as a comma-separated list.

   Example input:
   ```
   Enter number of jewels (N): 5
   Enter maximum operations (K): 3
   Enter jewel values (comma-separated): 10, 20, 30, 40, 50
   ```

3. **View Results**: After processing the operations, the application will output the maximum sum of the values of jewels in hand.

   Example output:
   ```
   90
   ```

## How It Works

The application uses a deque (double-ended queue) to manage the jewels efficiently. The operations available are:

- **Operation A**: Remove the leftmost jewel from the deque and add its value to your hand.
- **Operation B**: Remove the rightmost jewel from the deque and add its value to your hand.
- **Operation C**: Insert a jewel from your hand to the left end of the deque.
- **Operation D**: Insert a jewel from your hand to the right end of the deque.

The program explores all possible combinations of these operations up to K times to find the maximum sum of jewel values in hand.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.x
- Collections (part of the standard library)

## Additional Information

For further details on how to extend or modify the application, please refer to the code comments within `main.py` and `jewels_handler.py`.

For any issues or feature requests, please contact the development team at [support@chatdev.com](mailto:support@chatdev.com).

Happy jewel managing!
```

This manual provides a comprehensive overview of the Jewels Management System, including installation instructions, usage guidelines, and a brief explanation of how the system operates.