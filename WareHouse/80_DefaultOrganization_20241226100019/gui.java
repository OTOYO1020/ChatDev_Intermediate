import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import javax.swing.JOptionPane;
import javax.swing.JLabel;
import javax.swing.JPanel;
import IncomeExpenseData;
/**
 * This class represents the graphical user interface of the SavingsPlanner application.
 * It contains the main window and handles user interactions.
 */
public class GUI {
    private JFrame frame;
    private JButton addButton;
    private JTextField incomeField;
    private JTextField expenseField;
    private JTextField categoryField;
    private JTextField savingsTargetField;
    private ArrayList<IncomeExpenseData> data;
    public GUI() {
        // Create the main window
        frame = new JFrame("SavingsPlanner");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        // Create input fields
        incomeField = new JTextField(10);
        expenseField = new JTextField(10);
        categoryField = new JTextField(10);
        savingsTargetField = new JTextField(10);
        // Create buttons
        addButton = new JButton("Add");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle add button click event
                addIncomeExpense();
                updateGUI(); // Update the GUI after adding income/expense data
            }
        });
        // Create layout
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(5, 2));
        panel.add(new JLabel("Income:"));
        panel.add(incomeField);
        panel.add(new JLabel("Expense:"));
        panel.add(expenseField);
        panel.add(new JLabel("Category:"));
        panel.add(categoryField);
        panel.add(new JLabel("Savings Target:"));
        panel.add(savingsTargetField);
        panel.add(new JLabel(""));
        panel.add(addButton);
        // Add the panel to the main window
        frame.getContentPane().add(panel);
        // Initialize the data structure
        data = new ArrayList<>();
    }
    /**
     * Starts the GUI by making the main window visible.
     */
    public void start() {
        frame.setVisible(true);
    }
    /**
     * Adds the income and expense data entered by the user to the data structure.
     * Updates the GUI and shows a message dialog.
     */
    private void addIncomeExpense() {
        // Get input values
        double income = Double.parseDouble(incomeField.getText());
        double expense = Double.parseDouble(expenseField.getText());
        String category = categoryField.getText();
        double savingsTarget = Double.parseDouble(savingsTargetField.getText());
        // Create an instance of the income/expense data class
        IncomeExpenseData incomeExpenseData = new IncomeExpenseData(income, expense, category, savingsTarget);
        // Add the income/expense data object to the data structure
        data.add(incomeExpenseData);
        // Update the GUI after adding income/expense data
        updateGUI();
        // Show a message dialog
        JOptionPane.showMessageDialog(frame, "Income and expense added successfully!");
    }
    /**
     * Calculates the savings progress and updates the GUI components.
     */
    private void updateGUI() {
        // Calculate savings progress and update GUI components
        double totalSavingsTarget = 0;
        double totalExpense = 0;
        for (IncomeExpenseData incomeExpenseData : data) {
            totalSavingsTarget += incomeExpenseData.getSavingsTarget();
            totalExpense += incomeExpenseData.getExpense();
        }
        double savingsProgress = (totalSavingsTarget - totalExpense) / totalSavingsTarget * 100;
        // Update GUI components to display savings progress
        frame.setTitle("SavingsPlanner - Savings Progress: " + String.format("%.2f", savingsProgress) + "%");
    }
}