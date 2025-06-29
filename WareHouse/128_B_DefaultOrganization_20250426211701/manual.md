Here's the `manual.md` file for the restaurant sorting application:

```markdown
# Restaurant Sorting Application

A simple application to manage and sort restaurants based on their city and score.

## Main Functions

The Restaurant Sorting Application allows users to:

- Input the number of restaurants.
- Enter the city name and score for each restaurant.
- Sort the restaurants primarily by city name in lexicographical order.
- For restaurants with the same city name, sort them by score in descending order.
- Display the sorted identification numbers of the restaurants.

## Installation

To run the Restaurant Sorting Application, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

1. **Python**: Ensure you have Python 3.x installed.
2. **Tkinter**: This library is included with most Python installations. If you encounter issues, you may need to install it separately based on your operating system.

To install any additional dependencies, you can use pip:

```bash
pip install tkinter
```

## How to Use the Application

### Running the Console Application

1. Open your terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run the application using the following command:

   ```bash
   python main.py
   ```

4. Follow the prompts to enter the number of restaurants and their details (city name and score).

### Running the GUI Application

1. Open your terminal or command prompt.
2. Navigate to the directory where `app.py` is located.
3. Run the application using the following command:

   ```bash
   python app.py
   ```

4. The GUI will open, allowing you to enter the number of restaurants, city names, and scores.
5. Click on the "Set Number of Restaurants" button to initialize the application.
6. Enter the city name and score for each restaurant and click "Add Restaurant" to add them to the list.
7. Click on "Show Sorted IDs" to display the sorted identification numbers in the list box.

## Example Usage

1. **Console Application**:
   ```
   Enter the number of restaurants: 3
   Enter city name and score for restaurant 1 (separated by space): NewYork 85
   Enter city name and score for restaurant 2 (separated by space): LosAngeles 90
   Enter city name and score for restaurant 3 (separated by space): NewYork 95
   Sorted restaurant IDs: 3 1 2
   ```

2. **GUI Application**:
   - Set the number of restaurants to `3`.
   - Add the following entries:
     - City: `NewYork`, Score: `85`
     - City: `LosAngeles`, Score: `90`
     - City: `NewYork`, Score: `95`
   - Click "Show Sorted IDs" to see the sorted IDs displayed in the list box.

## Conclusion

This application provides a user-friendly way to manage and sort restaurant data based on city and score. Whether you prefer a console or GUI interface, the Restaurant Sorting Application is designed to meet your needs.
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and examples to help users effectively utilize the software.