import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface (GUI) of the application.
 */
public class GUI {
    private JFrame frame;
    private JButton button;
    private JLabel label;
    private JTextField expenseField;
    private JComboBox<String> categoryDropdown;
    private JTextField goalAmountField;
    private JTextField goalDateField;
    private JProgressBar progressBar;
    // Create instances of ExpenseTracker and SavingsTracker
    private ExpenseTracker expenseTracker;
    private SavingsTracker savingsTracker;
    public void initialize() {
        // Create the main frame
        frame = new JFrame("BudgetSaver");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        // Create the button
        button = new JButton("Add Expense");
        button.addActionListener(new ButtonClickListener());
        // Create the label
        label = new JLabel("Hello, World!");
        // Create text fields for expense input, goal setting, and progress tracking
        expenseField = new JTextField(10);
        goalAmountField = new JTextField(10);
        goalDateField = new JTextField(10);
        // Create a dropdown menu for expense categorization
        String[] categories = {"Food", "Transportation", "Housing", "Entertainment", "Other"};
        categoryDropdown = new JComboBox<>(categories);
        // Create a progress bar for tracking savings goal progress
        progressBar = new JProgressBar();
        progressBar.setStringPainted(true);
        // Add the components to the frame
        frame.getContentPane().setLayout(new FlowLayout());
        frame.getContentPane().add(new JLabel("Expense:"));
        frame.getContentPane().add(expenseField);
        frame.getContentPane().add(new JLabel("Category:"));
        frame.getContentPane().add(categoryDropdown);
        frame.getContentPane().add(button);
        frame.getContentPane().add(new JLabel("Savings Goal Amount:"));
        frame.getContentPane().add(goalAmountField);
        frame.getContentPane().add(new JLabel("Savings Goal Date:"));
        frame.getContentPane().add(goalDateField);
        frame.getContentPane().add(new JLabel("Progress:"));
        frame.getContentPane().add(progressBar);
        frame.getContentPane().add(label);
        // Initialize the ExpenseTracker and SavingsTracker
        expenseTracker = new ExpenseTracker();
        savingsTracker = new SavingsTracker();
        // Make the frame visible
        frame.setVisible(true);
    }
    /**
     * This class represents the action listener for the button.
     */
    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            // Get the expense details from the input fields
            String expense = expenseField.getText();
            String category = (String) categoryDropdown.getSelectedItem();
            // Add the expense to the ExpenseTracker
            expenseTracker.addExpense(expense, category);
            // Update the label text when the button is clicked
            label.setText("Expense added!");
            // Clear the input fields
            expenseField.setText("");
        }
    }
}