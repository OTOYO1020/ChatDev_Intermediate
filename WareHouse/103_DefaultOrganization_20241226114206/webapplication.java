/**
 * This class represents the web application and handles the overall functionality.
 */
import gui.GUI;
import expensetracker.ExpenseTracker;
import budgetmanager.BudgetManager;
import reportgenerator.ReportGenerator;
public class WebApplication {
    private ExpenseTracker expenseTracker;
    private BudgetManager budgetManager;
    private ReportGenerator reportGenerator;
    public WebApplication() {
        // Initialize the expense tracker, budget manager, and report generator
        expenseTracker = new ExpenseTracker();
        budgetManager = new BudgetManager();
        reportGenerator = new ReportGenerator();
    }
    public void run() {
        // Initialize the GUI
        GUI gui = new GUI(expenseTracker, budgetManager, reportGenerator);
        gui.show();
        // Perform other necessary operations
        // Generate the report
        reportGenerator.generateReport(expenseTracker.getExpenses(), budgetManager.getBudgets());
        // Close the GUI
        gui.close();
    }
}