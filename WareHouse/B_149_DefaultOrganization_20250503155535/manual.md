Here's a detailed user manual for the cookie simulation software, structured in Markdown format as requested:

```markdown
# Cookie Simulation Program

A simple application to simulate cookie actions between two players, Takahashi and Aoki.

## Overview

This program allows users to input the number of cookies that Takahashi and Aoki have, as well as the number of actions to perform. The program will then simulate the actions of decrementing the cookie counts based on the specified rules.

## Main Functions

- **Input Handling**: The program prompts the user to enter the number of cookies for both players and the number of actions to perform, ensuring that all inputs are non-negative integers.
- **Simulation Logic**: The program simulates the actions where Takahashi and Aoki decrement their cookie counts based on the rules provided.
- **Output**: After the simulation, the program displays the remaining cookies for both players.

## Installation

To run the Cookie Simulation Program, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This program does not require any external libraries beyond the standard Python library. Ensure you have Python 3.x installed.

## How to Use the Program

1. **Clone the Repository**: If you have the source code in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Program**: Execute the main application file using Python.
   ```bash
   python main.py
   ```

3. **Input Values**: Follow the prompts to enter:
   - The number of cookies Takahashi has (A).
   - The number of cookies Aoki has (B).
   - The number of actions to perform (K).

4. **View Results**: After entering the required values, the program will display the remaining cookies for both Takahashi and Aoki.

## Example Usage

```plaintext
Please enter the number of cookies that Takahashi has: 5
Please enter the number of cookies that Aoki has: 3
Please enter the number of actions to perform: 7
Remaining cookies - Takahashi: 0, Aoki: 1
```

## Notes

- Ensure that you enter non-negative integers for the number of cookies and actions. The program will prompt you to re-enter values if invalid inputs are provided.
- The program handles the scenario where both players run out of cookies gracefully, doing nothing when both counts reach zero.

## Support

For any issues or questions regarding the Cookie Simulation Program, please reach out to our support team at [support@chatdev.com](mailto:support@chatdev.com).

Happy simulating!
```

This manual provides a comprehensive guide for users to understand and utilize the cookie simulation software effectively. Let me know if you need any further modifications or additional information!