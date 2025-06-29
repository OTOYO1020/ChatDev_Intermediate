Here's a detailed user manual for the handle change application, formatted in Markdown as requested:

```markdown
# Handle Change Application

A user handle management system that allows users to change their handles while ensuring that no two users have the same handle at the same time.

## Main Functions

The Handle Change Application provides the following functionalities:

- **User Handle Management**: Allows users to input their current and desired handles.
- **Handle Change Processing**: Processes the handle changes while ensuring that all constraints are met.
- **Change Order Display**: Outputs the order in which handle changes are made or an error message if the changes cannot be fulfilled.

## Installation

To run the Handle Change Application, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This application does not require any external libraries beyond Python's standard library. However, ensure that you have Python 3.x installed.

## How to Use the Application

1. **Clone the Repository**: If you haven't already, clone the repository containing the application code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main script to start the application.

   ```bash
   python main.py
   ```

3. **Input the Number of Users**: When prompted, enter the integer \( N \) representing the number of users.

   ```
   Enter the number of users: 3
   ```

4. **Input Current and Desired Handles**: For each user, input their current handle followed by their desired handle.

   ```
   Enter current handle: user1
   Enter desired handle: new_user1
   Enter current handle: user2
   Enter desired handle: new_user2
   Enter current handle: user3
   Enter desired handle: new_user1  # This will trigger the temporary handle change logic if 'new_user1' is already in use.
   ```

5. **View the Result**: After all inputs are provided, the application will process the handle changes and display the order of changes or an error message if the requests cannot be fulfilled.

   ```
   Change Order:
   user1 -> new_user1
   user2 -> new_user2
   ```

## Error Handling

If the application encounters a situation where it cannot fulfill the handle change requests due to constraints (e.g., a desired handle is already in use and no temporary handle can be found), it will output an error message:

```
Error: Cannot fulfill handle change requests.
```

## Conclusion

The Handle Change Application is a straightforward tool for managing user handles while ensuring that all constraints are respected. By following the steps outlined in this manual, users can easily change their handles without conflicts.

For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive overview of the application, its functionalities, installation steps, and usage instructions, ensuring that users can effectively utilize the software.