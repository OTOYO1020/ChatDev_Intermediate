Here's the `manual.md` file for the jewels application, detailing its main functions, installation instructions, and usage guidelines.

```markdown
# Jewels Application

Calculate the maximum number of blue jewels of level 1 through conversions of red and blue jewels.

## Main Functions

The Jewels Application provides a single main function:

- **max_blue_jewels(N: int, X: int, Y: int) -> int**: 
  - Calculates the maximum number of blue jewels of level 1 based on the provided parameters:
    - `N`: The level of the red jewels (must be between 1 and 10).
    - `X`: The number of blue jewels obtained from converting one red jewel of level N.
    - `Y`: The number of blue jewels obtained from converting one blue jewel of level (N-1).

## Installation

To run the Jewels Application, ensure you have Python installed on your machine. You can install the required dependencies using pip. 

### Quick Install

```bash
pip install -r requirements.txt
```

### Environment Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   Create a `requirements.txt` file with the necessary dependencies (if any) and run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. **Run the Application**:
   Execute the main script to start the application:
   ```bash
   python main.py
   ```

2. **Input Handling**:
   - The application will prompt you to enter three integers:
     - `N`: Enter a value between 1 and 10.
     - `X`: Enter the number of blue jewels obtained from converting one red jewel.
     - `Y`: Enter the number of blue jewels obtained from converting one blue jewel of the previous level.

3. **Output**:
   - After entering the values, the application will calculate and display the maximum number of blue jewels of level 1.

### Example Usage

```plaintext
Enter N (1-10): 5
Enter X (blue jewels from red): 3
Enter Y (blue jewels from blue): 2
Maximum Blue Jewels of Level 1: 15
```

## Error Handling

- If you enter a value for `N` that is less than 1 or greater than 10, the application will return `0` as an invalid case.
- If non-integer values are entered, the application will prompt you to enter valid integers.

## Conclusion

The Jewels Application is a simple yet powerful tool for calculating the maximum number of blue jewels through conversions. For any issues or feature requests, please reach out to the development team.

```

This manual provides a comprehensive overview of the application, ensuring users can easily understand how to install, run, and utilize the software effectively.