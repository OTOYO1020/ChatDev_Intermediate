```markdown
# City Journey Simulation

Welcome to the City Journey Simulation software! This application allows users to simulate a journey through a series of cities connected by roads. The journey is managed through a graphical user interface (GUI) built with Tkinter, where users can input the number of cities and the roads connecting them.

## Main Functions

- **Input Cities and Roads**: Users can specify the number of cities and the roads connecting them in a user-friendly dialog.
- **Simulate Journey**: The application simulates Takahashi's journey, visiting cities in a depth-first manner and backtracking when necessary.
- **Display Visited Sequence**: The sequence of cities visited during the journey is displayed in the GUI.

## Installation and Environment Setup

To run the City Journey Simulation, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Tkinter**: Tkinter is included with most Python installations. If you encounter issues, you can install it using:
   - For Windows: Tkinter is included with the standard Python installation.
   - For Ubuntu: Run `sudo apt-get install python3-tk`.
   - For macOS: Tkinter is included with the standard Python installation.

3. **Clone the Repository**: Clone the repository containing the application code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

4. **Run the Application**: Execute the main Python script to start the application.
   ```bash
   python main.py
   ```

## How to Use the Application

1. **Start the Application**: Run the `main.py` script to launch the City Journey Simulation GUI.

2. **Input Number of Cities**:
   - In the input dialog that appears, enter the total number of cities (N). Ensure that N is at least 1.

3. **Input Roads**:
   - Enter the roads connecting the cities in the format `A B`, where A and B are the city numbers. Each road should be entered on a new line. 
   - For example:
     ```
     1 2
     1 3
     2 4
     ```
   - After entering all roads, click the "Submit" button.

4. **View the Visited Sequence**:
   - Once the journey simulation is complete, the sequence of visited cities will be displayed in the main window under "Visited Sequence".

5. **End the Journey**: The journey will automatically end when all reachable cities have been visited or when the journey returns to City 1.

## Example Usage

1. Launch the application.
2. Input `4` for the number of cities.
3. Input the following roads:
   ```
   1 2
   1 3
   2 4
   ```
4. Click "Submit" to start the journey.
5. Observe the visited sequence displayed in the application.

## Conclusion

The City Journey Simulation is a simple yet effective tool for visualizing journeys through connected cities. Feel free to explore different configurations of cities and roads to see how the journey changes!

For any issues or feedback, please reach out to the development team.
```