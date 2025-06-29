package GUI;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class GUI {
    private JFrame frame;
    private JButton addButton;
    private JButton calculateButton;
    private JTextField incomeField;
    private JTextField expenseField;
    private JTextField savingsGoalField;
    private JTextArea budgetBreakdownArea;
    public void start() {
        frame = new JFrame("Budget Manager");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Create and configure GUI components
        addButton = new JButton("Add");
        calculateButton = new JButton("Calculate");
        incomeField = new JTextField(10);
        expenseField = new JTextField(10);
        savingsGoalField = new JTextField(10);
        budgetBreakdownArea = new JTextArea(10, 20);
        budgetBreakdownArea.setEditable(false);
        // Add action listeners to buttons
        addButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                addButtonClicked();
            }
        });
        calculateButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                calculateButtonClicked();
            }
        });
        // Add components to frame
        frame.setLayout(new FlowLayout());
        frame.add(new JLabel("Income:"));
        frame.add(incomeField);
        frame.add(new JLabel("Expense:"));
        frame.add(expenseField);
        frame.add(new JLabel("Savings Goal:"));
        frame.add(savingsGoalField);
        frame.add(addButton);
        frame.add(calculateButton);
        frame.add(new JScrollPane(budgetBreakdownArea));
        frame.pack();
        frame.setVisible(true);
    }
    private void addButtonClicked() {
        // Implement logic for adding income or expense
        double income = Double.parseDouble(incomeField.getText());
        double expense = Double.parseDouble(expenseField.getText());
        double savingsGoal = Double.parseDouble(savingsGoalField.getText());
        BudgetManager budgetManager = new BudgetManager(income, expense, savingsGoal);
        String breakdown = budgetManager.getBudgetBreakdown();
        budgetBreakdownArea.setText(breakdown);
    }
    private void calculateButtonClicked() {
        // Implement logic for calculating budget breakdown
        addButtonClicked();
    }
}