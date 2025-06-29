import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import expensetracker.ExpenseTracker;
import budgetmanager.BudgetManager;
import reportgenerator.ReportGenerator;
/**
 * This class represents the graphical user interface of the web application.
 */
public class GUI {
    private JFrame frame;
    private ExpenseTracker expenseTracker;
    private BudgetManager budgetManager;
    private ReportGenerator reportGenerator;
    public GUI(ExpenseTracker expenseTracker, BudgetManager budgetManager, ReportGenerator reportGenerator) {
        this.expenseTracker = expenseTracker;
        this.budgetManager = budgetManager;
        this.reportGenerator = reportGenerator;
        // Initialize the frame
        frame = new JFrame("Expense Budget Planner");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        // Add components to the frame
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(4, 2));
        JLabel expenseLabel = new JLabel("Expense:");
        JTextField expenseField = new JTextField();
        JLabel categoryLabel = new JLabel("Category:");
        JTextField categoryField = new JTextField();
        JLabel budgetLabel = new JLabel("Budget Limit:");
        JTextField budgetField = new JTextField();
        JButton addButton = new JButton("Add Expense");
        addButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String expense = expenseField.getText();
                String category = categoryField.getText();
                double budgetLimit = Double.parseDouble(budgetField.getText());
                // Add the expense to the expense tracker
                expenseTracker.addExpense(new Expense(expense, category, budgetLimit));
                // Clear the input fields
                expenseField.setText("");
                categoryField.setText("");
                budgetField.setText("");
            }
        });
        panel.add(expenseLabel);
        panel.add(expenseField);
        panel.add(categoryLabel);
        panel.add(categoryField);
        panel.add(budgetLabel);
        panel.add(budgetField);
        panel.add(addButton);
        frame.getContentPane().add(panel);
    }
    public void show() {
        // Show the frame
        frame.setVisible(true);
    }
    public void close() {
        // Close the frame
        frame.dispose();
    }
}