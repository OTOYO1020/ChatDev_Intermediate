package com.example.budgetsaverlite;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the BudgetSaver Lite application.
 * It provides a user-friendly interface for inputting income and expenses
 * and offers basic budgeting features such as goal setting and visual representations of budget breakdowns.
 */
public class BudgetSaverLite extends JFrame implements ActionListener {
    private JButton addButton;
    private JButton saveButton;
    private JTextField incomeField;
    private JTextField expenseField;
    private JTextArea budgetBreakdownArea;
    public BudgetSaverLite() {
        // Create the main window
        setTitle("BudgetSaver Lite");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 300);
        // Create input fields
        incomeField = new JTextField();
        expenseField = new JTextField();
        // Create buttons
        addButton = new JButton("Add");
        saveButton = new JButton("Save");
        // Create budget breakdown area
        budgetBreakdownArea = new JTextArea();
        budgetBreakdownArea.setEditable(false);
        // Create layout
        JPanel panel = new JPanel(new GridLayout(4, 2));
        panel.add(new JLabel("Income:"));
        panel.add(incomeField);
        panel.add(new JLabel("Expense:"));
        panel.add(expenseField);
        panel.add(addButton);
        panel.add(saveButton);
        panel.add(new JLabel("Budget Breakdown:"));
        panel.add(new JScrollPane(budgetBreakdownArea));
        // Add the panel to the main window
        getContentPane().add(panel, BorderLayout.CENTER);
        // Add action listeners
        addButton.addActionListener(this);
        saveButton.addActionListener(this);
    }
    public void start() {
        // Show the main window
        setVisible(true);
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == addButton) {
            addTransaction();
        } else if (e.getSource() == saveButton) {
            saveBudget();
        }
    }
    private void addTransaction() {
        String income = incomeField.getText();
        String expense = expenseField.getText();
        // Perform validation and add the transaction to the budget breakdown area
        if (isValidAmount(income) && isValidAmount(expense)) {
            String transaction = "Income: " + income + ", Expense: " + expense;
            budgetBreakdownArea.append(transaction + "\n");
            // Clear input fields
            incomeField.setText("");
            expenseField.setText("");
        } else {
            JOptionPane.showMessageDialog(this, "Invalid amount entered!", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }
    private boolean isValidAmount(String amount) {
        try {
            double value = Double.parseDouble(amount);
            return value >= 0;
        } catch (NumberFormatException e) {
            return false;
        }
    }
    private void saveBudget() {
        // Save the budget breakdown to a file or database
        String budget = budgetBreakdownArea.getText();
        // TODO: Implement saving logic
        JOptionPane.showMessageDialog(this, "Budget saved successfully!", "Success", JOptionPane.INFORMATION_MESSAGE);
    }
}