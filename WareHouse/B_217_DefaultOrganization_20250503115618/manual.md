Here's a detailed user manual for the AtCoder contest series checker software, formatted in Markdown as requested:

```markdown
# AtCoder Contest Series Checker

A simple application to check the remaining contest series held by AtCoder based on user input.

## Overview

This software allows users to input three contest series from AtCoder and determines which series are still available. The available series are: **ABC**, **ARC**, **AGC**, and **AHC**. The application will inform the user of any additional series that are still held by AtCoder after their input.

## Main Functions

- **Input Handling**: The application prompts the user to enter three valid contest series while ensuring no duplicates are entered.
- **Series Calculation**: It calculates the remaining series by comparing the user's input against the held series.
- **Output**: The application outputs either the remaining series or a message indicating that there are no additional series.

## Installation

To set up the environment and run the AtCoder Contest Series Checker, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Since this project does not rely on any third-party libraries, you can directly run the application without additional installations. However, ensure you have Python installed on your system.

3. **Run the Application**:
   Execute the following command in your terminal:
   ```bash
   python main.py
   ```

## How to Use

1. **Start the Application**: Run the `main.py` script as described above.
2. **Input Contest Series**: When prompted, enter three contest series from the following options:
   - `ABC`
   - `ARC`
   - `AGC`
   - `AHC`
   
   Ensure that you do not enter duplicates. The application will guide you if you enter an invalid series or a duplicate.

3. **View Results**: After entering three valid series, the application will display:
   - A list of remaining series that are still held by AtCoder, or
   - A message stating "No additional series" if all series have been entered.

## Example Usage

```
Please enter three contest series from the following options: 'ABC', 'ARC', 'AGC', 'AHC'
ABC
You still need to enter 2 valid contest series.
ARC
You still need to enter 1 valid contest series.
AGC
No additional series
```

## Conclusion

The AtCoder Contest Series Checker is a straightforward tool to help users quickly identify which contest series are still available based on their input. For any issues or feedback, please contact the support team.

```

This manual provides a comprehensive guide for users to understand the software's purpose, installation process, and usage instructions. Let me know if you need any modifications or additional information!