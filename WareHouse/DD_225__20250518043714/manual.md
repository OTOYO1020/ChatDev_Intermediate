Here's a detailed user manual for the toy train network software, formatted in Markdown as requested:

```markdown
# Toy Train Network

Manage and visualize connections between toy train cars with ease.

## Overview

The Toy Train Network application allows users to connect and disconnect toy train cars, as well as retrieve the connected components of the network. This software is designed to handle multiple queries efficiently, making it suitable for managing up to 100,000 queries.

## Main Functions

1. **Connect Cars**: Establish a connection between two toy train cars.
2. **Disconnect Cars**: Remove the connection between two toy train cars.
3. **Retrieve Connected Component**: Get a list of all cars connected to a specified car.

## Installation

To run the Toy Train Network application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Use pip to install the required dependencies. Open your terminal or command prompt and run:

   ```bash
   pip install tkinter
   ```

   Note: `tkinter` is included with most Python installations, but if you encounter issues, please refer to the [tkinter documentation](https://docs.python.org/3/library/tkinter.html) for installation instructions.

## How to Use the Application

### Running the Application

1. **Clone the Repository**: Download or clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd toy_train_network
   ```

2. **Run the GUI**: Execute the following command to start the application:

   ```bash
   python gui.py
   ```

### Using the GUI

Once the application is running, you will see a graphical user interface (GUI) with the following functionalities:

- **Connect Cars**: 
  - Enter the car numbers you wish to connect in the "Connect Cars" section.
  - Click the "Connect" button to establish the connection.

- **Disconnect Cars**: 
  - Enter the car numbers you wish to disconnect in the "Disconnect Cars" section.
  - Click the "Disconnect" button to remove the connection.

- **Retrieve Connected Component**: 
  - Enter the car number for which you want to retrieve the connected component in the "Retrieve Component for Car" section.
  - Click the "Retrieve" button to display the connected cars.

### Error Handling

The application includes error handling to ensure that invalid inputs are managed gracefully. If you enter an invalid car number or attempt to connect/disconnect cars incorrectly, an error message will be displayed.

### Example Usage

1. Connect Car 1 to Car 2.
2. Connect Car 2 to Car 3.
3. Retrieve the connected component for Car 1, which should display Cars 1, 2, and 3.
4. Disconnect Car 2 from Car 3.
5. Retrieve the connected component for Car 1 again, which should now display Cars 1 and 2.

## Unit Testing

The application includes unit tests to validate the functionality of each query type and the overall `process_queries` function. You can run the tests by executing the following command in the terminal:

```bash
python -m unittest main.py
```

## Conclusion

The Toy Train Network application is a powerful tool for managing connections between toy train cars. With its intuitive GUI and efficient query processing, users can easily visualize and manipulate the network of cars. For any issues or feature requests, please reach out to the development team.

```

This manual provides a comprehensive guide for users to understand the functionalities of the Toy Train Network application, how to install it, and how to interact with it effectively.