Here's a detailed user manual for the City Connections application, formatted in Markdown as requested:

```markdown
# City Connections

A simple application to manage and visualize connections between cities using an adjacency list representation.

## Main Functions

The City Connections application allows users to:
- Input the number of cities and roads.
- Define connections between cities.
- View the number of directly connected cities for each city along with the list of those cities.

## Quick Install

To run the City Connections application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can run the application directly without any additional dependencies. However, if you wish to use the GUI version, ensure you have the Tkinter library, which is included with most Python installations.

## How to Use the Application

### Running the Command-Line Version

1. **Open your terminal or command prompt.**
2. **Navigate to the directory where the `main.py` file is located.**
3. **Run the application using the following command:**
   ```bash
   python main.py
   ```
4. **Input the number of cities (N) and roads (M) when prompted.**
5. **For each road, input the pair of cities (A_i, B_i) that are connected.**
6. **The application will output the number of directly connected cities for each city along with the sorted list of those cities.**

### Running the GUI Version

1. **Open your terminal or command prompt.**
2. **Navigate to the directory where the `app.py` file is located.**
3. **Run the application using the following command:**
   ```bash
   python app.py
   ```
4. **A GUI window will appear.**
5. **Enter the number of cities in the first input field.**
6. **In the text area, enter each road on a new line in the format `A B`, where A and B are the city numbers.**
7. **Click the "Submit" button.**
8. **The results will be displayed in the text area below, showing the number of directly connected cities and their respective city numbers.**

## Error Handling

- If you enter a number of cities that is less than or equal to zero, or a number of roads that is negative, the application will display an error message.
- If you attempt to connect a city to itself or provide invalid city indices, the application will raise an error and display a message indicating the issue.

## Example Input/Output

### Command-Line Version Example

```
Input:
5 4
1 2
1 3
2 4
3 5

Output:
2 2 3
1 4
1 5
0
```

### GUI Version Example

```
Input:
Number of Cities: 5
Roads:
1 2
1 3
2 4
3 5

Output:
2 2 3
1 4
1 5
0
```

## Conclusion

The City Connections application is a straightforward tool for managing city connections. Whether you prefer a command-line interface or a graphical user interface, this application provides a simple way to visualize and manage city relationships.
```

This manual provides a comprehensive overview of the City Connections application, including installation instructions, usage guidelines, and examples to help users effectively utilize the software.