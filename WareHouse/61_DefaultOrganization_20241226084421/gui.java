import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface of the application.
 */
public class GUI {
    private JFrame frame;
    private JButton button;
    private JLabel totalExpensesLabel; // Label to display the total expenses
    private ExpenseTracker expenseTracker; // Reference to the ExpenseTracker class
    public GUI(ExpenseTracker expenseTracker) {
        this.expenseTracker = expenseTracker; // Assign the reference to the ExpenseTracker class
        // Create the main frame
        frame = new JFrame("Expense Tracker");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        // Create the button
        button = new JButton("Add Expense");
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                showExpenseDialog();
            }
        });
        // Create the total expenses label
        totalExpensesLabel = new JLabel("Total Expenses: $0.00");
        // Create a panel to hold the button and label
        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());
        panel.add(button, BorderLayout.NORTH);
        panel.add(totalExpensesLabel, BorderLayout.CENTER);
        // Add the panel to the frame
        frame.getContentPane().add(panel);
    }
    public void start() {
        // Show the frame
        frame.setVisible(true);
    }
    private void showExpenseDialog() {
        // Show an input dialog to get the expense amount
        String expenseAmountString = JOptionPane.showInputDialog(frame, "Enter expense amount:");
        if (expenseAmountString != null && !expenseAmountString.isEmpty()) {
            try {
                double expenseAmount = Double.parseDouble(expenseAmountString);
                if (expenseAmount >= 0) { // Check if expense amount is greater than or equal to zero
                    // Add the expense to the ExpenseTracker
                    expenseTracker.addExpense(expenseAmount);
                    // Update the total expenses label
                    totalExpensesLabel.setText("Total Expenses: $" + expenseTracker.getTotalExpenses());
                    // Show a message dialog
                    JOptionPane.showMessageDialog(frame, "Expense added successfully!");
                } else {
                    JOptionPane.showMessageDialog(frame, "Invalid expense amount! Expense amount should be greater than or equal to zero.");
                }
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(frame, "Invalid expense amount! Please enter a valid number.");
            }
        } else {
            JOptionPane.showMessageDialog(frame, "Expense amount not provided!");
        }
    }
}