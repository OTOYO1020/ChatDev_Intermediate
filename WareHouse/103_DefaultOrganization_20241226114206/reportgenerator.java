import java.util.List;
import expense.Expense;
import budget.Budget;
/**
 * This class represents the report generator and handles the generation of expense reports and visualizations.
 */
public class ReportGenerator {
    public void generateReport(List<Expense> expenses, List<Budget> budgets) {
        // Generate the report based on the expenses and budgets
        for (Expense expense : expenses) {
            System.out.println("Expense: " + expense.getExpense());
            System.out.println("Category: " + expense.getCategory());
            System.out.println("Budget Limit: " + expense.getBudgetLimit());
            System.out.println("------------------------");
        }
        for (Budget budget : budgets) {
            System.out.println("Category: " + budget.getCategory());
            System.out.println("Limit: " + budget.getLimit());
            System.out.println("------------------------");
        }
    }
}