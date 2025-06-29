import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class gui extends JFrame {
    private JTextField incomeField;
    private JTextField expenseField;
    public gui() {
        // Initialize the GUI components and layout
        // Add input fields for income and expenses
        incomeField = new JTextField();
        expenseField = new JTextField();
        // Add buttons for goal setting and visual representations
        JButton goalButton = new JButton("Set Goal");
        JButton visualizeButton = new JButton("Visualize Budget");
        // Set the size and position of the window
        setSize(800, 600);
        setLocationRelativeTo(null); // Center the window on the screen
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Create a panel to hold the components
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(4, 1));
        panel.add(new JLabel("Income:"));
        panel.add(incomeField);
        panel.add(new JLabel("Expense:"));
        panel.add(expenseField);
        panel.add(goalButton);
        panel.add(visualizeButton);
        // Add the panel to the frame
        add(panel);
        // Add action listeners to the buttons
        goalButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle goal setting
                String income = incomeField.getText();
                String expense = expenseField.getText();
                // Perform goal setting logic
                double remainingBudget = Double.parseDouble(income) - Double.parseDouble(expense);
                // Display the remaining budget to the user
                JOptionPane.showMessageDialog(null, "Remaining Budget: $" + remainingBudget);
            }
        });
        visualizeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle visualization
                String income = incomeField.getText();
                String expense = expenseField.getText();
                // Perform visualization logic
                // Add your visualization logic here
            }
        });
    }
    // Implement other methods for handling user interactions and updating the budget
}