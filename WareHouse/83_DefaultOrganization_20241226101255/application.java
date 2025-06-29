import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the application that handles the GUI and starts the budget manager.
 */
public class Application {
    private JTextField incomeTextField;
    private JTextField expenseTextField;
    private BudgetManager budgetManager;
    public void start() {
        // Initialize the GUI and start the application logic
        SwingUtilities.invokeLater(() -> {
            // Create and show the main application window
            JFrame frame = new JFrame("Budget Manager Lite");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(800, 600);
            // Create GUI components
            JPanel panel = new JPanel();
            panel.setLayout(new GridLayout(3, 2));
            JLabel incomeLabel = new JLabel("Income:");
            incomeTextField = new JTextField();
            JLabel expenseLabel = new JLabel("Expense:");
            expenseTextField = new JTextField();
            JButton addButton = new JButton("Add");
            JButton summaryButton = new JButton("Summary");
            // Add action listeners to buttons
            addButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    addIncomeOrExpense();
                }
            });
            summaryButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    displayBudgetSummary();
                }
            });
            // Add components to panel
            panel.add(incomeLabel);
            panel.add(incomeTextField);
            panel.add(expenseLabel);
            panel.add(expenseTextField);
            panel.add(addButton);
            panel.add(summaryButton);
            // Add panel to frame
            frame.getContentPane().add(panel);
            frame.setVisible(true);
            // Create an instance of the BudgetManager class
            budgetManager = new BudgetManager();
        });
    }
    private void addIncomeOrExpense() {
        String incomeText = incomeTextField.getText();
        String expenseText = expenseTextField.getText();
        if (!incomeText.isEmpty()) {
            double income = Double.parseDouble(incomeText);
            budgetManager.addIncome(income);
        }
        if (!expenseText.isEmpty()) {
            double expense = Double.parseDouble(expenseText);
            budgetManager.addExpense(expense);
        }
        // Clear text fields
        incomeTextField.setText("");
        expenseTextField.setText("");
    }
    private void displayBudgetSummary() {
        budgetManager.displayBudgetSummary();
    }
}