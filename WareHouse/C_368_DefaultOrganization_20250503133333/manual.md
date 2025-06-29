Here's a detailed user manual for the Enemy Battle simulation software, formatted in Markdown:

```markdown
# Enemy Battle Simulation

Welcome to the Enemy Battle Simulation software! This application allows users to simulate a battle against a series of enemies, each with their own health values. The goal is to determine how many turns it takes to defeat all enemies.

## Main Functions

- **Input Handling**: Read the number of enemies and their respective health values from the user.
- **Battle Logic**: Simulate the battle where each enemy's health is reduced based on the turn number.
- **Turn Tracking**: Keep track of the total number of turns taken to defeat all enemies.
- **Output**: Display the total number of turns taken once all enemies are defeated.

## Installation

To run the Enemy Battle Simulation, you need to set up your environment and install the necessary dependencies. Follow these steps:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   # List of dependencies (if any)
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Software

1. **Run the Application**:
   Execute the main application file:
   ```bash
   python main.py
   ```

2. **Input the Number of Enemies**:
   You will be prompted to enter the number of enemies. For example:
   ```
   Enter the number of enemies: 3
   ```

3. **Input the Health Values**:
   Enter the health values for each enemy as comma-separated integers. For example:
   ```
   Enter the health values (comma-separated integers, e.g., 10,20,30): 10,20,30
   ```

4. **Battle Simulation**:
   The simulation will run, and you will see the progress as the enemies are defeated.

5. **View Results**:
   Once all enemies are defeated, the total number of turns taken will be displayed:
   ```
   Total turns taken to defeat all enemies: X
   ```

6. **Exit the Program**:
   You can type 'exit' at any input prompt to terminate the program.

## Example Usage

Here’s a quick example of how to use the application:

1. Start the application:
   ```
   python main.py
   ```

2. Input:
   ```
   Enter the number of enemies: 3
   Enter the health values (comma-separated integers, e.g., 10,20,30): 10,20,30
   ```

3. Output:
   ```
   Total turns taken to defeat all enemies: 15
   ```

## Conclusion

The Enemy Battle Simulation is a simple yet engaging way to understand turn-based battle mechanics. Feel free to modify the code for enhancements or additional features!

For any questions or support, please contact the development team.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and examples to help users get started effectively.