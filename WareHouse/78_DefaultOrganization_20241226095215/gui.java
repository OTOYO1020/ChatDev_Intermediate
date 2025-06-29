import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * GUI class to handle the user interface and functionality of the BudgetOptimizerLite Plus application.
 */
public class GUI {
    private JFrame frame;
    private JPanel panel;
    private JLabel incomeLabel;
    private JTextField incomeField;
    private JLabel expensesLabel;
    private JTextField expensesField;
    private JButton inputButton;
    private JLabel goalsLabel;
    private JTextField goalsField;
    private JButton setGoalsButton;
    private JLabel savingsLabel;
    private JTextField savingsField;
    private JButton trackSavingsButton;
    /**
     * Method to initialize and setup the GUI.
     */
    public void start() {
        frame = new JFrame("BudgetOptimizerLite Plus");
        panel = new JPanel(new GridLayout(4, 2));
        incomeLabel = new JLabel("Income:");
        incomeField = new JTextField();
        expensesLabel = new JLabel("Expenses:");
        expensesField = new JTextField();
        inputButton = new JButton("Input");
        goalsLabel = new JLabel("Goals:");
        goalsField = new JTextField();
        setGoalsButton = new JButton("Set Goals");
        savingsLabel = new JLabel("Savings:");
        savingsField = new JTextField();
        trackSavingsButton = new JButton("Track Savings");
        panel.add(incomeLabel);
        panel.add(incomeField);
        panel.add(expensesLabel);
        panel.add(expensesField);
        panel.add(inputButton);
        panel.add(goalsLabel);
        panel.add(goalsField);
        panel.add(setGoalsButton);
        panel.add(savingsLabel);
        panel.add(savingsField);
        panel.add(trackSavingsButton);
        frame.add(panel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
        inputButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                inputIncomeAndExpenses();
            }
        });
        setGoalsButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                setGoals();
            }
        });
        trackSavingsButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                trackSavingsProgress();
            }
        });
    }
    /**
     * Method to allow users to input their income and expenses.
     */
    public void inputIncomeAndExpenses() {
        String incomeText = incomeField.getText();
        String expensesText = expensesField.getText();
        // Check if the input fields are empty
        if (incomeText.isEmpty() || expensesText.isEmpty()) {
            JOptionPane.showMessageDialog(frame, "Please enter both income and expenses.");
            return;
        }
        try {
            double income = Double.parseDouble(incomeText);
            double expenses = Double.parseDouble(expensesText);
            // Perform necessary operations with the income and expenses values
            // For example, you can calculate the remaining budget or display a message based on the values
            // Clear the input fields
            incomeField.setText("");
            expensesField.setText("");
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(frame, "Invalid input. Please enter numeric values for income and expenses.");
        }
    }
    /**
     * Method to allow users to set their budget goals.
     */
    public void setGoals() {
        String goalsText = goalsField.getText();
        // Check if the input field is empty
        if (goalsText.isEmpty()) {
            JOptionPane.showMessageDialog(frame, "Please enter a goal.");
            return;
        }
        try {
            double goals = Double.parseDouble(goalsText);
            // Perform necessary operations with the goals value
            // For example, you can store the goals in a data structure or display a message based on the value
            // Clear the input field
            goalsField.setText("");
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(frame, "Invalid input. Please enter a numeric value for goals.");
        }
    }
    /**
     * Method to track the user's savings progress over time.
     */
    public void trackSavingsProgress() {
        String savingsText = savingsField.getText();
        // Check if the input field is empty
        if (savingsText.isEmpty()) {
            JOptionPane.showMessageDialog(frame, "Please enter savings.");
            return;
        }
        try {
            double savings = Double.parseDouble(savingsText);
            // Perform necessary operations with the savings value
            // For example, you can calculate the progress towards the savings goal or display a message based on the value
            // Clear the input field
            savingsField.setText("");
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(frame, "Invalid input. Please enter a numeric value for savings.");
        }
    }
}