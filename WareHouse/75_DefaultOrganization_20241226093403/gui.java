/**
 * This class represents the graphical user interface of the web application.
 * It contains all the necessary components and handles user interactions.
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;
public class GUI {
    private JFrame frame;
    private JButton addButton;
    private JButton budgetButton;
    private JButton reportButton;
    private ExpenseManager expenseManager;
    private BudgetManager budgetManager;
    private ReportGenerator reportGenerator;
    public void initialize() {
        // Create the main frame
        frame = new JFrame("ExpensePlanner");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        // Create buttons
        addButton = new JButton("Add Expense");
        budgetButton = new JButton("Set Budget");
        reportButton = new JButton("Generate Report");
        // Add action listeners to buttons
        addButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Handle add expense button click event
                AddExpenseDialog dialog = new AddExpenseDialog(frame);
                dialog.setVisible(true);
                if (dialog.isConfirmed()) {
                    Expense expense = dialog.getExpense();
                    expenseManager.addExpense(expense);
                    showMessage("Expense added successfully!");
                }
            }
        });
        budgetButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Handle set budget button click event
                SetBudgetDialog dialog = new SetBudgetDialog(frame);
                dialog.setVisible(true);
                if (dialog.isConfirmed()) {
                    Budget budget = dialog.getBudget();
                    budgetManager.addBudget(budget);
                    showMessage("Budget set successfully!");
                }
            }
        });
        reportButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Handle generate report button click event
                Report report = reportGenerator.generateReport(expenseManager, budgetManager);
                showReport(report);
            }
        });
        // Add the buttons to the frame
        frame.getContentPane().setLayout(new FlowLayout());
        frame.getContentPane().add(addButton);
        frame.getContentPane().add(budgetButton);
        frame.getContentPane().add(reportButton);
        // Display the frame
        frame.setVisible(true);
    }
    private void showMessage(String message) {
        JOptionPane.showMessageDialog(frame, message);
    }
    private void showReport(Report report) {
        String reportDetails = "Report details:\n\n";
        reportDetails += "Total Expenses: $" + report.getTotalExpenses() + "\n";
        reportDetails += "Total Budgets: $" + report.getTotalBudgets() + "\n";
        reportDetails += "Remaining Budget: $" + report.getRemainingBudget() + "\n";
        reportDetails += "Budget Breakdown:\n";
        for (Budget budget : report.getBudgets()) {
            reportDetails += budget.getCategory() + ": $" + budget.getLimit() + "\n";
        }
        JOptionPane.showMessageDialog(frame, reportDetails);
    }
    public void setExpenseManager(ExpenseManager expenseManager) {
        this.expenseManager = expenseManager;
    }
    public void setBudgetManager(BudgetManager budgetManager) {
        this.budgetManager = budgetManager;
    }
    public void setReportGenerator(ReportGenerator reportGenerator) {
        this.reportGenerator = reportGenerator;
    }
}