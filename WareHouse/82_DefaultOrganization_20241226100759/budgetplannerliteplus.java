import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface of the application.
 * It creates and manages the main window and its components.
 */
public class BudgetPlannerLitePlus {
    private JFrame frame;
    private JTextField incomeField;
    private JTextField expenseField;
    private JButton addButton;
    private JTextArea budgetTextArea;
    private JTextField goalField;
    private JButton setGoalButton;
    private JLabel savingsLabel;
    private double savingsGoal;
    private double savingsAmount;
    public BudgetPlannerLitePlus() {
        // Create the main window
        frame = new JFrame("BudgetPlannerLite Plus");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        // Create income and expense input fields
        incomeField = new JTextField(10);
        expenseField = new JTextField(10);
        // Create an "Add" button to add income and expense
        addButton = new JButton("Add");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                addIncomeAndExpense();
            }
        });
        // Create a text area to display budget breakdown
        budgetTextArea = new JTextArea();
        budgetTextArea.setEditable(false);
        // Create a goal input field and a "Set Goal" button
        goalField = new JTextField(10);
        setGoalButton = new JButton("Set Goal");
        setGoalButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                setSavingsGoal();
            }
        });
        // Create a label to display savings progress
        savingsLabel = new JLabel();
        // Create a panel to hold the components
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(6, 1));
        panel.add(new JLabel("Income:"));
        panel.add(incomeField);
        panel.add(new JLabel("Expense:"));
        panel.add(expenseField);
        panel.add(addButton);
        panel.add(budgetTextArea);
        panel.add(new JLabel("Savings Goal:"));
        panel.add(goalField);
        panel.add(setGoalButton);
        panel.add(savingsLabel);
        // Add the panel to the main window
        frame.getContentPane().add(panel, BorderLayout.CENTER);
    }
    public void start() {
        // Display the main window
        frame.setVisible(true);
    }
    private void addIncomeAndExpense() {
        double income = Double.parseDouble(incomeField.getText());
        double expense = Double.parseDouble(expenseField.getText());
        // Calculate the budget breakdown
        double savings = income - expense;
        double expensesPercentage = (expense / income) * 100;
        double savingsPercentage = 100 - expensesPercentage;
        // Update the budget breakdown text area
        budgetTextArea.setText("Expenses: " + expensesPercentage + "%\nSavings: " + savingsPercentage + "%");
        // Update the savings amount
        savingsAmount += savings;
        updateSavingsLabel();
    }
    private void setSavingsGoal() {
        savingsGoal = Double.parseDouble(goalField.getText());
        updateSavingsLabel();
    }
    private void updateSavingsLabel() {
        // Calculate the savings progress
        double savingsProgress = (savingsAmount / savingsGoal) * 100;
        // Update the savings label
        savingsLabel.setText("Savings Progress: " + savingsProgress + "%");
    }
}